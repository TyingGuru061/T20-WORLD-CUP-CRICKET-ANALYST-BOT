import requests
import pandas as pd

POINTS_URL = "https://raw.githubusercontent.com/your-dummy-source/t20-points-table/main/points.json"

def fetch_points_table():
    """
    Replace URL later with live source.
    For now structure-ready.
    """
    response = requests.get(POINTS_URL)
    data = response.json()
    return pd.DataFrame(data)

def fetch_latest_match():
    """
    Using Streamlit cricket widget for real match.
    """
    return "latest"
