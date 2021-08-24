# coin catcher (Joe from Idaho)

import pandas as pd
import time
import schedule
import threading
from get_crypto_data import get_crypto_data

assets = ['ADA']

def get_time_series():
    data = get_crypto_data(assets)
    # print(data)

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

# schedule.every(1).seconds.do(run_threaded, get_time_series)
# # schedule.every().hour.do(run_threaded, get_time_series)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

get_time_series()







