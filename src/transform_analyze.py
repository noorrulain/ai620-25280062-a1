import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import glob

# Configuration
PROCESSED_DIR = 'data/processed'
CLEANED_DIR = 'data/cleaned'
VIS_DIR = 'visualizations'

def setup_directories():
    os.makedirs(CLEANED_DIR, exist_ok=True)
    os.makedirs(VIS_DIR, exist_ok=True)

def assess_quality(df, name):
    """
    (a) Data Quality Assessment: Reports missing values and duplicates.
    """
    print(f"\n--- Quality Assessment: {name} ---")
    print(f"Total Rows: {len(df)}")
    
    # Check missing values
    missing = df.isnull().sum()
    print(f"Missing Values:\n{missing[missing > 0]}")
    
    # Check duplicates
    dupes = df.duplicated().sum()
    print(f"Duplicate Rows: {dupes}")
    
    return missing, dupes

def clean_kaggle_jobs(df):
    """
    (b) Transformation and Cleaning for Job Market Data
    """
    print("\n[Cleaning] Processing Jobs Dataset...")
    
    # 1. Handle Duplicates
    initial_rows = len(df)
    df = df.drop_duplicates()
    print(f"Removed {initial_rows - len(df)} duplicate rows.")
    
    # 2. Handle Missing Values
    # Assumption: If 'salary_in_usd' is missing, the row is not useful for salary analysis.
    # However, for this specific dataset, we might impute or drop. Let's drop for strict accuracy.
    if 'salary_in_usd' in df.columns:
        df = df.dropna(subset=['salary_in_usd'])
    
    # 3. Standardize Formats
    # Convert 'experience_level' to categorical if it exists
    if 'experience_level' in df.columns:
        df['experience_level'] = df['experience_level'].astype('category')
        
    return df

def clean_google_trends(df):
    """
    (b) Transformation and Cleaning for Trends Data
    """
    print("\n[Cleaning] Processing Google Trends Dataset...")
    
    # 1. Standardize Dates
    # The index might be the date, or it might be a column 'date'
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    else:
        # Sometimes pytrends puts the date in the index. Reset it to a column.
        df.reset_index(inplace=True)
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'])
            
    # 2. Handle Missing Values
    # For time-series, forward fill (ffill) is often better than dropping
    df = df.ffill()
    
    return df

def create_visualizations(df_jobs, df_trends):
    """
    Exploratory Analysis and Visualization
    """
    print("\n[Analysis] Generating Visualizations...")
    sns.set_theme(style="whitegrid")

    # --- Vis 1: Temporal Analysis (Time-Series) ---
    # Plotting search interest over time
    plt.figure(figsize=(12, 6))
    # Melt the dataframe to plot multiple keywords on one chart
    if 'date' in df_trends.columns:
        trends_melted = df_trends.melt(id_vars=['date'], var_name='Keyword', value_name='Search Interest')
        sns.lineplot(data=trends_melted, x='date', y='Search Interest', hue='Keyword')
        plt.title('Search Interest for AI Terms Over Time (2020-2025)')
        plt.xlabel('Date')
        plt.ylabel('Interest Level (0-100)')
        plt.savefig(f"{VIS_DIR}/1_temporal_trends.png")
        plt.close()
        print(f"✔ Saved: {VIS_DIR}/1_temporal_trends.png")

    # --- Vis 2: Categorical Analysis (Bar Chart) ---
    # Top 10 Job Titles by frequency
    if 'job_title' in df_jobs.columns:
        plt.figure(figsize=(10, 8))
        top_jobs = df_jobs['job_title'].value_counts().nlargest(10).index
        sns.countplot(data=df_jobs[df_jobs['job_title'].isin(top_jobs)], y='job_title', order=top_jobs, palette='viridis')
        plt.title('Top 10 Most Common AI Job Titles')
        plt.xlabel('Number of Postings')
        plt.savefig(f"{VIS_DIR}/2_categorical_jobs.png")
        plt.close()
        print(f"✔ Saved: {VIS_DIR}/2_categorical_jobs.png")

    # --- Vis 3: Correlation/Relationship (Box Plot) ---
    # Salary Distribution by Experience Level
    if 'salary_in_usd' in df_jobs.columns and 'experience_level' in df_jobs.columns:
        plt.figure(figsize=(10, 6))
        # Sort order: Entry-level (EN), Mid (MI), Senior (SE), Executive (EX)
        order = ['EN', 'MI', 'SE', 'EX'] 
        # Filter mostly for these standard codes if they exist
        filtered_jobs = df_jobs[df_jobs['experience_level'].isin(order)]
        
        sns.boxplot(data=filtered_jobs, x='experience_level', y='salary_in_usd', order=order)
        plt.title('Salary Distribution by Experience Level')
        plt.ylabel('Salary (USD)')
        plt.xlabel('Experience Level')
        plt.savefig(f"{VIS_DIR}/3_relationship_salary.png")
        plt.close()
        print(f"✔ Saved: {VIS_DIR}/3_relationship_salary.png")

def run_analysis():
    setup_directories()
    
    # 1. Load Data (processed CSVs)
    # Find the Kaggle job CSV dynamically
    job_files = glob.glob(f"{PROCESSED_DIR}/*job*processed.csv")
    trends_file = f"{PROCESSED_DIR}/trends_processed.csv"
    
    if not job_files or not os.path.exists(trends_file):
        print("CRITICAL ERROR: Processed data not found. Run Part 1 first.")
        return

    df_jobs = pd.read_csv(job_files[0])
    df_trends = pd.read_csv(trends_file)

    # 2. Quality Assessment
    assess_quality(df_jobs, "AI Jobs Dataset")
    assess_quality(df_trends, "Google Trends Dataset")

    # 3. Cleaning & Transformation
    df_jobs_clean = clean_kaggle_jobs(df_jobs)
    df_trends_clean = clean_google_trends(df_trends)

    # 4. Save Cleaned Data
    df_jobs_clean.to_csv(f"{CLEANED_DIR}/jobs_cleaned.csv", index=False)
    df_trends_clean.to_csv(f"{CLEANED_DIR}/trends_cleaned.csv", index=False)
    print(f"\n✔ Cleaned datasets saved to {CLEANED_DIR}/")

    # 5. Visualization
    create_visualizations(df_jobs_clean, df_trends_clean)

if __name__ == "__main__":
    run_analysis()