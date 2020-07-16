from urllib import request
from urllib import parse

# url = 'http://www.baidu.com'
# response = request.urlopen(url, timeout=1)
# print(response.read().decode('utf-8'))


# response2 = request.urlopen('http://httpbin.org/get', timeout=1)
# print(response2.read())

# data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf8')
# response1 = request.urlopen('http://httpbin.org/post', data=data)
# print(response1.read().decode('utf8'))

# import urllib
# import socket
#
# try:
#     response2 = request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')

# 字典
# 模拟headers
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Host": "httpbin.org",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-5e5f9a40-ce990b3ad9f29c14644f4e22"
}

dict = {
    'name': 'value'
}
url = 'http://httpbin.org/post'
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
