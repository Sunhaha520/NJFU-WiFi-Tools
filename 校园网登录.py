import requests

url = "http://10.11.1.3/a70.htm"

data = {
    "DDDDD": "w.......", # 填写自己的校园网账号
    "upass": "********", #填写自己的密码
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
    "Content-Length": "160",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "10.11.1.3",
    "Origin": "http://10.11.1.3",
    "Referer": "http://10.11.1.3/a70.htm",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}

response = requests.post(url, data, headers=header).status_code

print("回应代码{}".format(response))
input("Press <enter>")
