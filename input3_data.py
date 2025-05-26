# (
#     stock_id='2330',
#     start_date='2020-01-02',
#     end_date='2020-04-12',
# )
func_stock = [
    # 提供台股，上市、上櫃、興櫃，的股票日成交資訊！
    # 資料區間：1994-10-01 ~ now
    "taiwan_stock_daily",

    # 個股PER、PBR資料表 TaiwanStockPER¶
    # 資料區間：2005-10-01 ~ now
    "taiwan_stock_per_pbr",

    # 當日沖銷交易標的及成交量值
    # 2014-01-01 ~ now
    "taiwan_stock_day_trading",

]

# (
#     index_id="TAIEX",
#     start_date='2020-04-02',
#     end_date='2020-04-12'
# )
func_index = [
    # 加權、櫃買報酬指數 TaiwanStockTotalReturnIndex¶
    # 資料區間：2003-01-01 ~ now
    "taiwan_stock_total_return_index",
]