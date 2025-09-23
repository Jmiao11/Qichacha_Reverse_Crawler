import execjs
import requests
from lxml import etree
import re
from encode_url import encode_url_chinese


f = open("02_企查查_header加密逻辑.js", "r", encoding="utf-8")
js_code = f.read()
# 加载js代码
js_exec = execjs.compile(js_code)
session = requests.Session()
cookie = "QCCSESSID=4492646e8427e818c96f8a311c; qcc_did=4c746af8-ff7c-461f-8c31-d8bb3edace82; _c_WBKFRo=zJ9ulNNG082rHugxKmMCenBYiQBSfE86YweFqO4L; acw_tc=1a0c384a17569783716737256e1077afb9216c05d0b25bae68c4d4b1732fa6"

print('--------------------通过访问静态页面，获取window_pid-------------------------')
key_word = str(input("搜索关键字:"))
main_url = "https://www.qcc.com/web/search?key="
main_url = main_url + key_word
encode_main_url = encode_url_chinese(main_url)
print(" URL 转换为编码后：",encode_main_url)

main_header = {
    "cookie": cookie,
    "referer": encode_main_url,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0",
}

try:
    response = session.get(main_url, headers=main_header)
    tree = etree.HTML(response.text)
    window_pid = tree.xpath('/html/body/script[1]/text()')[0]
    window_pid = window_pid.split(";")[0]
    print("正则准备提取：", window_pid)

    result = re.search(r"window\.pid='(.*?)'", window_pid)
    window_pid = result.group(1)
    print("提取成功：", window_pid)
except Exception as e:
    print("获取window_pid失败：",e)


print('--------------------处理searchMulti_header-------------------------')

pageIndex = int(input("搜索页数（无会员两页内）："))

searchMulti_header = {
    "content-type": "application/json",
    "cookie": cookie,
    "origin": "https://www.qcc.com",
    "priority": "u=1, i",
    "referer": encode_main_url+"&p=2",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0",
    "x-requested-with": "XMLHttpRequest",
    "x-pid": window_pid
}



e = {
    "url": "/api/search/searchMulti",
    "method": "post",
    "data": {
        "searchKey": key_word,
        "pageIndex": pageIndex,
        "pageSize": 20
    },
    "headers": {
        "common": {
            "Accept": "application/json, text/plain, */*"
        },
        "delete": {},
        "get": {},
        "head": {},
        "post": {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        "put": {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        "patch": {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        "X-Requested-With": "XMLHttpRequest",
        "x-pid": window_pid
    },
    "baseURL": "https://www.qcc.com",
    "transformRequest": [None],  # 修正：Python 用 None 替代 JS 的 null
    "transformResponse": [None],  # 同上
    "timeout": 0,
    "xsrfCookieName": "XSRF-TOKEN",
    "xsrfHeaderName": "X-XSRF-TOKEN",
    "maxContentLength": -1,
    "maxBodyLength": -1,
    "transitional": {
        "silentJSONParsing": True,
        "forcedJSONParsing": True,
        "clarifyTimeoutError": False
    },
    "withCredentials": True
}
r = js_exec.call("main",e)
print(r)
searchMulti_header[r["i"]] = r["u"]
print("Multi_header已经处理完毕：",searchMulti_header)

print('--------------------发送请求-------------------------')

data = {
    "searchKey": key_word,
    "pageIndex": pageIndex,
    "pageSize": 20
}


# 发送请求时捕获详细异常
try:
    response_ = session.post(
        "https://www.qcc.com/api/search/searchMulti",
        headers=searchMulti_header,
        json=data,
        timeout=10
    )
    print("响应状态码:", response_.status_code)
    print("响应头:", response_.headers)
    print("响应内容:", response_.text)
except Exception as e:
    print("请求失败:", str(e))


