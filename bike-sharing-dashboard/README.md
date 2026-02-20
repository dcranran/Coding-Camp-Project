# Interactive Dashboard for Analyzing Bike Sharing Demand Trends

## Description
This project develops an **interactive dashboard** to analyze **bike sharing demand patterns** over time. The analysis focuses on understanding how weather conditions, seasonal variations, and temporal factors influence rental demand. The dashboard enables exploration of peak and low-demand periods to support data-driven operational decisions.

## Dataset
The dataset contains historical bike rental records, including features such as date, season, weather conditions, temperature, humidity, and rental counts. It can be downloaded from [Kaggle: Bike Sharing Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset).

## Project Objectives
1. Analyze the influence of weather and seasonal factors on bike rental demand.
2. Identify time periods with the highest and lowest rental activity.
3. Build an interactive dashboard to visualize trends and support decision making.

## Setup Environment - Anaconda
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup environment - Shell/Terminal
```bash
mkdir bike_data_project
cd bike_data_project
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run streamlit app
```bash
streamlit run dashboard.py
```
