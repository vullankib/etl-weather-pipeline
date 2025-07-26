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

## Visualize Data with Streamlit

1. Install Streamlit and pandas:
   ```
   pip install streamlit pandas
   ```
2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
3. This will open a browser window where you can view and interact with your weather data.

<img src="[images/eatherDataVisualization.png](https://github.com/vullankib/etl-weather-pipeline/blob/main/images/weatherDataVisualization.png)" align="center" alt="Weather ETL Pipeline" width="600"/>

