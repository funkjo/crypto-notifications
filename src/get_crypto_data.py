from dotenv import load_dotenv
import pandas as pd
import requests
import os
import json

load_dotenv()

API_KEY = os.getenv('LC_API_KEY')

api_assets_uri = 'https://api.lunarcrush.com/v2?data=assets&key=' + API_KEY


def generate_query(assets: list):
    query = '&symbol='
    if len(assets) < 2:
        query = query + assets[0] + '&data_points=24&time_series_indicators=open,close,high,low'
    else:
        for asset in assets:
            if asset == assets[-1]:
                query = query + asset
            else:
                query = query + asset + ','
    query = query + '&data_points=24&time_series_indicators=open,close,high,low'

    return query


def convert_to_df(time_series):
    return None


def get_crypto_data(assets: list):
    query = generate_query(assets)
    api_call_str = api_assets_uri + query
    r = requests.get(api_call_str)

    data = json.loads(r.text)
    pct_chang_24h = data['data'][0]['percent_change_24h']
    pct_change_7d = data['data'][0]['percent_change_7d']
    time_series = data['data'][0]['timeSeries']
    df = convert_to_df(time_series)
    return None