import logging

# 設定最基本的輸出格式（只要寫一次）
logging.basicConfig(
    filename = 'log.txt',
    level=logging.INFO,
    format = '%(asctime)s | %(levelname)s | %(message)s',
    encoding='utf-8'
)

# 開始寫 log
logging.info("這是 info 等級，會印出來")
logging.debug("這是 debug 等級，預設不會印出來")
logging.warning("這是警告！")
logging.error("這是錯誤訊息")
