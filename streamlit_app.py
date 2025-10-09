# streamlit_app.py - IMPROVED UI/UX VERSION
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import get_custom_css, get_healthcare_icons
from utils import (
    load_models, preprocess_input, create_gauge_chart,
    create_feature_importance_chart, create_rf_prediction_chart,
    get_health_recommendations, calculate_risk_factors
)

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)
icons = get_healthcare_icons()

# ============================================================================
# LOAD MODELS
# ============================================================================
@st.cache_resource
def get_models():
    return load_models()

models_dict = get_models()
if models_dict is None:
    st.error("❌ **Error**: Tidak dapat memuat model")
    st.stop()

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'prediction_made' not in st.session_state:
    st.session_state.prediction_made = False
if 'prediction_result' not in st.session_state:
    st.session_state.prediction_result = None
if 'form_data' not in st.session_state:
    st.session_state.form_data = {}

# ============================================================================
# NAVIGATION FUNCTIONS
# ============================================================================
def navigate_to(page):
    st.session_state.page = page
    st.session_state.step = 1
    st.rerun()

# ============================================================================
# MODERN HEADER WITH NAVIGATION
# ============================================================================
col1, col2, col3 = st.columns([2, 3, 2])

with col1:
    st.markdown(f"""
        <div style="padding: 1rem 0;">
            <h2 style="color: #00D9A3; margin: 0; font-size: 1.8rem;">
                {icons['heart']} HeartCheck AI
            </h2>
        </div>
    """, unsafe_allow_html=True)

with col3:
    nav_col1, nav_col2, nav_col3 = st.columns(3)
    with nav_col1:
        if st.button("🏠 Home", use_container_width=True, 
                     type="primary" if st.session_state.page == 'home' else "secondary"):
            navigate_to('home')
    with nav_col2:
        if st.button("🩺 Check", use_container_width=True,
                     type="primary" if st.session_state.page == 'predict' else "secondary"):
            navigate_to('predict')
    with nav_col3:
        if st.button("ℹ️ Info", use_container_width=True,
                     type="primary" if st.session_state.page == 'info' else "secondary"):
            navigate_to('info')

st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)

# ============================================================================
# HOME PAGE
# ============================================================================
if st.session_state.page == 'home':
    
    # Hero Section
    st.markdown(f"""
        <div class="hero-section">
            <div class="hero-content">
                <h1 class="hero-title">Deteksi Dini Risiko Penyakit Jantung</h1>
                <p class="hero-subtitle">
                    Gunakan kekuatan AI untuk mengetahui risiko kesehatan jantung Anda. 
                    Cepat, akurat, dan mudah digunakan.
                </p>
                <div class="hero-stats">
                    <div class="stat-item">
                        <div class="stat-number">88.6%</div>
                        <div class="stat-label">Akurasi</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-number">2 Min</div>
                        <div class="stat-label">Waktu Check</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-number">100%</div>
                        <div class="stat-label">Gratis</div>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # CTA Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🩺 Mulai Pemeriksaan Sekarang", use_container_width=True, type="primary"):
            navigate_to('predict')
    
    st.markdown("<div style='margin: 3rem 0;'></div>", unsafe_allow_html=True)
    
    # How It Works Section
    st.markdown(f"""
        <div class="section-title">
            <h2>Cara Kerja Sistem</h2>
            <p>Proses sederhana dalam 3 langkah</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
            <div class="step-card">
                <div class="step-number">1</div>
                <div class="step-icon">📝</div>
                <h3 class="step-title">Input Data</h3>
                <p class="step-desc">Masukkan data kesehatan Anda melalui form yang mudah diikuti</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="step-card">
                <div class="step-number">2</div>
                <div class="step-icon">🤖</div>
                <h3 class="step-title">AI Analisis</h3>
                <p class="step-desc">Model machine learning menganalisis data dengan akurasi 88.6%</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class="step-card">
                <div class="step-number">3</div>
                <div class="step-icon">📊</div>
                <h3 class="step-title">Hasil & Saran</h3>
                <p class="step-desc">Dapatkan hasil prediksi dan rekomendasi kesehatan personal</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin: 3rem 0;'></div>", unsafe_allow_html=True)
    
    # Features Section
    st.markdown(f"""
        <div class="section-title">
            <h2>Mengapa HeartCheck AI?</h2>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">🎯</div>
                <h3>Akurasi Tinggi</h3>
                <p>Model Random Forest dengan akurasi 88.6% yang telah divalidasi</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <h3>Hasil Instant</h3>
                <p>Dapatkan hasil prediksi dalam hitungan detik</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">🔒</div>
                <h3>Data Aman</h3>
                <p>Data Anda tidak disimpan dan tetap privat</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">💡</div>
                <h3>Rekomendasi Personal</h3>
                <p>Saran kesehatan yang disesuaikan dengan kondisi Anda</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Warning Section
    st.markdown("<div style='margin: 3rem 0;'></div>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="warning-box">
            <div class="warning-icon">{icons['warning']}</div>
            <div class="warning-content">
                <h3>Penting untuk Diketahui</h3>
                <p>Hasil prediksi ini <strong>bukan diagnosis medis</strong>. 
                Aplikasi ini hanya memberikan indikasi awal dan sebaiknya dikonsultasikan 
                dengan dokter untuk diagnosis dan penanganan yang tepat.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PREDICTION PAGE - STEP BY STEP
# ============================================================================
elif st.session_state.page == 'predict':
    
    # Progress Bar
    progress = st.session_state.step / 4
    st.markdown(f"""
        <div class="progress-container">
            <div class="progress-bar" style="width: {progress*100}%"></div>
        </div>
        <div class="progress-text">Langkah {st.session_state.step} dari 4</div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    # STEP 1: Personal Info
    if st.session_state.step == 1:
        st.markdown(f"""
            <div class="step-header">
                <h2>{icons['doctor']} Informasi Pribadi</h2>
                <p>Mulai dengan informasi dasar Anda</p>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.number_input(
                "Usia (tahun)",
                min_value=1,
                max_value=120,
                value=st.session_state.form_data.get('age', 50),
                help="Masukkan usia Anda dalam tahun"
            )
            
        with col2:
            sex = st.selectbox(
                "Jenis Kelamin",
                options=["M", "F"],
                format_func=lambda x: "👨 Laki-laki" if x == "M" else "👩 Perempuan",
                index=0 if st.session_state.form_data.get('sex', 'M') == 'M' else 1
            )
        
        st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Lanjut ke Langkah 2 →", use_container_width=True, type="primary"):
                st.session_state.form_data['age'] = age
                st.session_state.form_data['sex'] = sex
                st.session_state.step = 2
                st.rerun()
    
    # STEP 2: Symptoms
    elif st.session_state.step == 2:
        st.markdown(f"""
            <div class="step-header">
                <h2>{icons['stethoscope']} Gejala & Kondisi</h2>
                <p>Ceritakan gejala yang Anda alami</p>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            chest_pain = st.selectbox(
                "Tipe Nyeri Dada",
                options=["ASY", "NAP", "ATA", "TA"],
                format_func=lambda x: {
                    "ASY": "😊 Tidak Ada Nyeri (Asymptomatic)",
                    "NAP": "😐 Nyeri Non-Anginal",
                    "ATA": "😟 Nyeri Atypical Angina",
                    "TA": "😰 Nyeri Typical Angina"
                }[x],
                index=["ASY", "NAP", "ATA", "TA"].index(
                    st.session_state.form_data.get('chest_pain', 'ASY')
                ),
                help="Pilih jenis nyeri dada yang paling sesuai"
            )
            
        with col2:
            exercise_angina = st.selectbox(
                "Nyeri Saat Olahraga?",
                options=["N", "Y"],
                format_func=lambda x: "✅ Tidak" if x == "N" else "⚠️ Ya",
                index=0 if st.session_state.form_data.get('exercise_angina', 'N') == 'N' else 1,
                help="Apakah Anda merasakan nyeri saat berolahraga?"
            )
        
        resting_ecg = st.selectbox(
            "Hasil EKG Istirahat",
            options=["Normal", "ST", "LVH"],
            format_func=lambda x: {
                "Normal": "✅ Normal",
                "ST": "⚠️ ST-T Wave Abnormality",
                "LVH": "⚠️ Left Ventricular Hypertrophy"
            }[x],
            index=["Normal", "ST", "LVH"].index(
                st.session_state.form_data.get('resting_ecg', 'Normal')
            ),
            help="Hasil pemeriksaan EKG saat istirahat"
        )
        
        st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Kembali", use_container_width=True):
                st.session_state.step = 1
                st.rerun()
        with col2:
            if st.button("Lanjut ke Langkah 3 →", use_container_width=True, type="primary"):
                st.session_state.form_data['chest_pain'] = chest_pain
                st.session_state.form_data['exercise_angina'] = exercise_angina
                st.session_state.form_data['resting_ecg'] = resting_ecg
                st.session_state.step = 3
                st.rerun()
    
    # STEP 3: Vital Signs
    elif st.session_state.step == 3:
        st.markdown(f"""
            <div class="step-header">
                <h2>{icons['heart']} Tanda Vital</h2>
                <p>Data pemeriksaan kesehatan</p>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🩸 Tekanan Darah & Gula")
            resting_bp = st.number_input(
                "Tekanan Darah (mm Hg)",
                min_value=80,
                max_value=200,
                value=st.session_state.form_data.get('resting_bp', 120),
                help="Normal: 90-120 mm Hg"
            )
            
            fasting_bs = st.selectbox(
                "Gula Darah Puasa > 120 mg/dl?",
                options=[0, 1],
                format_func=lambda x: "✅ Tidak (< 120)" if x == 0 else "⚠️ Ya (> 120)",
                index=st.session_state.form_data.get('fasting_bs', 0),
                help="Normal: < 100 mg/dl"
            )
            
            cholesterol = st.number_input(
                "Kolesterol Total (mg/dl)",
                min_value=0,
                max_value=600,
                value=st.session_state.form_data.get('cholesterol', 200),
                help="Normal: < 200 mg/dl"
            )
        
        with col2:
            st.markdown("#### ❤️ Detak Jantung")
            max_hr = st.number_input(
                "Detak Jantung Maksimal",
                min_value=60,
                max_value=220,
                value=st.session_state.form_data.get('max_hr', 150),
                help="Saat aktivitas maksimal"
            )
            
            oldpeak = st.number_input(
                "ST Depression (Oldpeak)",
                min_value=-3.0,
                max_value=7.0,
                value=st.session_state.form_data.get('oldpeak', 0.0),
                step=0.1,
                help="Depresi ST yang diukur dari EKG"
            )
            
            st_slope = st.selectbox(
                "ST Slope",
                options=["Up", "Flat", "Down"],
                format_func=lambda x: {"Up": "⬆️ Naik", "Flat": "➡️ Datar", "Down": "⬇️ Turun"}[x],
                index=["Up", "Flat", "Down"].index(
                    st.session_state.form_data.get('st_slope', 'Flat')
                )
            )
        
        st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Kembali", use_container_width=True):
                st.session_state.step = 2
                st.rerun()
        with col2:
            if st.button("Lanjut ke Review →", use_container_width=True, type="primary"):
                st.session_state.form_data.update({
                    'resting_bp': resting_bp,
                    'fasting_bs': fasting_bs,
                    'cholesterol': cholesterol,
                    'max_hr': max_hr,
                    'oldpeak': oldpeak,
                    'st_slope': st_slope
                })
                st.session_state.step = 4
                st.rerun()
    
    # STEP 4: Review & Predict
    elif st.session_state.step == 4:
        st.markdown(f"""
            <div class="step-header">
                <h2>{icons['check']} Review Data</h2>
                <p>Periksa kembali data Anda sebelum analisis</p>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
                <div class="review-card">
                    <h3>👤 Info Pribadi</h3>
                </div>
            """, unsafe_allow_html=True)
            st.write(f"**Usia:** {st.session_state.form_data['age']} tahun")
            st.write(f"**Jenis Kelamin:** {'Laki-laki' if st.session_state.form_data['sex'] == 'M' else 'Perempuan'}")
        
        with col2:
            st.markdown("""
                <div class="review-card">
                    <h3>🩺 Gejala</h3>
                </div>
            """, unsafe_allow_html=True)
            st.write(f"**Nyeri Dada:** {st.session_state.form_data['chest_pain']}")
            st.write(f"**Nyeri saat Olahraga:** {'Ya' if st.session_state.form_data['exercise_angina'] == 'Y' else 'Tidak'}")
            st.write(f"**EKG:** {st.session_state.form_data['resting_ecg']}")
        
        with col3:
            st.markdown("""
                <div class="review-card">
                    <h3>❤️ Vital Signs</h3>
                </div>
            """, unsafe_allow_html=True)
            st.write(f"**Tekanan Darah:** {st.session_state.form_data['resting_bp']} mm Hg")
            st.write(f"**Kolesterol:** {st.session_state.form_data['cholesterol']} mg/dl")
            st.write(f"**Max HR:** {st.session_state.form_data['max_hr']} bpm")
        
        st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Edit Data", use_container_width=True):
                st.session_state.step = 1
                st.rerun()
        with col2:
            if st.button("🔍 Analisis Sekarang", use_container_width=True, type="primary"):
                with st.spinner("🤖 AI sedang menganalisis data Anda..."):
                    try:
                        input_data = {
                            'Age': st.session_state.form_data['age'],
                            'Sex': st.session_state.form_data['sex'],
                            'ChestPainType': st.session_state.form_data['chest_pain'],
                            'RestingBP': st.session_state.form_data['resting_bp'],
                            'Cholesterol': st.session_state.form_data['cholesterol'],
                            'FastingBS': st.session_state.form_data['fasting_bs'],
                            'RestingECG': st.session_state.form_data['resting_ecg'],
                            'MaxHR': st.session_state.form_data['max_hr'],
                            'ExerciseAngina': st.session_state.form_data['exercise_angina'],
                            'Oldpeak': st.session_state.form_data['oldpeak'],
                            'ST_Slope': st.session_state.form_data['st_slope']
                        }
                        
                        X_processed = preprocess_input(
                            input_data, models_dict['scaler'],
                            models_dict['label_encoders'], models_dict['feature_names']
                        )
                        
                        model = models_dict['champion_model']
                        prediction = model.predict(X_processed)[0]
                        probability = model.predict_proba(X_processed)[0]
                        
                        st.session_state.prediction_made = True
                        st.session_state.prediction_result = {
                            'prediction': prediction,
                            'probability': probability[1],
                            'input_data': input_data,
                            'risk_factors': calculate_risk_factors(input_data)
                        }
                        
                        st.success("✅ Analisis selesai!")
                        st.balloons()
                        
                    except Exception as e:
                        st.error(f"❌ Terjadi kesalahan: {str(e)}")

# ============================================================================
# RESULTS SECTION
# ============================================================================
if st.session_state.prediction_made and st.session_state.page == 'predict':
    result = st.session_state.prediction_result
    
    st.markdown("<div style='margin: 3rem 0;'></div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Main Result Card
    if result['prediction'] == 0:
        st.markdown(f"""
            <div class="result-banner result-positive">
                <div class="result-icon-large">💚</div>
                <h1>Risiko Rendah</h1>
                <p>Berdasarkan data yang dianalisis, Anda memiliki risiko rendah terkena penyakit jantung</p>
                <div class="probability-badge">
                    Tingkat Risiko: {result['probability']*100:.1f}%
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="result-banner result-negative">
                <div class="result-icon-large">⚠️</div>
                <h1>Risiko Tinggi</h1>
                <p>Berdasarkan data yang dianalisis, Anda memiliki risiko tinggi terkena penyakit jantung</p>
                <div class="probability-badge">
                    Tingkat Risiko: {result['probability']*100:.1f}%
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Tingkat Risiko")
        gauge_fig = create_gauge_chart(result['probability'], "Probabilitas")
        st.plotly_chart(gauge_fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🎯 Prediksi Model")
        pred_fig = create_rf_prediction_chart(result['probability'])
        st.plotly_chart(pred_fig, use_container_width=True)
    
    # Risk Factors
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    st.markdown("### ⚠️ Faktor Risiko Terdeteksi")
    
    risk_factors = result['risk_factors']
    risk_cols = st.columns(3)
    
    risk_items = [
        ('high_cholesterol', '🔴 Kolesterol Tinggi', f"{result['input_data']['Cholesterol']} mg/dl"),
        ('high_bp', '🔴 Tekanan Darah Tinggi', f"{result['input_data']['RestingBP']} mm Hg"),
        ('high_blood_sugar', '🔴 Gula Darah Tinggi', "Puasa > 120 mg/dl")
    ]
    
    for idx, (key, title, value) in enumerate(risk_items):
        with risk_cols[idx]:
            if risk_factors.get(key, False):
                st.markdown(f"""
                    <div class="risk-badge risk-high">
                        <div class="risk-title">{title}</div>
                        <div class="risk-value">{value}</div>
                    </div>
                """, unsafe_allow_html=True)
    
    # Recommendations
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    st.markdown("### 💡 Rekomendasi untuk Anda")
    
    recommendations = get_health_recommendations(
        result['prediction'], result['probability'], risk_factors
    )
    
    for rec in recommendations:
        st.markdown(f"""
            <div class="recommendation-card">
                {rec}
            </div>
        """, unsafe_allow_html=True)
    
    # Action Buttons
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Lakukan Pemeriksaan Baru", use_container_width=True):
            st.session_state.prediction_made = False
            st.session_state.step = 1
            st.session_state.form_data = {}
            st.rerun()
    with col2:
        if st.button("🏠 Kembali ke Home", use_container_width=True):
            navigate_to('home')

# ============================================================================
# INFO PAGE
# ============================================================================
elif st.session_state.page == 'info':
    
    st.markdown(f"""
        <div class="section-title">
            <h2>📊 Informasi Model & Teknologi</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Model Performance
    metadata = models_dict['metadata']
    
    col1, col2, col3, col4 = st.columns(4)
    
    metrics = [
        (metadata['champion_accuracy']*100, "Akurasi", "🎯"),
        (metadata['champion_precision']*100, "Presisi", "📊"),
        (metadata['champion_recall']*100, "Recall", "🔍"),
        (metadata['champion_roc_auc']*100, "ROC-AUC", "📈")
    ]
    
    for col, (value, label, icon) in zip([col1, col2, col3, col4], metrics):
        with col:
            st.markdown(f"""
                <div class="metric-box">
                    <div class="metric-icon">{icon}</div>
                    <div class="metric-number">{value:.1f}%</div>
                    <div class="metric-name">{label}</div>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    # Technology Stack
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="info-box">
                <h3>🤖 Machine Learning</h3>
                <ul>
                    <li>Random Forest Classifier</li>
                    <li>918 Training Samples</li>
                    <li>11 Input Features</li>
                    <li>5-Fold Cross Validation</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="info-box">
                <h3>💻 Technology Stack</h3>
                <ul>
                    <li>Python & Scikit-learn</li>
                    <li>Streamlit Framework</li>
                    <li>Plotly Visualization</li>
                    <li>Modern Responsive UI</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    # Feature Importance
    st.markdown("### 📊 Fitur Paling Berpengaruh")
    rf_importance_fig = create_feature_importance_chart(
        models_dict['rf_model'], models_dict['feature_names'], top_n=10
    )
    st.plotly_chart(rf_importance_fig, use_container_width=True)
    
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    # About & Disclaimer
    st.markdown("""
        <div class="disclaimer-box">
            <h3>⚠️ Disclaimer Penting</h3>
            <p>Aplikasi ini <strong>BUKAN</strong> alat diagnosis medis. Hasil prediksi bersifat 
            indikatif dan edukatif. Selalu konsultasikan dengan dokter untuk diagnosis dan 
            penanganan yang tepat. Jangan gunakan hasil ini sebagai satu-satunya dasar 
            untuk keputusan medis.</p>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<div style='margin: 3rem 0;'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
    <div class="footer">
        <p>❤️ HeartCheck AI • Powered by Machine Learning</p>
        <p style="font-size: 0.9rem; opacity: 0.7;">© 2024 • Made with Streamlit</p>
    </div>
""", unsafe_allow_html=True)