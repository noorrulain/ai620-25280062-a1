# Name: Noor Ul Ain Anwar
# Student ID: 25280062

import pandas as pd
import json
import os
import glob

# Define paths
RAW_DIR = 'data/raw'
PROCESSED_DIR = 'data/processed'

def load_and_process():
    """
    Reads raw data from data/raw/, converts it to CSV/JSON,
    and saves it to data/processed/.
    """
    print(f"Checking {RAW_DIR} for files...")
    
    # Ensure processed directory exists
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    # ---------------------------
    # 1. Process Google Trends (CSV -> CSV + JSON)
    # ---------------------------
    trends_file = os.path.join(RAW_DIR, 'google_trends.csv')
    if os.path.exists(trends_file):
        try:
            df = pd.read_csv(trends_file)
            
            # Save as Processed CSV
            df.to_csv(os.path.join(PROCESSED_DIR, 'trends_processed.csv'), index=False)
            
            # Save as Processed JSON
            df.to_json(os.path.join(PROCESSED_DIR, 'trends_processed.json'), orient='records', indent=4)
            
            print(f"✔ Processed Google Trends data saved to {PROCESSED_DIR}")
        except Exception as e:
            print(f"✘ Error processing trends: {e}")

    # ---------------------------
    # 2. Process Kaggle Data (CSV -> CSV + JSON)
    # ---------------------------
    # Kaggle downloads often come with unpredictable filenames, so we grab any CSV that isn't the trends file
    csv_files = glob.glob(os.path.join(RAW_DIR, "*.csv"))
    for file in csv_files:
        if "google_trends" not in file:
            try:
                df = pd.read_csv(file)
                filename = os.path.basename(file).replace('.csv', '')
                
                # Save as Processed CSV
                df.to_csv(os.path.join(PROCESSED_DIR, f'{filename}_processed.csv'), index=False)
                
                # Save as Processed JSON
                df.to_json(os.path.join(PROCESSED_DIR, f'{filename}_processed.json'), orient='records', indent=4)
                
                print(f"✔ Processed Kaggle data ({filename}) saved to {PROCESSED_DIR}")
            except Exception as e:
                print(f"✘ Error processing {file}: {e}")

if __name__ == "__main__":
    load_and_process()