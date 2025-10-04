# streamlit_app.py - Random Forest Only Version
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from styles import get_custom_css, get_healthcare_icons
from utils import (
    load_models, 
    preprocess_input, 
    create_gauge_chart,
    create_feature_importance_chart,
    create_rf_prediction_chart,
    get_health_recommendations,
    calculate_risk_factors
)

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="Prediksi Penyakit Jantung",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
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
# SESSION STATE
# ============================================================================
if 'prediction_made' not in st.session_state:
    st.session_state.prediction_made = False
if 'prediction_result' not in st.session_state:
    st.session_state.prediction_result = None

# ============================================================================
# HEADER
# ============================================================================
st.markdown(f"""
    <div class="header-container">
        <h1 class="header-title">{icons['heart']} Sistem Prediksi Penyakit Jantung</h1>
        <p class="header-subtitle">Deteksi Dini Risiko Penyakit Jantung dengan Machine Learning</p>
    </div>
""", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR
# ============================================================================
st.sidebar.image("https://img.icons8.com/color/200/000000/cardiovascular.png", width=150)
st.sidebar.title(f"{icons['stethoscope']} Menu Navigasi")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Pilih Halaman:",
    ["🏠 Beranda", "🩺 Prediksi Kesehatan", "📊 Informasi Model", "ℹ️ Tentang Aplikasi"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.info(f"""
    {icons['info']} **Informasi Sistem**
    
    **Model**: Random Forest  
    **Akurasi**: {models_dict['metadata']['champion_accuracy']*100:.2f}%  
    **Status**: {icons['check']} Aktif
""")

# ============================================================================
# PAGE 1: BERANDA
# ============================================================================
if page == "🏠 Beranda":
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
            <div class="info-card">
                <h2 style="color: #2C3E50;">{icons['health']} Selamat Datang</h2>
                <p style='font-size: 1.1rem; line-height: 1.8; color: #2C3E50;'>
                    Sistem ini menggunakan <strong>Machine Learning Random Forest</strong> untuk membantu 
                    mendeteksi risiko penyakit jantung berdasarkan data kesehatan Anda. Dengan akurasi tinggi 
                    mencapai <strong>{models_dict['metadata']['champion_accuracy']*100:.1f}%</strong>, 
                    sistem ini dapat memberikan prediksi awal yang membantu Anda untuk berkonsultasi 
                    dengan tenaga medis profesional.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
            <div class="alert-warning">
                <strong style="color: #856404;">{icons['warning']} PENTING:</strong> 
                <span style="color: #856404;">Hasil prediksi ini bukan diagnosis medis. 
                Selalu konsultasikan dengan dokter untuk diagnosis dan penanganan yang tepat.</span>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="info-card" style="background: linear-gradient(135deg, #E8F5F3 0%, #FFFFFF 100%);">
                <h3 style="text-align: center; color: #00D9A3;">{icons['chart']} Statistik Sistem</h3>
                <div class="metric-card">
                    <div class="metric-value">{models_dict['metadata']['champion_accuracy']*100:.1f}%</div>
                    <div class="metric-label">Akurasi Model</div>
                </div>
                <div class="metric-card">
                    <div class="metric-value">Random Forest</div>
                    <div class="metric-label" style="color: #7F8C8D;">Algoritma ML</div>
                </div>
                <div class="metric-card">
                    <div class="metric-value">918</div>
                    <div class="metric-label">Data Training</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown(f"## {icons['star']} Fitur Utama Sistem")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
            <div class="info-card">
                <h3 style="color: #00D9A3; text-align: center;">{icons['target']} Akurasi Tinggi</h3>
                <p style="text-align: center; color: #2C3E50;">
                    Model machine learning dengan akurasi <strong>88.6%</strong> 
                    menggunakan algoritma Random Forest.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="info-card">
                <h3 style="color: #00D9A3; text-align: center;">{icons['stethoscope']} Mudah Digunakan</h3>
                <p style="text-align: center; color: #2C3E50;">
                    Interface yang user-friendly dan mudah dipahami. 
                    Input data kesehatan dan dapatkan hasil instant.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class="info-card">
                <h3 style="color: #00D9A3; text-align: center;">{icons['shield']} Rekomendasi Personal</h3>
                <p style="text-align: center; color: #2C3E50;">
                    Dapatkan rekomendasi kesehatan yang dipersonalisasi 
                    berdasarkan hasil prediksi dan faktor risiko.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown(f"## {icons['info']} Cara Kerja Sistem")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
            <div style="text-align: center; padding: 1.5rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">📝</div>
                <h4 style="color: #00D9A3;">1. Input Data</h4>
                <p style="color: #7F8C8D;">Masukkan data kesehatan</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div style="text-align: center; padding: 1.5rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">⚙️</div>
                <h4 style="color: #00D9A3;">2. Analisis AI</h4>
                <p style="color: #7F8C8D;">Model AI menganalisis</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div style="text-align: center; padding: 1.5rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">📊</div>
                <h4 style="color: #00D9A3;">3. Hasil Prediksi</h4>
                <p style="color: #7F8C8D;">Lihat hasil & probabilitas</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
            <div style="text-align: center; padding: 1.5rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">💡</div>
                <h4 style="color: #00D9A3;">4. Rekomendasi</h4>
                <p style="color: #7F8C8D;">Saran kesehatan</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown(f"""
        <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #E8F5F3 0%, #FFFFFF 100%); border-radius: 15px;">
            <h2 style="color: #00D9A3; margin-bottom: 1rem;">{icons['heart']} Siap Memulai?</h2>
            <p style="font-size: 1.2rem; color: #2C3E50; margin-bottom: 2rem;">
                Mulai deteksi dini risiko penyakit jantung Anda sekarang!
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🩺 Mulai Prediksi Sekarang", use_container_width=True, type="primary"):
        st.switch_page("pages/prediksi.py") if hasattr(st, 'switch_page') else st.rerun()

# ============================================================================
# PAGE 2: PREDIKSI KESEHATAN
# ============================================================================
elif page == "🩺 Prediksi Kesehatan":
    
    st.markdown(f"## {icons['stethoscope']} Form Prediksi Kesehatan Jantung")
    
    st.markdown(f"""
        <div class="alert-info">
            <strong style="color: #004085;">{icons['info']} Petunjuk:</strong> 
            <span style="color: #004085;">Lengkapi data dengan akurat untuk hasil prediksi yang optimal.</span>
        </div>
    """, unsafe_allow_html=True)
    
    with st.form("prediction_form"):
        
        st.markdown(f"### {icons['doctor']} Data Pribadi")
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.number_input("Usia (tahun)", 1, 120, 50)
            sex = st.selectbox("Jenis Kelamin", ["M", "F"],
                             format_func=lambda x: "Laki-laki" if x == "M" else "Perempuan")
        
        with col2:
            chest_pain = st.selectbox("Tipe Nyeri Dada", ["TA", "ATA", "NAP", "ASY"],
                                     format_func=lambda x: {
                                         "TA": "Typical Angina",
                                         "ATA": "Atypical Angina",
                                         "NAP": "Non-Anginal Pain",
                                         "ASY": "Asymptomatic"
                                     }[x])
            exercise_angina = st.selectbox("Nyeri saat Olahraga", ["N", "Y"],
                                          format_func=lambda x: "Tidak" if x == "N" else "Ya")
        
        st.markdown("---")
        
        st.markdown(f"### {icons['heart']} Pemeriksaan Vital")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            resting_bp = st.number_input("Tekanan Darah (mm Hg)", 80, 200, 120)
            max_hr = st.number_input("Detak Jantung Maksimal", 60, 220, 150)
        
        with col2:
            cholesterol = st.number_input("Kolesterol (mg/dl)", 0, 600, 200)
            oldpeak = st.number_input("ST Depression", -3.0, 7.0, 0.0, 0.1)
        
        with col3:
            fasting_bs = st.selectbox("Gula Darah Puasa > 120", [0, 1],
                                     format_func=lambda x: "Tidak" if x == 0 else "Ya")
            st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"],
                                   format_func=lambda x: {"Up": "Naik", "Flat": "Datar", "Down": "Turun"}[x])
        
        st.markdown("---")
        
        st.markdown(f"### {icons['chart']} Hasil EKG")
        resting_ecg = st.selectbox("Hasil EKG Istirahat", ["Normal", "ST", "LVH"],
                                   format_func=lambda x: {
                                       "Normal": "Normal",
                                       "ST": "ST-T Wave Abnormality",
                                       "LVH": "Left Ventricular Hypertrophy"
                                   }[x])
        
        st.markdown("---")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            submit_button = st.form_submit_button(f"{icons['target']} Prediksi Sekarang", use_container_width=True)
    
    if submit_button:
        
        with st.spinner("🔄 Memproses data..."):
            
            input_data = {
                'Age': age, 'Sex': sex, 'ChestPainType': chest_pain,
                'RestingBP': resting_bp, 'Cholesterol': cholesterol,
                'FastingBS': fasting_bs, 'RestingECG': resting_ecg,
                'MaxHR': max_hr, 'ExerciseAngina': exercise_angina,
                'Oldpeak': oldpeak, 'ST_Slope': st_slope
            }
            
            try:
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
                
                st.success(f"{icons['check']} Prediksi berhasil! (Random Forest - 88.6% Akurasi)")
                
            except Exception as e:
                st.error(f"❌ Terjadi kesalahan: {str(e)}")
                st.stop()
    
    if st.session_state.prediction_made:
        
        result = st.session_state.prediction_result
        
        st.markdown("---")
        st.markdown(f"## {icons['chart']} Hasil Prediksi")
        
        if result['prediction'] == 0:
            st.markdown(f"""
                <div class="result-card-positive">
                    <div class="result-icon">{icons['healthy']}</div>
                    <h2 class="result-title">Risiko Rendah</h2>
                    <p class="result-subtitle">Sistem memprediksi Anda memiliki risiko rendah terkena penyakit jantung.</p>
                    <div class="probability-text">Probabilitas Risiko: {result['probability']*100:.1f}%</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="result-card-negative">
                    <div class="result-icon">{icons['warning']}</div>
                    <h2 class="result-title">Risiko Tinggi</h2>
                    <p class="result-subtitle">Sistem memprediksi Anda memiliki risiko tinggi terkena penyakit jantung.</p>
                    <div class="probability-text">Probabilitas Risiko: {result['probability']*100:.1f}%</div>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"### {icons['chart']} Tingkat Risiko")
            gauge_fig = create_gauge_chart(result['probability'], "Probabilitas Penyakit Jantung")
            st.plotly_chart(gauge_fig, use_container_width=True)
        
        with col2:
            st.markdown(f"### {icons['target']} Prediksi Model")
            pred_fig = create_rf_prediction_chart(result['probability'])
            st.plotly_chart(pred_fig, use_container_width=True)
        
        st.markdown("---")
        
        st.markdown(f"### {icons['warning']} Faktor Risiko Terdeteksi")
        
        risk_factors = result['risk_factors']
        risk_count = sum(risk_factors.values())
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if risk_factors['high_cholesterol']:
                st.markdown(f"""
                    <div class="info-card" style="border-left-color: #FF6B6B;">
                        <h4 style="color: #FF6B6B;">{icons['caution']} Kolesterol Tinggi</h4>
                        <p style="color: #2C3E50;">Level: {result['input_data']['Cholesterol']} mg/dl<br>
                        <small style="color: #7F8C8D;">(Normal: <200 mg/dl)</small></p>
                    </div>
                """, unsafe_allow_html=True)
        
        with col2:
            if risk_factors['high_bp']:
                st.markdown(f"""
                    <div class="info-card" style="border-left-color: #FF6B6B;">
                        <h4 style="color: #FF6B6B;">{icons['caution']} Tekanan Darah Tinggi</h4>
                        <p style="color: #2C3E50;">Level: {result['input_data']['RestingBP']} mm Hg<br>
                        <small style="color: #7F8C8D;">(Normal: 90-120 mm Hg)</small></p>
                    </div>
                """, unsafe_allow_html=True)
        
        with col3:
            if risk_factors['high_blood_sugar']:
                st.markdown(f"""
                    <div class="info-card" style="border-left-color: #FF6B6B;">
                        <h4 style="color: #FF6B6B;">{icons['caution']} Gula Darah Tinggi</h4>
                        <p style="color: #2C3E50;">Gula darah puasa > 120 mg/dl<br>
                        <small style="color: #7F8C8D;">(Normal: <100 mg/dl)</small></p>
                    </div>
                """, unsafe_allow_html=True)
        
        if risk_count == 0:
            st.markdown(f"""
                <div class="alert-success">
                    <span style="color: #155724;">{icons['check']} <strong>Bagus!</strong> Tidak ada faktor risiko utama terdeteksi.</span>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown(f"### {icons['pill']} Rekomendasi Kesehatan")
        
        recommendations = get_health_recommendations(
            result['prediction'], result['probability'], risk_factors
        )
        
        for rec in recommendations:
            st.markdown(f"""
                <div class="info-card">
                    <p style="margin: 0; font-size: 1.05rem; line-height: 1.8; color: #2C3E50;">{rec}</p>
                </div>
            """, unsafe_allow_html=True)

# ============================================================================
# PAGE 3: INFORMASI MODEL
# ============================================================================
elif page == "📊 Informasi Model":
    
    st.markdown(f"## {icons['chart']} Informasi Model Machine Learning")
    
    st.markdown(f"### {icons['target']} Performa Model")
    
    col1, col2, col3, col4 = st.columns(4)
    
    metadata = models_dict['metadata']
    
    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{metadata['champion_accuracy']*100:.1f}%</div>
                <div class="metric-label">Akurasi</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{metadata['champion_precision']*100:.1f}%</div>
                <div class="metric-label">Presisi</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{metadata['champion_recall']*100:.1f}%</div>
                <div class="metric-label">Recall</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{metadata['champion_roc_auc']*100:.1f}%</div>
                <div class="metric-label">ROC-AUC</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
            <div class="info-card">
                <h3 style="color: #00D9A3;">{icons['info']} Model Champion</h3>
                <p style="color: #2C3E50;"><strong>Nama Model:</strong> {metadata['champion_model_name']}</p>
                <p style="color: #2C3E50;"><strong>Tanggal Training:</strong> {metadata['training_date']}</p>
                <p style="color: #2C3E50;"><strong>Total Data:</strong> 918 samples</p>
                <p style="color: #2C3E50;"><strong>Total Fitur:</strong> {len(metadata['feature_names'])} fitur</p>
                <p style="color: #2C3E50;"><strong>Algoritma:</strong> Random Forest</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="info-card">
                <h3 style="color: #00D9A3;">{icons['star']} Keunggulan Model</h3>
                <ul style="line-height: 2; color: #2C3E50;">
                    <li>✅ Akurasi tinggi (88.6%)</li>
                    <li>✅ Feature engineering advanced</li>
                    <li>✅ Cross-validation 5-fold</li>
                    <li>✅ Hyperparameter tuning optimal</li>
                    <li>✅ Robust & reliable predictions</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown(f"### {icons['chart']} Fitur Paling Berpengaruh")
    
    rf_importance_fig = create_feature_importance_chart(
        models_dict['rf_model'], models_dict['feature_names'], top_n=15
    )
    st.plotly_chart(rf_importance_fig, use_container_width=True)
    
    st.markdown("---")
    
    with st.expander(f"{icons['info']} Detail Teknis Model"):
        st.markdown("#### Random Forest Hyperparameters")
        st.json(metadata['rf_best_params'])

# ============================================================================
# PAGE 4: TENTANG
# ============================================================================
elif page == "ℹ️ Tentang Aplikasi":
    
    st.markdown(f"## {icons['info']} Tentang Aplikasi")
    
    st.markdown(f"""
        <div class="info-card">
            <h3 style="color: #00D9A3;">{icons['heart']} Sistem Prediksi Penyakit Jantung</h3>
            <p style="font-size: 1.1rem; line-height: 1.8; color: #2C3E50;">
                Aplikasi web ini dikembangkan untuk membantu deteksi dini risiko penyakit jantung 
                menggunakan <strong>Machine Learning Random Forest</strong>, yang telah dilatih 
                menggunakan dataset Heart Failure Prediction dari UCI Machine Learning Repository.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown(f"### {icons['target']} Teknologi")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
            <div class="info-card">
                <h4 style="color: #00D9A3;">Machine Learning</h4>
                <ul style="line-height: 2; color: #2C3E50;">
                    <li>🌲 Random Forest Classifier</li>
                    <li>📊 Scikit-learn</li>
                    <li>🔢 NumPy & Pandas</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="info-card">
                <h4 style="color: #00D9A3;">Web Development</h4>
                <ul style="line-height: 2; color: #2C3E50;">
                    <li>🎨 Streamlit</li>
                    <li>📈 Plotly</li>
                    <li>💅 Custom CSS</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown(f"### {icons['warning']} Disclaimer")
    
    st.markdown(f"""
        <div class="alert-warning">
            <h4 style="margin-top: 0; color: #856404;">⚠️ Pernyataan Penting</h4>
            <p style="line-height: 1.8; color: #856404;">
                Aplikasi ini <strong>BUKAN</strong> pengganti diagnosis medis profesional. 
                Hasil prediksi bersifat <strong>indikatif</strong> dan <strong>edukatif</strong>. 
                Selalu konsultasikan dengan dokter untuk diagnosis dan penanganan yang tepat.
            </p>
        </div>
    """, unsafe_allow_html=True)

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("---")
st.markdown(f"""
    <div class="footer">
        <p style="color: #7F8C8D;">{icons['heart']} Heart Disease Prediction System | © 2024</p>
        <p style="font-size: 0.85rem; color: #95A5A6;">
            Powered by Machine Learning • Random Forest • Streamlit
        </p>
    </div>
""", unsafe_allow_html=True)