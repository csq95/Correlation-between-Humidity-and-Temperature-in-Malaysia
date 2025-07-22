# Correlation-between-Humidity-and-Temperature-in-Malaysia
A simple pipeline to aggregate daily humidity and temperature data from all 13 Malaysian states (Jan–Jun 2025), compute monthly averages of humidity and temperature across all states in Malaysia using the OpenAI API.

## 🚀 Features

- **Load** a batch JSON file (`input.json`) of state‑level daily weather records.
- **Compute** monthly national averages for humidity and temperature.

## 🔧 Prerequisites

- Python 3.8 or higher  
- An OpenAI API key
  
## 📦 Installation
  1.  Clone the repo
  2.  Change your API Key
  3.  Run GenerateBatch to create batch_input.json 
  4.  Run UploadBatch to upload files to the Batch API for processing, you will get your Batch         ID after running this.
  5.  In the meantime, you can run CheckStatusOfBatch to check on your request.
  6.  Download the output file, batch_output.jsonl here and run PrintOutput to extract the             output content only.
  7.  You can find the data/summary I have sorted in my Excel file.

##  Sources from: https://www.visualcrossing.com/
