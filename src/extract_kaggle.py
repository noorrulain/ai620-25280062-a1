# Name: Noor Ul Ain Anwar
# Student ID: 25280062

import os
from pathlib import Path
from dotenv import load_dotenv
from kaggle.api.kaggle_api_extended import KaggleApi

# 1. Robustly find the .env file
# This looks for .env in the parent directory of this script (project root)
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# 2. Debugging: Print to see if it actually found the key (Don't leave this in final submission)
print(f"DEBUG: Username found? {'Yes' if os.getenv('KAGGLE_USERNAME') else 'No'}")
print(f"DEBUG: Key found? {'Yes' if os.getenv('KAGGLE_API_TOKEN') else 'No'}")

# 3. Manual Mapping
# The library ONLY checks 'KAGGLE_KEY', so we must copy your token into that variable
if os.getenv('KAGGLE_API_TOKEN'):
    os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_API_TOKEN')

def download_ai_job_data(download_path='data/raw/'):
    try:
        api = KaggleApi()
        api.authenticate()
        
        dataset_slug = 'mann14/global-ai-and-data-science-job-market-20202026'
        os.makedirs(download_path, exist_ok=True)
        
        print(f"Downloading {dataset_slug}...")
        api.dataset_download_files(dataset_slug, path=download_path, unzip=True)
        print("Download complete.")
        
    except Exception as e:
        print(f"Error: {e}")
        print("Tip: Check if your .env file is in the project root and named correctly.")

if __name__ == "__main__":
    download_ai_job_data()