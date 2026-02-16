# AI Labor Market ELT Pipeline
**Course:** AI 620: Data Engineering for AI Systems  
**Assignment:** 1 - Building a Modern ELT Pipeline  

## Project Overview
This project implements a modular **Extract, Load, and Transform (ELT)** pipeline that aggregates data related to the **AI Labor Market**. It integrates data from three distinct sources to analyze job trends, skill demands, and salary benchmarks in the Artificial Intelligence sector.

### Thematic Domain: AI Labor Markets
* **Focus:** Job trends, skill demands, and salary evolution in AI/ML.
* **Goal:** To engineer a dataset that supports analysis of the shifting landscape of AI employment.

---

## 📂 Project Structure
```text
├── data/
│   ├── raw/                  # Raw data downloaded from APIs/Sources
│   └── processed/            # Cleaned data in CSV and JSON formats
├── src/
│   ├── __init__.py           # Makes 'src' a Python package
│   ├── extract_api.py        # Extracts news articles via NewsAPI
│   ├── extract_kaggle.py     # Downloads datasets via Kaggle API
│   ├── extract_trends.py     # Fetches search trends via Google Trends
│   └── load_data.py          # Converts raw data to standardized formats
├── .env                      # API Credentials (ensure this is Git-ignored)
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
└── run_pipeline.py           # Main orchestration script