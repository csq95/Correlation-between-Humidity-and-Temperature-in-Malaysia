import os
import json
import re
import textwrap

input_dir   = "input_data"   # ← your flat folder
output_file = "batch_input.jsonl"
max_chars   = 10000

def clean_filename(name):
    # safe for custom_id
    return re.sub(r"[^\w\-_.]", "_", name)

with open(output_file, "w", encoding="utf-8") as out:
    for i, filename in enumerate(os.listdir(input_dir), start=1):
        # skip hidden/system files
        if filename.startswith("."):
            continue

        name, ext = os.path.splitext(filename)   # e.g. "johor_april", ".txt"
        ext = ext.lower()
        if ext not in (".txt", ".json"):
            continue

        # parse state/month
        try:
            state, month = name.rsplit("_", 1)
        except ValueError:
            print(f"⚠️  couldn’t split {filename!r}, skipping")
            continue

        file_path = os.path.join(input_dir, filename)

        # read content
        if ext == ".json":
            with open(file_path, encoding="utf-8") as f:
                data = json.load(f)
            content = data.get("content", json.dumps(data, ensure_ascii=False))
        else:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

        content = content[:max_chars]

        # your prompt
        prompt = textwrap.dedent(f"""
    You are a data assistant. I will give you a JSON array of objects, each representing one Malaysian state’s daily weather . Each object has:
    state: the state name (string),
    days: an array of daily entries, each with:
      - datetime (YYYY‑MM‑DD)
      - humidity (float, %)
      - temp (float, °C)

    Your tasks:
    compute the average humidity across and the average temperature.
    Return only a JSON object with two keys:
    monthly: an array of {{ "state": "...", "month": "...", "avg_humidity": <float>, "avg_temperature": <float> }} objects


    {content}
    """)

        # custom_id includes state+month+index
        cid = clean_filename(f"{state}_{month}_{i}")

        batch_payload = {
            "custom_id": cid,
            "method":    "POST",
            "url":       "/v1/chat/completions",
            "body": {
                "model":      "gpt-4o-mini",
                "messages":   [{"role": "user", "content": prompt}],
                "max_tokens": 3000
            }
        }

        out.write(json.dumps(batch_payload, ensure_ascii=False) + "\n")

print("✅ batch_input.jsonl created successfully.")
