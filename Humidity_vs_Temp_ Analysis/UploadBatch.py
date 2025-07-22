import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# === 1. Upload the batch_input.jsonl file ===
with open("batch_input.jsonl", "rb") as f:
    print("📤 Uploading file...")
    upload_response = requests.post(
        "https://api.openai.com/v1/files",
        headers={"Authorization": f"Bearer {api_key}"},
        files={"file": f},
        data={"purpose": "batch"}
    )

upload_data = upload_response.json()

if upload_response.status_code != 200:
    print("❌ File upload failed:", upload_data)
    exit()

file_id = upload_data["id"]
print(f"✅ File uploaded. File ID: {file_id}")

# === 2. Submit the batch job ===
print("🚀 Submitting batch job...")

batch_payload = {
    "input_file_id": file_id,
    "endpoint": "/v1/chat/completions",
    "completion_window": "24h"
}

batch_response = requests.post(
    "https://api.openai.com/v1/batches",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json=batch_payload
)

batch_data = batch_response.json()

if batch_response.status_code == 200:
    print("✅ Batch submitted!")
    print("📦 Batch ID:", batch_data["id"])
    print("⏳ Status:", batch_data["status"])
else:
    print("❌ Batch submission failed:")
    print(batch_data)
