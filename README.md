# Name: Noor Ul Ain Anwar
# Student ID: 25280062

## Project Overview
This project implements a modular Extract, Load, and Transform (ELT) pipeline that aggregates data related to the AI Labor Market. It integrates data from three distinct sources to analyze job trends, skill demands, and salary benchmarks in the Artificial Intelligence sector.

---

## How to Run the Pipeline
To execute the full Extraction, Loading, and Transformation process, run the main orchestration script (run_pipeline.py) from the project root:

## Pipeline Workflow:
Extraction (Step 1-3): Connects to NewsAPI, Kaggle, and Google Trends to download raw data into data/raw/.

Loading (Step 4): Standardizes the raw data into CSV and JSON formats in data/processed/.

Transformation & Analysis (Step 5): Cleans missing values and duplicates, saves the final "Gold" datasets to data/cleaned/ and generates analytical charts (e.g., Salary vs. Experience) in the visualizations/ folder.

## Project Structure
```text
├── data/
│   ├── raw/                  # Raw data downloaded from APIs/Sources
│   ├── processed/            # Cleaned data in CSV and JSON formats
|   └── cleaned/              # Final cleaned data for analysis
├── visualizations/           # Generated plots and charts (PNG)
├── src/
│   ├── __init__.py           # Makes 'src' a Python package
│   ├── extract_api.py        # Extracts news articles via NewsAPI
│   ├── extract_kaggle.py     # Downloads datasets via Kaggle API
│   ├── extract_trends.py     # Fetches search trends via Google Trends
│   ├── load_data.py          # Converts raw data to standardized formats
|   └── transform_analyze.py  # Cleans data and generates visualizations
├── .env                      # API Credentials (ensure this is Git-ignored)
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── run_pipeline.py           # Main orchestration script
├── Part1_Part2_Questions.pdf # Assignment Questions (open using vscode-pdf extension)
└── Assignment_Report.pdf     # Brief summary of the assignment (open using vscode-pdf extension)