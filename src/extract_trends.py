import pandas as pd
from pytrends.request import TrendReq
import os

# Configuration: Keywords relevant to your "AI Labor Markets" theme
KEYWORDS = ["AI Jobs", "Machine Learning", "Data Science", "Generative AI"]

def extract_google_trends():
    """
    Extracts time-series search data from Google Trends.
    """
    print("Connecting to Google Trends...")
    
    # Initialize the connection
    pytrends = TrendReq(hl='en-US', tz=360)
    
    # --- FIX STARTS HERE ---
    try:
        # Build the payload
        pytrends.build_payload(KEYWORDS, cat=0, timeframe='today 5-y', geo='', gprop='')
        
        # Get 'Interest Over Time'
        data = pytrends.interest_over_time()
        
        if data.empty:
            print("No data found for the specified keywords.")
            return

        # Drop the 'isPartial' column which Google includes by default
        if 'isPartial' in data.columns:
            data = data.drop(columns=['isPartial'])

        # Ensure the raw directory exists
        save_path = 'data/raw/google_trends.csv'
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # Save to CSV
        data.to_csv(save_path)
        print(f"Successfully saved trends data to {save_path}")

    except Exception as e:
        # This is the block you were missing!
        print(f"An error occurred: {e}")
        if "429" in str(e):
            print("(!) Rate Limit Exceeded: Google is blocking the request. Try again later.")
    # --- FIX ENDS HERE ---

if __name__ == "__main__":
    extract_google_trends()