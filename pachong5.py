import requests
import re

content = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text
#
# print(content)

#  <div class="grid-item work-thumbnail">
#  <a href="http://www.cnu.cc/works/364609" class="thumbnail" target="_blank">
#  <div class="title"> IMPETUOUS. </div>
#  <div class="author"> 快门怪咖</div>

# 正则
# <div class="grid-item work-thumbnail">
#  <a href="(.*?)" .*?title"> (.*?)</div>
# <div class="author"> 快门怪咖</div>

patten = re.compile(r' <a href="(.*?)".*?title">(.*?)</div>', re.S)
results = re.findall(patten, content)
print(results)

for result in results:
    url,name = result
    print(url,re.sub('\s','',name)) # /s匹配空白字符  utf8模式下 匹配各种制表符 换行符
