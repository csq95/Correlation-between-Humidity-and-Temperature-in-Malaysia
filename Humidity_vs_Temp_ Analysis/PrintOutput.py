import json

# Load data from the input JSON Lines file
input_file = "batch_output.jsonl"
output_file = "monthly_data.json"
all_records = []

with open(input_file, 'r') as f:
    for line in f:
        # Parse each line as JSON
        entry = json.loads(line)
        
        # Skip failed responses (non-200 status or errors)
        if entry.get("error") or entry["response"]["status_code"] != 200:
            continue
        
        # Extract the content string
        content_str = entry["response"]["body"]["choices"][0]["message"]["content"]
        
        # Remove markdown code block delimiters (```json and ```)
        json_str = content_str.replace('```json', '').replace('```', '').strip()
        
        # Parse the inner JSON and extract "monthly" records
        try:
            data = json.loads(json_str)
            all_records.extend(data["monthly"])  # Combine records
        except json.JSONDecodeError:
            print(f"Failed to parse JSON for: {entry['id']}")
            continue

# Save all records to a new JSON file
with open(output_file, 'w') as outfile:
    json.dump(all_records, outfile, indent=2)

print(f"Success! Extracted {len(all_records)} records to {output_file}.")