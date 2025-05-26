import os
import pandas as pd
import datetime as dt
from dotenv import load_dotenv
from FinMind.data import DataLoader
import logging
import input0_data
import input1_data
import input3_data

def logger():
    logging.basicConfig(
        filename = 'log.txt',
        level=logging.INFO,
        format = '%(asctime)s | %(levelname)s | %(message)s',
        encoding='utf-8'
    )

def login():
    load_dotenv()
    USER_NAME = os.getenv("FINMIND_USER")
    PASSWORD = os.getenv("FINMIND_PASSWORD")

    if not USER_NAME or not PASSWORD:
        raise ValueError("請確認 .env 檔案中 FINMIND_USER 和 FINMIND_PASSWORD 是否正確")

    data_loader = DataLoader()
    data_loader.login(user_id=USER_NAME, password=PASSWORD)
    return data_loader

def save_to_csv(df: pd.DataFrame, folder: str, filename: str):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    df.to_csv(path, index=False, encoding="utf-8-sig")
    logging.info("✅ 已儲存檔案： " + str(filename))
    print(f"✅ 已儲存檔案：{path}")

def take_data0(data_loader):
    now = dt.datetime.now()
    timestamp = now.strftime("%Y%m%d")

    for method_name in input0_data.func:
        try:
            method = getattr(data_loader, method_name)
            df = method()
            folder = f"db/{method_name}"
            filename = f"{method_name}_{timestamp}.csv"
            save_to_csv(df, folder, filename)
        except Exception as e:
            logging.warning("⚠️ 無法取得" + method_name + str(e))
            print(f"⚠️ 無法取得 {method_name}：{e}")

def take_data1(data_loader, input_date):
    # now = dt.datetime.now()
    # timestamp = now.strftime("%Y%m%d_%H%M")

    for method_name in input1_data.func:
        try:
            method = getattr(data_loader, method_name)
            df = method(date = input_date)
            folder = f"db/{method_name}"
            filename = f"{method_name}_{input_date}.csv"
            save_to_csv(df, folder, filename)
        except Exception as e:
            logging.warning("⚠️ 無法取得" + method_name + str(e))
            print(f"⚠️ 無法取得 {method_name}：{e}")

def take_data3(data_loader):
    now = dt.datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M")

    for method_name in input0_data.func:
        try:
            method = getattr(data_loader, method_name)
            df = method()
            folder = f"db/{method_name}"
            filename = f"{method_name}_{timestamp}.csv"
            save_to_csv(df, folder, filename)
        except Exception as e:
            logging.warning("⚠️ 無法取得" + method_name + str(e))
            print(f"⚠️ 無法取得 {method_name}：{e}")

if __name__ == "__main__":
    data_loader = login()
    logger()
    take_data0(data_loader)
    take_data1(data_loader, input_date = '2025-05-09')
    #take_data3(data_loader, input_stock = '2330', input_date = '2005-01-01')
    
