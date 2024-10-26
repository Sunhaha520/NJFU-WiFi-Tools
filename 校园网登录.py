import requests

url = "http://10.11.1.3/a70.htm"

data = {
    "DDDDD": "w.......",  # 填写自己的校园网账号
    "upass": "********",  # 填写自己的密码
    "R1": "0",
    "R2": "",
    "R3": "0",
    "R6": "0",
    "para": "00",
    "0MKKey": "123456",
}

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "10.11.1.3",
    "Origin": "http://10.11.1.3",
    "Referer": "http://10.11.1.3/a70.htm",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}

try:
    response = requests.post(url, data=data, headers=header)
    response.raise_for_status()  # 如果请求返回错误，抛出异常
    print("回应代码: {}".format(response.status_code))
    print("响应内容: {}".format(response.text))  # 输出服务器响应的内容
except requests.exceptions.RequestException as e:
    print(f"请求出错：{e}")

input("Press <enter>")
