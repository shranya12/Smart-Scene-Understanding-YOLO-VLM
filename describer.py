import requests


class SceneDescriber:

    def __init__(self):

        self.url = "http://10.0.0.147:5000/analyze"

    def analyze_scene(self, objects):

        try:

            data = {
                "objects": objects
            }

            response = requests.post(
                self.url,
                json=data
            )

            result = response.json()

            description = result["scene_analysis"]

            level = result["risk_level"]

            risk = description

            return description, risk, level

        except Exception as e:

            return (
                "VLM connection failed.",
                str(e),
                "UNKNOWN"
            )
