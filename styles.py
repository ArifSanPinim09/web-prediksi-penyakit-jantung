# styles.py - Custom CSS Styling untuk Web Kesehatan

def get_custom_css():
    """
    Returns custom CSS for healthcare-themed web application
    """
    return """
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Main Container */
    .main {
        background: linear-gradient(135deg, #E8F5F3 0%, #FFFFFF 100%);
        padding: 2rem;
    }
    
    /* Header Styles */
    .header-container {
        background: linear-gradient(135deg, #00D9A3 0%, #00B88F 100%);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 217, 163, 0.3);
        text-align: center;
        margin-bottom: 2rem;
        animation: fadeInDown 0.8s ease-in-out;
    }
    
    .header-title {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    .header-subtitle {
        color: #E8F5F3;
        font-size: 1.2rem;
        font-weight: 400;
        margin-top: 0.5rem;
    }
    
    /* Card Styles */
    .info-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        margin-bottom: 1.5rem;
        border-left: 5px solid #00D9A3;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0, 217, 163, 0.2);
    }
    
    /* Result Card - Positive (No Disease) */
    .result-card-positive {
        background: linear-gradient(135deg, #00D9A3 0%, #00E5B0 100%);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 217, 163, 0.3);
        text-align: center;
        animation: fadeIn 0.8s ease-in-out;
    }
    
    /* Result Card - Negative (Disease) */
    .result-card-negative {
        background: linear-gradient(135deg, #FF6B6B 0%, #FF8787 100%);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(255, 107, 107, 0.3);
        text-align: center;
        animation: fadeIn 0.8s ease-in-out;
    }
    
    .result-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
    }
    
    .result-title {
        color: white;
        font-size: 2rem;
        font-weight: 700;
        margin: 1rem 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    .result-subtitle {
        color: white;
        font-size: 1.2rem;
        font-weight: 400;
        opacity: 0.9;
    }
    
    .probability-text {
        background: rgba(255, 255, 255, 0.2);
        padding: 1rem;
        border-radius: 10px;
        margin-top: 1rem;
        color: white;
        font-size: 1.5rem;
        font-weight: 600;
    }
    
    /* Metric Cards */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        text-align: center;
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #00D9A3;
        margin: 0.5rem 0;
    }
    
    .metric-label {
        font-size: 1rem;
        color: #7F8C8D;
        font-weight: 500;
    }
    
    /* Button Styles */
    .stButton > button {
        background: linear-gradient(135deg, #00D9A3 0%, #00B88F 100%);
        color: white;
        font-weight: 600;
        font-size: 1.1rem;
        padding: 0.75rem 2rem;
        border: none;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0, 217, 163, 0.3);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #00B88F 0%, #009975 100%);
        box-shadow: 0 8px 20px rgba(0, 217, 163, 0.4);
        transform: translateY(-2px);
    }
    
    /* Sidebar Styles */
    .css-1d391kg {
        background: linear-gradient(180deg, #F0F8F7 0%, #FFFFFF 100%);
    }
    
    /* Input Styles */
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        border: 2px solid #E0E0E0;
        border-radius: 8px;
        padding: 0.5rem;
        transition: border-color 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #00D9A3;
        box-shadow: 0 0 0 0.2rem rgba(0, 217, 163, 0.25);
    }
    
    /* Expander Styles */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #F0F8F7 0%, #E8F5F3 100%);
        border-radius: 10px;
        font-weight: 600;
        color: #2C3E50;
    }
    
    /* Alert Box */
    .alert-info {
        background: #E3F2FD;
        border-left: 5px solid #2196F3;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .alert-warning {
        background: #FFF3E0;
        border-left: 5px solid #FF9800;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .alert-success {
        background: #E8F5E9;
        border-left: 5px solid #4CAF50;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    /* Animation */
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
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Progress Bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #00D9A3 0%, #00E5B0 100%);
    }
    
    /* Tab Styles */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: white;
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #00D9A3 0%, #00B88F 100%);
        color: white;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #7F8C8D;
        font-size: 0.9rem;
        margin-top: 3rem;
        border-top: 1px solid #E0E0E0;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """


def get_healthcare_icons():
    """
    Returns healthcare-related emoji icons
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