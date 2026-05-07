from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

print("Loading VLM model...")

pipe = pipeline(
    "image-text-to-text",
    model="LiquidAI/LFM2.5-VL-450M",
    trust_remote_code=True
)

print("Model loaded!")

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json

    objects = data.get("objects", [])

    prompt = f"""
    Analyze the scene containing these objects:

    {objects}

    Give:
    1. A short scene description
    2. Risk level as ONLY:
       LOW or HIGH
    3. Brief reason
    """

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                }
            ]
        }
    ]

    output = pipe(text=messages)

    response_text = output[0]["generated_text"][-1]["content"]

    text_lower = response_text.lower()

    if "high" in text_lower:
        risk_level = "HIGH"
    else:
        risk_level = "LOW"

    return jsonify({
        "scene_analysis": response_text,
        "risk_level": risk_level
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)