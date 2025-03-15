import requests
import os, environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, "ironfeedback/.env"))

def send_sms(phone_number, message):
    url = "https://rest.nexmo.com/sms/json"
    payload = {
        "api_key": env('VONAGE_API_KEY'),
        "api_secret": env('VONAGE_API_SECRET'),
        "to": phone_number,
        "from": env('VONAGE_SENDER_ID'),
        "text": message
    }
    response = requests.post(url, json=payload)
    data = response.json()
    
    if data["messages"][0]["status"] == "0":
        return True  # SMS sent successfully
    else:
        print("Error sending SMS:", data["messages"][0]["error-text"])
        return False
