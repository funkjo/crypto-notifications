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
    # print(query)
    return query


def get_crypto_data(assets: list):
    query = generate_query(assets)
    api_call_str = api_assets_uri + query
    r = requests.get(api_call_str)
    data = json.loads(r.text)

    return_dict = {

    }

    for asset in data['data']:
        time_series = asset['timeSeries']
        now = time_series[-1]['close']
        one_hr_ago = time_series[-2]['close']
        pct_change_1h = (now - one_hr_ago) / now * 100
        return_dict[asset['symbol']] = {
            'price': asset['price'],
            'pct_change_24h': asset['percent_change_24h'],
            'pct_change_7d': asset['percent_change_7d'],
            'pct_change_1h': pct_change_1h,
            'open': one_hr_ago
        }
    return return_dict