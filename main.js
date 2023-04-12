var id=storages.create("id")
if(id.get("un")==null){
    var un=rawInput("请输入账号:")
    id.put("un",un)
    var pa=rawInput("请输入密码:")
    id.put("pa",pa)
   // var ur=rawInput("请输入认证页面ip:")
    //id.put("ur",ur)
    }

var headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "160",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "10.11.1.3",
    "Origin": "http://10.11.2.3",
    "Referer": "http://10.11.2.3/a70.htm",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
}

var data = { 
     "DDDDD": id.get("un"),
     "upass": id.get("pa"), 
     "R1": "0", 
     "R2": "", 
     "R3": "0", 
     "R6": "0", 
     "para": "00", 
     "0MKKey": "123456", 
     }

                                                                                                                                                                               
var url = "http://10.11.2.3/a70.htm";
console.log("请保证流量开关已经关闭")
console.log("本脚本由小阿宇创建")
console.log("欢迎访问小阿宇的网站:https://www.xiaoayu.ren")
console.log("正在进行认证绕过，你即将畅享校园网！")
console.log("有兴趣可以看看我可爱女友的小团子的博客!")
console.log("地址是:https://yynaixi.repl.co")
console.log("***********************************")
console.log("************请稍等****************")
console.log("**********************************")

var res = http.post(url,data,headers)
var html = res.body.string();
toast("您的网络已连接!")
