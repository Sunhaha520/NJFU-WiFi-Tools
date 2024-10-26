import os
import requests
import json
import logging
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# 设置日志配置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)

def login_to_campus(url, username, password):
    data = {
        "DDDDD": username,
        "upass": password,
        "R1": "0",
        "R2": "",
        "R3": "0",
        "R6": "0",
        "para": "00",
        "0MKKey": "123456",
    }

    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "10.11.1.3",
        "Origin": url,
        "Referer": url,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    }

    # 创建一个会话，并添加重试机制
    with requests.Session() as session:
        retry = Retry(total=5, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        try:
            response = session.post(url, data=data, headers=header)
            response.raise_for_status()  # 如果请求失败，抛出异常
            logging.info("Login successful.")
            return response.status_code, response.text
        except requests.exceptions.RequestException as e:
            logging.error(f"请求出错：{e}")
            return None, str(e)

# 主程序
if __name__ == "__main__":
    config = load_config()
    url = config['url']
    username = config['credentials']['username']
    password = config['credentials']['password']
    
    status_code, response_text = login_to_campus(url, username, password)
    print("回应代码: {}".format(status_code))
    print("响应内容: {}".format(response_text))
