import numpy as np
import pandas as pd
from datetime import date

# 讀CSV，parse_dates會把date欄位轉成日期格式

def compute():
    today = str(date.today()).replace("-", "")
    # print(today)

    filepath = "taiwan_stock_total_return_index"
    df = pd.read_csv('db/' + filepath + '/' + filepath + '_' + today + '.csv')

    # 排序資料，確保日期從小到大
    df = df.sort_values('date').to_numpy()

    #compute
    index = df[:, 0]
    last = index[-1]
    avg = index.sum() / 5
    # print(index)
    # print(avg)
    # print(last)

    #checking
    if(last - avg > 0):
        print("今日比五日大!")
        print("今日: ", last, ' ', "五日平均: ", avg)
    else:
        print("一般般")