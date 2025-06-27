import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("mobile_pricing_model.pkl")
price_labels = ['Low', 'Medium', 'High', 'Very High']

# App layout
st.set_page_config(page_title="Mobile Price Predictor", layout="centered")
st.title("📱 Mobile Price Prediction App")
st.markdown("""
Enter the specifications of a mobile phone below to predict its price category.
""")

# Input fields with nice layout
col1, col2 = st.columns(2)

with col1:
    battery_power = st.slider("Battery Power (mAh)", 500, 2000, 1000)
    clock_speed = st.slider("Clock Speed (GHz)", 0.5, 3.0, 1.5)
    fc = st.slider("Front Camera (MP)", 0, 20, 5)
    int_memory = st.slider("Internal Memory (GB)", 2, 128, 32)
    mobile_wt = st.slider("Mobile Weight (g)", 80, 250, 150)
    px_height = st.slider("Pixel Height", 0, 1960, 800)
    ram = st.slider("RAM (MB)", 256, 8192, 2048)
    talk_time = st.slider("Talk Time (Hours)", 2, 20, 10)
    sc_h = st.slider("Screen Height (cm)", 5, 20, 12)
    m_dep = st.slider("Mobile Depth (cm)", 0.1, 1.0, 0.5)

with col2:
    px_width = st.slider("Pixel Width", 500, 2000, 800)
    sc_w = st.slider("Screen Width (cm)", 2, 20, 10)
    pc = st.slider("Primary Camera (MP)", 0, 20, 8)
    n_cores = st.slider("Number of Cores", 1, 8, 4)

    blue = st.selectbox("Bluetooth", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    dual_sim = st.selectbox("Dual SIM", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    four_g = st.selectbox("4G", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    three_g = st.selectbox("3G", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    touch_screen = st.selectbox("Touch Screen", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    wifi = st.selectbox("WiFi", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

# Predict button
if st.button("📊 Predict Price Category"):
    # Create dataframe for prediction
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
        'wifi': wifi
    }])

    prediction = model.predict(input_data)[0]
    st.success(f"📱 Predicted Price Category: **{price_labels[prediction]}**")