import requests

url = "http://10.0.0.147:5000/analyze"

data = {
    "objects": ["person", "car", "crosswalk"]
}

response = requests.post(url, json=data)

print("\nAI RESPONSE:\n")

print(response.json()["scene_analysis"])
