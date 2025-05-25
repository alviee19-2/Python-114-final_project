import os
import pandas as pd
import datetime as dt
from dotenv import load_dotenv
from FinMind.data import DataLoader
import logging

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
    print(f"✅ 已儲存檔案：{path}")

def write_all_data(data_loader):
    now = dt.datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M")

    data_type = [
        "taiwan_stock_info",
        "taiwan_stock_info_with_warrant",
        "taiwan_securities_trader_info",
        "taiwan_stock_daily",
        "taiwan_stock_daily_adj",
        "taiwan_stock_tick",
        "taiwan_stock_per_pbr",
        "taiwan_stock_book_and_trade",
        "tse",
        "taiwan_stock_day_trading",
        "taiwan_stock_government_bank_buy_sell",
        "taiwan_stock_margin_purchase_short_sale",
        "taiwan_stock_margin_purchase_short_sale_total",
        "taiwan_stock_institutional_investors",
        "taiwan_stock_institutional_investors_total",
        "taiwan_stock_shareholding",
        "taiwan_stock_holding_shares_per",
        "taiwan_stock_securities_lending",
        "taiwan_daily_short_sale_balances",
        "taiwan_stock_cash_flows_statement",
        "taiwan_stock_financial_statement",
        "taiwan_stock_balance_sheet",
        "taiwan_stock_dividend",
        "taiwan_stock_dividend_result",
        "taiwan_stock_month_revenue",
        "taiwan_stock_market_value_weight",
        "taiwan_futopt_tick_info",
        "taiwan_futopt_tick_realtime",
        "taiwan_futopt_daily_info",
        "taiwan_futures_daily",
        "taiwan_option_daily",
        "taiwan_futures_open_interest_large_traders",
        "taiwan_option_open_interest_large_traders",
        "taiwan_futures_tick",
        "taiwan_option_tick",
        "taiwan_futures_institutional_investors",
        "taiwan_option_institutional_investors",
        "taiwan_futures_institutional_investors_after_hours",
        "taiwan_option_institutional_investors_after_hours",
        "taiwan_futures_dealer_trading_volume_daily",
        "taiwan_option_dealer_trading_volume_daily",
        "taiwan_stock_news",
        "taiwan_stock_total_return_index",
        "taiwan_stock_capital_reduction_reference_price",
        "taiwan_stock_market_value",
        "taiwan_stock_10year",
        "taiwan_stock_weekly",
        "taiwan_stock_monthly",
        "taiwan_stock_bar",
        "taiwan_stock_kbar",
        "taiwan_stock_delisting",
        "taiwan_total_exchange_margin_maintenance",
        "us_stock_info",
        "us_stock_price",
        "taiwan_stock_tick_snapshot",
        "taiwan_futures_snapshot",
        "taiwan_options_snapshot",
        "taiwan_stock_convertible_bond_info",
        "taiwan_stock_convertible_bond_daily",
        "taiwan_stock_convertible_bond_institutional_investors",
        "taiwan_stock_convertible_bond_daily_overview",
        "taiwan_stock_margin_short_sale_suspension",
        "taiwan_stock_trading_daily_report",
        "taiwan_stock_trading_daily_report_secid_agg",
        "taiwan_business_indicator",
        "taiwan_stock_disposition_securities_period",
        "taiwan_stock_industry_chain",
        "cnn_fear_greed_index",
        "taiwan_stock_every5seconds_index"
    ]

    for method_name in data_type:
        try:
            method = getattr(data_loader, method_name)
            df = method()
            folder = f"db/{method_name}"
            filename = f"{method_name}_{timestamp}.csv"
            save_to_csv(df, folder, filename)
        except Exception as e:
            print(f"⚠️ 無法取得 {method_name}：{e}")

if __name__ == "__main__":
    data_loader = login()
    write_all_data(data_loader)
