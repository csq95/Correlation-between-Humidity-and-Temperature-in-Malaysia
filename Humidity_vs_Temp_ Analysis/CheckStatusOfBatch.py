import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Replace with your actual batch ID
batch_id = "batch_687e458fc7308190bde130b0b4016817"

url = f"https://api.openai.com/v1/batches/{batch_id}"

response = requests.get(
    url,
    headers={"Authorization": f"Bearer {api_key}"}
)

print("📦 Batch Status:", response.status_code)
print(response.json())
