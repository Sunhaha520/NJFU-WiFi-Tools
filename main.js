// 创建存储空间
var storage = storages.create("id");

// 检查是否已存储账号和密码
if (storage.get("un") == null) {
    var username = rawInput("请输入账号:");
    storage.put("un", username);
    var password = rawInput("请输入密码:");
    storage.put("pa", password);
}

// 构建请求头
var headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "10.11.2.3",
    "Origin": "http://10.11.2.3",
    "Referer": "http://10.11.2.3/a70.htm",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
};

// 构建请求数据
var data = {
    "DDDDD": storage.get("un"),  // 用户账号
    "upass": storage.get("pa"),   // 用户密码
    "R1": "0",
    "R2": "",
    "R3": "0",
    "R6": "0",
    "para": "00",
    "0MKKey": "123456",
};

var url = "http://10.11.2.3/a70.htm";

// 提示信息
console.log("请保证流量开关已经关闭");
console.log("本脚本由小阿宇创建");
console.log("欢迎访问小阿宇的网站: https://www.xiaoayu.ren");
console.log("正在进行认证绕过，你即将畅享校园网！");
console.log("有兴趣可以看看我可爱女友的小团子的博客!");
console.log("地址是: https://yynaixi.repl.co");
console.log("***********************************");
console.log("************请稍等****************");
console.log("**********************************");

// 发送POST请求
var response = http.post(url, data, headers);
var htmlContent = response.body.string();

// 提示用户网络连接成功
toast("您的网络已连接!");
