# ETL Weather Pipeline

This project fetches daily weather data from OpenWeatherMap API, cleans and normalizes it, and stores it in a local SQLite database.

## Structure
- `data/`: Raw and processed data
- `src/`: ETL scripts
- `etl.py`: Main orchestration script

## Setup
1. Add your OpenWeatherMap API key to `.env`.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the pipeline:
   ```
   python etl.py
   ```
