# coin catcher (Joe from Idaho)

import pandas as pd
import time
import schedule
import threading
from get_crypto_data import get_crypto_data
from emailer import Emailer

assets = ['ADA', 'BTC']


def send_alert(symbol, pct_change, _type, _open, close):
    emailer = Emailer()
    emailer.send_email(symbol, _open, close, pct_change, _type)


def get_time_series():
    data = get_crypto_data(assets)
    for key in data:
        if abs(data[key]['pct_change_1h']) > 5:
            send_alert(key, data[key]['pct_change_1h'], 'hourly', data[key]['open'], data[key]['price'])
    print(data)


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

# schedule.every(1).seconds.do(run_threaded, get_time_series)
# # schedule.every().hour.do(run_threaded, get_time_series)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

get_time_series()







