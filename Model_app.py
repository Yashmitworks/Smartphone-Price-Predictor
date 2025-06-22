import streamlit as st
import pandas as pd
import joblib
import base64
from PIL import Image
import requests
from io import BytesIO

# Load trained model
model = joblib.load("mobile_pricing_model.pkl")
price_labels = ['Low', 'Medium', 'High', 'Very High']

# Page config
st.set_page_config(page_title="📱 Smart Mobile Price Predictor", page_icon="📊", layout="centered")

# App header with style
st.markdown("""
    <style>
        .main-title {
            font-size: 40px;
            font-weight: 700;
            color: #FF4B4B;
            text-align: center;
            margin-bottom: 20px;
        }
        .subtext {
            font-size: 18px;
            text-align: center;
            color: #333;
        }
    </style>
    <div class="main-title">📱 Smart Mobile Price Predictor</div>
    <div class="subtext">Predict the price category of a mobile phone based on its features</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Input fields
st.sidebar.header("🔧 Mobile Specifications")

battery_power = st.sidebar.slider("Battery Power (mAh)", 500, 6000, 3000)
clock_speed = st.sidebar.slider("Clock Speed (GHz)", 0.5, 5.0, 2.0)
fc = st.sidebar.slider("Front Camera (MP)", 0, 64, 16)
int_memory = st.sidebar.slider("Internal Memory (GB)", 2, 512, 64)
mobile_wt = st.sidebar.slider("Mobile Weight (g)", 80, 350, 180)
px_height = st.sidebar.slider("Pixel Height", 0, 3000, 1200)
ram = st.sidebar.slider("RAM (MB)", 256, 16384, 4096)
talk_time = st.sidebar.slider("Talk Time (Hours)", 2, 48, 20)
sc_h = st.sidebar.slider("Screen Height (cm)", 5, 30, 15)
m_dep = st.sidebar.slider("Mobile Depth (cm)", 0.1, 2.0, 0.7)

px_width = st.sidebar.slider("Pixel Width", 500, 3000, 1200)
sc_w = st.sidebar.slider("Screen Width (cm)", 2, 25, 12)
pc = st.sidebar.slider("Primary Camera (MP)", 0, 108, 32)
n_cores = st.sidebar.slider("Number of Cores", 1, 16, 8)

blue = st.sidebar.selectbox("Bluetooth", [0, 1], format_func=lambda x: "Yes" if x else "No")
dual_sim = st.sidebar.selectbox("Dual SIM", [0, 1], format_func=lambda x: "Yes" if x else "No")
four_g = st.sidebar.selectbox("4G", [0, 1], format_func=lambda x: "Yes" if x else "No")
three_g = st.sidebar.selectbox("3G", [0, 1], format_func=lambda x: "Yes" if x else "No")
touch_screen = st.sidebar.selectbox("Touch Screen", [0, 1], format_func=lambda x: "Yes" if x else "No")
wifi = st.sidebar.selectbox("WiFi", [0, 1], format_func=lambda x: "Yes" if x else "No")

# Center image (reliable loading)
try:
    image_url = "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9"
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    st.image(img, use_container_width=True)
except:
    st.warning("Could not load image.")

# Predict button
if st.button("📊 Predict Price Category"):
    input_data = pd.DataFrame([{
        'battery_power': battery_power,
        'blue': blue,
        'clock_speed': clock_speed,
        'dual_sim': dual_sim,
        'fc': fc,
        'four_g': four_g,
        'int_memory': int_memory,
        'm_dep': m_dep,
        'mobile_wt': mobile_wt,
        'n_cores': n_cores,
        'pc': pc,
        'px_height': px_height,
        'px_width': px_width,
        'ram': ram,
        'sc_h': sc_h,
        'sc_w': sc_w,
        'talk_time': talk_time,
        'three_g': three_g,
        'touch_screen': touch_screen,
        'wifi': wifi,
    
    }])

    prediction = model.predict(input_data)[0]
    st.markdown(f"""
        <div style='background-color:#DFF0D8; padding:20px; border-radius:10px;'>
            <h3 style='text-align:center;'>📱 Predicted Price Category: <span style='color:#FF4B4B'>{price_labels[prediction]}</span></h3>
        </div>
    """, unsafe_allow_html=True)

    st.balloons()

# Footer
st.markdown("---")
st.markdown("""<div style='text-align:center; font-size:14px; color:gray;'>
Made by Yashmit Rathee | Powered by XGBoost + Streamlit
</div>""", unsafe_allow_html=True)
