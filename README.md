# Smart Scene Understanding using YOLO + VLM

## Project Overview

This project combines YOLOv8 object detection with a Vision Language Model (VLM) for real-time smart scene understanding and AI-based risk analysis.

The system detects objects using YOLOv8 on NVIDIA Jetson and performs contextual scene reasoning using a lightweight Vision Language Model running on a local laptop server.

The project provides:
- Real-time webcam detection
- Upload image analysis
- AI-generated scene descriptions
- LOW/HIGH risk analysis
- Streamlit-based futuristic UI
- Distributed AI architecture using Flask API communication

---

## Technologies Used

- Python
- YOLOv8
- OpenCV
- Streamlit
- Flask
- Hugging Face Transformers
- Vision Language Models (VLM)
- NVIDIA Jetson

---

## System Architecture

### Jetson Device
- Webcam Input
- YOLOv8 Object Detection
- Streamlit User Interface
- API Communication

### Local Laptop Server
- Vision Language Model (VLM)
- Scene Reasoning
- Risk Analysis
- Flask API Backend

---

## Features

- Real-time object detection
- AI scene understanding
- LOW/HIGH risk classification
- Upload image mode
- Webcam live analysis
- Natural language reasoning
- Cyberpunk-inspired UI dashboard

---

## Example Outputs

### LOW RISK
- Person using laptop
- Classroom scenes
- Indoor workspace

### HIGH RISK
- Pedestrian near traffic
- Road crossing scenarios
- Traffic-related scenes

---

## How to Run

### Start VLM Server (Laptop)

```bash
python server.py
```

### Start Streamlit UI (Jetson)

```bash
streamlit run app.py
```

---

## Future Improvements

- Full image-based VLM reasoning
- Improved risk classification
- Higher FPS optimization
- Custom-trained safety datasets
- Voice-based alerts

---

## Project Outcome

This project demonstrates a real-time multimodal AI system integrating edge AI, computer vision, Vision Language Models, and intelligent scene-level reasoning for contextual risk analysis.
