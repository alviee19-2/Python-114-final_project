import os
import pandas as pd
import datetime as dt
from dotenv import load_dotenv
from FinMind.data import DataLoader

#login
load_dotenv()

#API_TOKEN = os.getenv("FINMIND_TOKEN")
USER_NAME = os.getenv("FINMIND_USER")
PASSWORD = os.getenv("FINMIND_PASSWORD")

data_loader = DataLoader()
data_loader.login(user_id= USER_NAME,password= PASSWORD)

df = data_loader.taiwan_stock_info()

now = dt.datetime.now()
timestamp = now.strftime("%Y%m%d_%H%M")

filepath = 'db/stockinfo/'
filename = 'stockinfo' + timestamp + '.csv'
df.to_csv(filepath + filename, index = False)

