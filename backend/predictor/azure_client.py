import os
import requests

class AzureMLClient:
    def __init__(self):
        self.endpoint = os.getenv("AZURE_ML_ENDPOINT")
        self.key = os.getenv("AZURE_ML_KEY")
        if not self.endpoint or not self.key:
            raise RuntimeError("AZURE_ML_ENDPOINT / AZURE_ML_KEY nisu postavljeni u .env")

    def predict(self, row: dict) -> str:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.key}",
        }
        payload = {"data": [row]}

        r = requests.post(self.endpoint, json=payload, headers=headers, timeout=30)
        r.raise_for_status()
        data = r.json()

        # očekujemo {"predictions": ["p"]} ili ["e"]
        pred = data["predictions"][0]
        return pred
