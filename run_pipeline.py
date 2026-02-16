# Name: Noor Ul Ain Anwar
# Student ID: 25280062

import sys
import os

# 1. Add the 'src' directory to the system path
# This tells Python: "Look inside the 'src' folder for imports too"
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(current_dir, 'src'))

# 2. Now import your modules directly
# (Note: We don't say 'from src import...', just import the file names directly
# because we added 'src' to the path above)
try:
    import extract_api
    import extract_kaggle
    import extract_trends
    import transform_analyze
except ImportError as e:
    print(f"CRITICAL ERROR: {e}")
    print("Make sure your files (extract_api.py, etc.) are inside the 'src' folder.")
    sys.exit(1)

def run():
    print("==========================================")
    print("   STARTING AI LABOR MARKET ELT PIPELINE  ")
    print("==========================================")

    # --- Step 1: NewsAPI ---
    print("\n[Step 1/3] Extracting News Data...")
    try:
        # Check if the function exists, or call the main logic
        if hasattr(extract_api, 'get_news_data'):
            extract_api.get_news_data()
        else:
            print("(!) Warning: No 'get_news_data' function found in extract_api.py")
    except Exception as e:
        print(f"✘ FAILED: {e}")

    # --- Step 2: Kaggle ---
    print("\n[Step 2/3] Extracting Kaggle Data...")
    try:
        extract_kaggle.download_ai_job_data()
    except Exception as e:
        print(f"✘ FAILED: {e}")

    # --- Step 3: Google Trends ---
    print("\n[Step 3/3] Extracting Google Trends Data...")
    try:
        extract_trends.extract_google_trends()
    except Exception as e:
        print(f"✘ FAILED: {e}")

    # --- Step 4: Transformation & Analysis (Part 2) ---
    print("\n[Step 4/4] Running Transformation & Analysis...")
    try:
        transform_analyze.run_analysis()
    except Exception as e:
        print(f"✘ Analysis FAILED: {e}")

    print("\n==========================================")
    print("   DONE                                   ")
    print("==========================================")

if __name__ == "__main__":
    run()