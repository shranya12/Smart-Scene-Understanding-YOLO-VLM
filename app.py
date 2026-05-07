import streamlit as st
import cv2
import requests
import numpy as np
from PIL import Image
from detector import detect_objects

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Smart Scene Understanding",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to bottom right, #0b0f19, #111827);
    color: white;
}

h1 {
    color: #00FFD1;
    text-align: center;
    font-size: 48px;
    font-weight: bold;
}

h2, h3 {
    color: #00FFD1;
}

.ai-box {
    background-color: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #00FFD1;
    box-shadow: 0px 0px 15px rgba(0,255,209,0.3);
}

.object-box {
    background-color: rgba(255,255,255,0.08);
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 10px;
    border-left: 5px solid #00FFD1;
}

.high-risk {
    background-color: rgba(255,0,0,0.2);
    border: 2px solid red;
    padding: 15px;
    border-radius: 12px;
    color: red;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
}

.low-risk {
    background-color: rgba(0,255,0,0.2);
    border: 2px solid lime;
    padding: 15px;
    border-radius: 12px;
    color: lime;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.title("Smart Scene Understanding using YOLO + VLM")

st.markdown(
    "<center>Real-time Object Detection, AI Scene Reasoning & Risk Analysis</center>",
    unsafe_allow_html=True
)

# ---------------- VLM SERVER ----------------

VLM_URL = "http://10.0.0.147:5000/analyze"

# ---------------- SIDEBAR ----------------

st.sidebar.title("Control Panel")

mode = st.sidebar.radio(
    "Choose Input Mode",
    ["Upload Image", "Webcam"]
)

st.sidebar.markdown("---")

st.sidebar.success("VLM Server Connected")

# ---------------- IMAGE MODE ----------------

if mode == "Upload Image":

    uploaded_file = st.file_uploader(
        "Upload an Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        frame = np.array(image)

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Detect objects
        detected_objects = detect_objects(frame)

        # Send to VLM
        try:

            response = requests.post(
                VLM_URL,
                json={"objects": detected_objects}
            )

            result = response.json()

            ai_response = result["scene_analysis"]

            risk_level = result["risk_level"]

        except Exception as e:

            ai_response = f"VLM Error: {e}"

            risk_level = "UNKNOWN"

        # Convert back for display
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # ---------------- UI ----------------

        col1, col2 = st.columns([2,1])

        with col1:

            st.image(
                frame_rgb,
                caption="Uploaded Image",
                use_container_width=True
            )

        with col2:

            st.subheader("Detected Objects")

            for obj in detected_objects:
                st.markdown(
                    f'<div class="object-box">{obj}</div>',
                    unsafe_allow_html=True
                )

            st.subheader("Risk Level")

            if risk_level == "HIGH":
                st.markdown(
                    '<div class="high-risk">HIGH RISK</div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    '<div class="low-risk">LOW RISK</div>',
                    unsafe_allow_html=True
                )

            st.subheader("AI Scene Analysis")

            st.markdown(
                f'<div class="ai-box">{ai_response}</div>',
                unsafe_allow_html=True
            )

# ---------------- WEBCAM MODE ----------------

elif mode == "Webcam":

    run = st.checkbox("Start Webcam")

    FRAME_WINDOW = st.image([])

    cap = cv2.VideoCapture(1)

    while run:

        ret, frame = cap.read()

        if not ret:
            st.error("Failed to access webcam")
            break

        # Detect objects
        detected_objects = detect_objects(frame)

        # Send to VLM
        try:

            response = requests.post(
                VLM_URL,
                json={"objects": detected_objects}
            )

            result = response.json()

            ai_response = result["scene_analysis"]

            risk_level = result["risk_level"]

        except Exception as e:

            ai_response = f"VLM Error: {e}"

            risk_level = "UNKNOWN"

        # Risk color
        if risk_level == "HIGH":
            color = (0, 0, 255)
        else:
            color = (0, 255, 0)

        # Overlay
        cv2.putText(
            frame,
            f"Risk: {risk_level}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            2
        )

        # Convert for display
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # ---------------- UI ----------------

        col1, col2 = st.columns([2,1])

        with col1:

            FRAME_WINDOW.image(
                frame_rgb,
                use_container_width=True
            )

        with col2:

            st.subheader("Detected Objects")

            for obj in detected_objects:
                st.markdown(
                    f'<div class="object-box">{obj}</div>',
                    unsafe_allow_html=True
                )

            st.subheader("Risk Level")

            if risk_level == "HIGH":
                st.markdown(
                    '<div class="high-risk">HIGH RISK</div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    '<div class="low-risk">LOW RISK</div>',
                    unsafe_allow_html=True
                )

            st.subheader("AI Scene Analysis")

            st.markdown(
                f'<div class="ai-box">{ai_response}</div>',
                unsafe_allow_html=True
            )

    cap.release()
