# utils.py - RF FOCUSED VERSION (XGBoost optional)

import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import os
import pickle

# XGBoost import with fallback
try:
    import xgboost as xgb
    XGBOOST_AVAILABLE = True
except ImportError:
    XGBOOST_AVAILABLE = False
    print("⚠️ XGBoost not available - will use Random Forest only")

# Base directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")

# Kalau models tidak di sini, coba fallback satu level di atas:
if not os.path.exists(MODELS_DIR):
    MODELS_DIR = os.path.join(os.path.dirname(BASE_DIR), "models")


def load_models():
    """
    Load all saved models and preprocessing objects
    Champion Model: Random Forest (88.59% accuracy)
    XGBoost: Optional (for comparison if available)
    """
    try:
        print("\n" + "="*70)
        print("🔄 LOADING MODELS...")
        print("="*70)
        
        # Load Random Forest - CHAMPION MODEL (MUST HAVE)
        rf_path = os.path.join(MODELS_DIR, 'random_forest_model.pkl')
        print(f"\n📂 Loading Random Forest (CHAMPION) from: {rf_path}")
        rf_model = joblib.load(rf_path)
        print("✅ Random Forest loaded successfully - CHAMPION MODEL (88.59% accuracy)")
        
        # Try to load champion_model.pkl (RF Baseline)
        champion_path = os.path.join(MODELS_DIR, 'champion_model.pkl')
        if os.path.exists(champion_path):
            print(f"\n📂 Loading Champion Model from: {champion_path}")
            champion_model = joblib.load(champion_path)
            print("✅ Champion Model (RF Baseline) loaded successfully")
        else:
            champion_model = rf_model  # Use RF Tuned as fallback
            print("ℹ️ Using RF Tuned as champion model")
        
        # Try to load XGBoost (OPTIONAL - for comparison only)
        xgb_model = None
        xgb_available = False
        
        if XGBOOST_AVAILABLE:
            try:
                xgb_path = os.path.join(MODELS_DIR, 'xgboost_model.pkl')
                print(f"\n📂 Attempting to load XGBoost from: {xgb_path}")
                
                # Try multiple loading methods
                try:
                    xgb_model = joblib.load(xgb_path)
                    xgb_available = True
                    print("✅ XGBoost loaded successfully (optional comparison)")
                except:
                    try:
                        with open(xgb_path, 'rb') as f:
                            xgb_model = pickle.load(f)
                        xgb_available = True
                        print("✅ XGBoost loaded successfully with pickle")
                    except Exception as e:
                        print(f"⚠️ XGBoost loading failed: {e}")
                        print("ℹ️ Continuing with Random Forest only (this is fine!)")
            except Exception as e:
                print(f"⚠️ XGBoost not loaded: {e}")
                print("ℹ️ Application will work with Random Forest only")
        else:
            print("\nℹ️ XGBoost library not available - using Random Forest only")
        
        # Load preprocessing objects (REQUIRED)
        print("\n📂 Loading preprocessing objects...")
        scaler = joblib.load(os.path.join(MODELS_DIR, 'scaler.pkl'))
        print("✅ Scaler loaded")
        
        label_encoders = joblib.load(os.path.join(MODELS_DIR, 'label_encoders.pkl'))
        print("✅ Label encoders loaded")
        
        feature_names = joblib.load(os.path.join(MODELS_DIR, 'feature_names.pkl'))
        print("✅ Feature names loaded")
        
        metadata = joblib.load(os.path.join(MODELS_DIR, 'model_metadata.pkl'))
        print("✅ Metadata loaded")
        
        print("\n" + "="*70)
        print("✅ MODELS LOADED SUCCESSFULLY!")
        print("="*70)
        print(f"\n🏆 Champion Model: Random Forest Baseline")
        print(f"   • Accuracy: 88.59%")
        print(f"   • Status: ✅ Active")
        if xgb_available:
            print(f"\n📊 XGBoost Model: Available for comparison")
        else:
            print(f"\n📊 XGBoost Model: Not available (using RF only)")
        print("="*70)
        
        return {
            'rf_model': rf_model,
            'champion_model': champion_model,  # RF Baseline
            'xgb_model': xgb_model,  # May be None
            'xgb_available': xgb_available,
            'scaler': scaler,
            'label_encoders': label_encoders,
            'feature_names': feature_names,
            'metadata': metadata
        }
        
    except Exception as e:
        print(f"\n❌ Critical Error loading models: {str(e)}")
        print(f"📁 Models directory: {MODELS_DIR}")
        print(f"📋 Files in models directory:")
        if os.path.exists(MODELS_DIR):
            for file in os.listdir(MODELS_DIR):
                print(f"   • {file}")
        return None


def preprocess_input(input_data, scaler, label_encoders, feature_names):
    """
    Preprocess user input to match training data format
    """
    # Create DataFrame from input
    df = pd.DataFrame([input_data])
    
    # Handle cholesterol zero values (same as training)
    if df['Cholesterol'].values[0] == 0:
        df['Cholesterol'] = 223.0  # Median from training
    
    # Feature Engineering (same as training)
    # 1. Age Group
    if df['Age'].values[0] <= 40:
        df['AgeGroup'] = 'Young'
    elif df['Age'].values[0] <= 50:
        df['AgeGroup'] = 'Middle'
    elif df['Age'].values[0] <= 60:
        df['AgeGroup'] = 'Senior'
    else:
        df['AgeGroup'] = 'Elderly'
    
    # 2. BP Category
    bp = df['RestingBP'].values[0]
    if bp < 120:
        df['BP_Category'] = 'Normal'
    elif 120 <= bp < 130:
        df['BP_Category'] = 'Elevated'
    elif 130 <= bp < 140:
        df['BP_Category'] = 'High_Stage1'
    else:
        df['BP_Category'] = 'High_Stage2'
    
    # 3. Cholesterol Risk
    chol = df['Cholesterol'].values[0]
    if chol < 200:
        df['Chol_Risk'] = 'Desirable'
    elif 200 <= chol < 240:
        df['Chol_Risk'] = 'Borderline'
    else:
        df['Chol_Risk'] = 'High'
    
    # 4. Heart Rate Category
    max_hr_expected = 220 - df['Age'].values[0]
    hr_percentage = (df['MaxHR'].values[0] / max_hr_expected) * 100
    if hr_percentage < 60:
        df['HR_Category'] = 'Low'
    elif 60 <= hr_percentage < 85:
        df['HR_Category'] = 'Normal'
    else:
        df['HR_Category'] = 'High'
    
    # 5. Risk Score
    df['Risk_Score'] = (
        int(df['Age'].values[0] > 55) +
        int(df['Cholesterol'].values[0] > 240) +
        int(df['RestingBP'].values[0] > 140) +
        int(df['FastingBS'].values[0] == 1) +
        int(df['ExerciseAngina'].values[0] == 'Y') +
        int(df['Oldpeak'].values[0] > 1.5)
    )
    
    # 6. Interaction Features
    df['Age_Cholesterol_Interaction'] = df['Age'] * df['Cholesterol']
    df['Age_MaxHR_Ratio'] = df['Age'] / (df['MaxHR'] + 1)
    
    # Label Encoding for binary/ordinal features
    for col in ['Sex', 'ExerciseAngina', 'ST_Slope', 'FastingBS']:
        if col in df.columns and col in label_encoders:
            le = label_encoders[col]
            df[col] = le.transform(df[col].astype(str))
    
    # One-hot encoding for nominal features
    df = pd.get_dummies(df, columns=['ChestPainType', 'RestingECG', 'AgeGroup', 
                                      'BP_Category', 'Chol_Risk', 'HR_Category'], 
                        drop_first=False, dtype=int)
    
    # Ensure all features from training are present
    for col in feature_names:
        if col not in df.columns:
            df[col] = 0
    
    # Select only the features used in training
    df = df[feature_names]
    
    # Scale the features
    df_scaled = scaler.transform(df)
    
    return df_scaled


def create_gauge_chart(probability, title):
    """Create a gauge chart for probability visualization"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=probability * 100,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title, 'font': {'size': 24, 'color': '#2C3E50'}},
        delta={'reference': 50, 'increasing': {'color': "#FF6B6B"}, 'decreasing': {'color': "#00D9A3"}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 2, 'tickcolor': "#2C3E50"},
            'bar': {'color': "#00D9A3" if probability < 0.5 else "#FF6B6B"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#E0E0E0",
            'steps': [
                {'range': [0, 30], 'color': '#E8F5E9'},
                {'range': [30, 70], 'color': '#FFF3E0'},
                {'range': [70, 100], 'color': '#FFEBEE'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 50
            }
        }
    ))
    
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=60, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        font={'family': 'Poppins, sans-serif'}
    )
    return fig


def create_feature_importance_chart(model, feature_names, top_n=10):
    """Create feature importance bar chart"""
    importance = model.feature_importances_
    indices = np.argsort(importance)[-top_n:]
    
    fig = go.Figure(go.Bar(
        x=importance[indices],
        y=[feature_names[i] for i in indices],
        orientation='h',
        marker=dict(
            color=importance[indices],
            colorscale='Teal',
            showscale=True,
            colorbar=dict(title="Importance")
        )
    ))
    
    fig.update_layout(
        title=f'Top {top_n} Fitur Paling Berpengaruh',
        xaxis_title='Tingkat Kepentingan',
        yaxis_title='Fitur',
        height=400,
        margin=dict(l=20, r=20, t=60, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        font={'family': 'Poppins, sans-serif'}
    )
    return fig


def create_comparison_chart(rf_prob, xgb_prob=None):
    """
    Create model comparison chart
    If XGBoost not available, show RF only
    """
    if xgb_prob is not None:
        # Show both models
        fig = go.Figure(data=[
            go.Bar(
                name='Random Forest (Champion)',
                x=['Tidak Berisiko', 'Berisiko'],
                y=[1-rf_prob, rf_prob],
                marker_color='#00D9A3',
                text=[f'{(1-rf_prob)*100:.1f}%', f'{rf_prob*100:.1f}%'],
                textposition='auto',
            ),
            go.Bar(
                name='XGBoost',
                x=['Tidak Berisiko', 'Berisiko'],
                y=[1-xgb_prob, xgb_prob],
                marker_color='#FF9800',
                text=[f'{(1-xgb_prob)*100:.1f}%', f'{xgb_prob*100:.1f}%'],
                textposition='auto',
            )
        ])
        title_text = 'Perbandingan Prediksi: Random Forest vs XGBoost'
    else:
        # Show RF only
        fig = go.Figure(data=[
            go.Bar(
                name='Random Forest (Champion)',
                x=['Tidak Berisiko', 'Berisiko'],
                y=[1-rf_prob, rf_prob],
                marker_color='#00D9A3',
                text=[f'{(1-rf_prob)*100:.1f}%', f'{rf_prob*100:.1f}%'],
                textposition='auto',
            )
        ])
        title_text = 'Prediksi Random Forest (Champion Model - 88.59% Akurasi)'
    
    fig.update_layout(
        title=title_text,
        xaxis_title='Kategori',
        yaxis_title='Probabilitas',
        barmode='group',
        height=400,
        margin=dict(l=20, r=20, t=60, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        font={'family': 'Poppins, sans-serif'},
        yaxis=dict(tickformat='.0%')
    )
    return fig


def get_health_recommendations(prediction, probability, risk_factors):
    """Generate personalized health recommendations"""
    recommendations = []
    
    if prediction == 1:  # High risk
        recommendations.append("🚨 **Segera Konsultasi dengan Dokter**: Hasil prediksi menunjukkan risiko tinggi penyakit jantung.")
        recommendations.append("📋 **Pemeriksaan Lanjutan**: Disarankan melakukan pemeriksaan jantung lengkap (EKG, Echocardiogram, dll).")
    
    # Risk-specific recommendations
    if risk_factors.get('high_cholesterol', False):
        recommendations.append("🥗 **Kolesterol Tinggi**: Kurangi konsumsi lemak jenuh, perbanyak serat dan omega-3.")
    
    if risk_factors.get('high_bp', False):
        recommendations.append("💊 **Tekanan Darah Tinggi**: Batasi garam, kelola stres, dan rutin monitor tekanan darah.")
    
    if risk_factors.get('exercise_angina', False):
        recommendations.append("⚠️ **Nyeri Dada saat Aktivitas**: Hindari aktivitas berat berlebihan, konsultasi untuk program olahraga yang aman.")
    
    if risk_factors.get('high_blood_sugar', False):
        recommendations.append("🍎 **Gula Darah Tinggi**: Kontrol asupan gula, perbanyak sayuran, dan pertimbangkan cek diabetes.")
    
    # General recommendations
    if prediction == 0:  # Low risk
        recommendations.append("✅ **Pertahankan Gaya Hidup Sehat**: Hasil prediksi baik, terus jaga pola hidup sehat.")
    
    recommendations.append("🏃 **Olahraga Teratur**: Minimal 150 menit aktivitas aerobik sedang per minggu.")
    recommendations.append("😴 **Tidur Cukup**: 7-9 jam per malam untuk kesehatan jantung optimal.")
    recommendations.append("🚭 **Hindari Rokok**: Merokok adalah faktor risiko utama penyakit jantung.")
    recommendations.append("🧘 **Kelola Stres**: Praktikkan teknik relaksasi seperti meditasi atau yoga.")
    
    return recommendations


def calculate_risk_factors(input_data):
    """Identify risk factors from input data"""
    risk_factors = {
        'high_cholesterol': input_data['Cholesterol'] > 240,
        'high_bp': input_data['RestingBP'] > 140,
        'exercise_angina': input_data['ExerciseAngina'] == 'Y',
        'high_blood_sugar': input_data['FastingBS'] == 1,
        'old_age': input_data['Age'] > 60,
        'abnormal_ecg': input_data['RestingECG'] != 'Normal'
    }
    return risk_factors


def create_rf_prediction_chart(rf_prob):
    """
    Create simple Random Forest prediction chart
    """
    import plotly.graph_objects as go
    
    fig = go.Figure(data=[
        go.Bar(
            name='Random Forest',
            x=['Tidak Berisiko', 'Berisiko'],
            y=[1-rf_prob, rf_prob],
            marker_color='#00D9A3',
            text=[f'{(1-rf_prob)*100:.1f}%', f'{rf_prob*100:.1f}%'],
            textposition='auto',
            textfont=dict(size=14, color='white', family='Poppins')
        )
    ])
    
    fig.update_layout(
        title='Prediksi Random Forest (88.6% Akurasi)',
        xaxis_title='Kategori',
        yaxis_title='Probabilitas',
        height=400,
        margin=dict(l=20, r=20, t=60, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        font={'family': 'Poppins, sans-serif'},
        yaxis=dict(tickformat='.0%'),
        showlegend=False
    )
    
    return fig

