# styles.py - Modern & Responsive CSS

def get_custom_css():
    """
    Modern, clean, and responsive CSS for heart disease prediction app
    """
    return """
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* ============================================
       GLOBAL STYLES & RESET
    ============================================ */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }
    
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #ffffff 100%);
        padding: 1rem;
    }
    
    /* ============================================
       HERO SECTION
    ============================================ */
    .hero-section {
        background: linear-gradient(135deg, #00D9A3 0%, #00B88F 100%);
        border-radius: 24px;
        padding: 4rem 2rem;
        text-align: center;
        box-shadow: 0 20px 60px rgba(0, 217, 163, 0.25);
        margin-bottom: 3rem;
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: pulse 15s ease-in-out infinite;
    }
    
    .hero-content {
        position: relative;
        z-index: 1;
    }
    
    .hero-title {
        color: white;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 1rem;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        line-height: 1.2;
    }
    
    .hero-subtitle {
        color: rgba(255, 255, 255, 0.95);
        font-size: 1.25rem;
        font-weight: 400;
        max-width: 700px;
        margin: 0 auto 2rem;
        line-height: 1.6;
    }
    
    .hero-stats {
        display: flex;
        justify-content: center;
        gap: 3rem;
        margin-top: 2.5rem;
        flex-wrap: wrap;
    }
    
    .stat-item {
        text-align: center;
    }
    
    .stat-number {
        color: white;
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1rem;
        font-weight: 500;
    }
    
    /* ============================================
       SECTION STYLES
    ============================================ */
    .section-title {
        text-align: center;
        margin: 3rem 0 2rem;
    }
    
    .section-title h2 {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 0.5rem;
    }
    
    .section-title p {
        font-size: 1.1rem;
        color: #718096;
    }
    
    /* ============================================
       STEP CARDS
    ============================================ */
    .step-card {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        position: relative;
        height: 100%;
    }
    
    .step-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 40px rgba(0, 217, 163, 0.2);
    }
    
    .step-number {
        position: absolute;
        top: 1rem;
        right: 1rem;
        background: linear-gradient(135deg, #00D9A3 0%, #00B88F 100%);
        color: white;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 1.2rem;
    }
    
    .step-icon {
        font-size: 4rem;
        margin: 1rem 0;
    }
    
    .step-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 0.75rem;
    }
    
    .step-desc {
        color: #718096;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    /* ============================================
       FEATURE CARDS
    ============================================ */
    .feature-card {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        margin-bottom: 1.5rem;
        border-left: 4px solid #00D9A3;
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateX(8px);
        box-shadow: 0 8px 30px rgba(0, 217, 163, 0.15);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .feature-card h3 {
        color: #1a202c;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 0.75rem;
    }
    
    .feature-card p {
        color: #718096;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    /* ============================================
       WARNING BOX
    ============================================ */
    .warning-box {
        background: linear-gradient(135deg, #FFF3E0 0%, #FFECB3 100%);
        border-radius: 16px;
        padding: 2rem;
        display: flex;
        gap: 1.5rem;
        align-items: flex-start;
        box-shadow: 0 4px 20px rgba(255, 152, 0, 0.15);
    }
    
    .warning-icon {
        font-size: 3rem;
        flex-shrink: 0;
    }
    
    .warning-content h3 {
        color: #E65100;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 0.75rem;
    }
    
    .warning-content p {
        color: #5D4037;
        font-size: 1rem;
        line-height: 1.7;
    }
    
    /* ============================================
       PROGRESS BAR
    ============================================ */
    .progress-container {
        background: #E2E8F0;
        border-radius: 50px;
        height: 8px;
        overflow: hidden;
        margin-bottom: 0.5rem;
    }
    
    .progress-bar {
        background: linear-gradient(90deg, #00D9A3 0%, #00B88F 100%);
        height: 100%;
        border-radius: 50px;
        transition: width 0.5s ease;
    }
    
    .progress-text {
        text-align: center;
        color: #718096;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 2rem;
    }
    
    /* ============================================
       STEP HEADER
    ============================================ */
    .step-header {
        text-align: center;
        margin-bottom: 2.5rem;
    }
    
    .step-header h2 {
        font-size: 2rem;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 0.5rem;
    }
    
    .step-header p {
        font-size: 1.1rem;
        color: #718096;
    }
    
    /* ============================================
       REVIEW CARD
    ============================================ */
    .review-card {
        background: linear-gradient(135deg, #E8F5F3 0%, #FFFFFF 100%);
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1rem;
        border-left: 4px solid #00D9A3;
    }
    
    .review-card h3 {
        color: #00B88F;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 0.75rem;
    }
    
    /* ============================================
       RESULT BANNER
    ============================================ */
    .result-banner {
        border-radius: 24px;
        padding: 3rem;
        text-align: center;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
        margin-bottom: 2rem;
    }
    
    .result-positive {
        background: linear-gradient(135deg, #00D9A3 0%, #00E5B0 100%);
    }
    
    .result-negative {
        background: linear-gradient(135deg, #FF6B6B 0%, #FF8787 100%);
    }
    
    .result-icon-large {
        font-size: 5rem;
        margin-bottom: 1rem;
    }
    
    .result-banner h1 {
        color: white;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 1rem;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    }
    
    .result-banner p {
        color: rgba(255, 255, 255, 0.95);
        font-size: 1.2rem;
        max-width: 600px;
        margin: 0 auto 1.5rem;
        line-height: 1.6;
    }
    
    .probability-badge {
        display: inline-block;
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(10px);
        border-radius: 50px;
        padding: 1rem 2rem;
        color: white;
        font-size: 1.3rem;
        font-weight: 700;
    }
    
    /* ============================================
       RISK BADGES
    ============================================ */
    .risk-badge {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    }
    
    .risk-high {
        border-left: 4px solid #FF6B6B;
    }
    
    .risk-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 0.5rem;
    }
    
    .risk-value {
        font-size: 1.3rem;
        font-weight: 600;
        color: #FF6B6B;
    }
    
    /* ============================================
       RECOMMENDATION CARDS
    ============================================ */
    .recommendation-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.06);
        border-left: 4px solid #00D9A3;
        font-size: 1.05rem;
        line-height: 1.7;
        color: #2D3748;
    }
    
    /* ============================================
       METRIC BOXES
    ============================================ */
    .metric-box {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
    }
    
    .metric-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0, 217, 163, 0.15);
    }
    
    .metric-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    .metric-number {
        font-size: 2.5rem;
        font-weight: 800;
        color: #00D9A3;
        margin-bottom: 0.5rem;
    }
    
    .metric-name {
        font-size: 1rem;
        color: #718096;
        font-weight: 600;
    }
    
    /* ============================================
       INFO BOXES
    ============================================ */
    .info-box {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        height: 100%;
    }
    
    .info-box h3 {
        color: #1a202c;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
    }
    
    .info-box ul {
        list-style: none;
        padding: 0;
    }
    
    .info-box li {
        color: #4A5568;
        font-size: 1.05rem;
        padding: 0.75rem 0;
        border-bottom: 1px solid #E2E8F0;
    }
    
    .info-box li:last-child {
        border-bottom: none;
    }
    
    .info-box li::before {
        content: '✓';
        color: #00D9A3;
        font-weight: 700;
        margin-right: 0.75rem;
    }
    
    /* ============================================
       DISCLAIMER BOX
    ============================================ */
    .disclaimer-box {
        background: linear-gradient(135deg, #FFF3E0 0%, #FFECB3 100%);
        border-radius: 16px;
        padding: 2rem;
        border: 2px solid #FFB74D;
        box-shadow: 0 4px 20px rgba(255, 152, 0, 0.15);
    }
    
    .disclaimer-box h3 {
        color: #E65100;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .disclaimer-box p {
        color: #5D4037;
        font-size: 1.05rem;
        line-height: 1.7;
    }
    
    /* ============================================
       BUTTONS
    ============================================ */
    .stButton > button {
        background: linear-gradient(135deg, #00D9A3 0%, #00B88F 100%);
        color: white;
        font-weight: 600;
        font-size: 1.05rem;
        padding: 0.75rem 2rem;
        border: none;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 217, 163, 0.3);
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #00B88F 0%, #009975 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 217, 163, 0.4);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* ============================================
       INPUTS
    ============================================ */
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        border: 2px solid #E2E8F0;
        border-radius: 10px;
        padding: 0.75rem;
        font-size: 1rem;
        transition: all 0.3s ease;
        background: white;
    }
    
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #00D9A3;
        box-shadow: 0 0 0 3px rgba(0, 217, 163, 0.1);
        outline: none;
    }
    
    /* Input Labels */
    .stNumberInput label,
    .stSelectbox label {
        color: #2D3748;
        font-weight: 600;
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }
    
    /* ============================================
       FOOTER
    ============================================ */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #718096;
        font-size: 0.95rem;
        margin-top: 3rem;
        border-top: 1px solid #E2E8F0;
    }
    
    .footer p {
        margin: 0.5rem 0;
    }
    
    /* ============================================
       ANIMATIONS
    ============================================ */
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.8;
        }
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* ============================================
       RESPONSIVE DESIGN
    ============================================ */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2rem;
        }
        
        .hero-subtitle {
            font-size: 1rem;
        }
        
        .hero-stats {
            gap: 1.5rem;
        }
        
        .stat-number {
            font-size: 2rem;
        }
        
        .section-title h2 {
            font-size: 1.8rem;
        }
        
        .result-banner h1 {
            font-size: 2rem;
        }
        
        .result-banner p {
            font-size: 1rem;
        }
        
        .step-card {
            padding: 1.5rem;
        }
        
        .feature-card {
            padding: 1.5rem;
        }
        
        .warning-box {
            flex-direction: column;
            text-align: center;
        }
    }
    
    @media (max-width: 480px) {
        .main {
            padding: 0.5rem;
        }
        
        .hero-section {
            padding: 2rem 1rem;
            border-radius: 16px;
        }
        
        .hero-title {
            font-size: 1.5rem;
        }
        
        .hero-subtitle {
            font-size: 0.9rem;
        }
        
        .stat-number {
            font-size: 1.5rem;
        }
        
        .stat-label {
            font-size: 0.85rem;
        }
    }
    
    /* ============================================
       HIDE STREAMLIT BRANDING
    ============================================ */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Hide sidebar collapse button */
    button[kind="header"] {
        display: none;
    }
    </style>
    """

def get_healthcare_icons():
    """
    Healthcare-related emoji icons
    """
    return {
        'heart': '❤️',
        'health': '🏥',
        'doctor': '👨‍⚕️',
        'stethoscope': '🩺',
        'pill': '💊',
        'syringe': '💉',
        'ambulance': '🚑',
        'check': '✅',
        'warning': '⚠️',
        'cross': '❌',
        'chart': '📊',
        'info': 'ℹ️',
        'star': '⭐',
        'target': '🎯',
        'shield': '🛡️',
        'success': '🎉',
        'healthy': '💚',
        'caution': '⚡'
    }