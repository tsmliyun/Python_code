# coding:utf-8
# 下载豆瓣爱情的电影封面
import requests
import json


# 下载图片
def download(url, title):
    dir = './img/' + title + '.jpg'
    try:
        pic = requests.get(url)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        print(title)
    except requests.exceptions.ConnectionError:
        print('图片无法下载')


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Host": "httpbin.org",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-5e5f9a40-ce990b3ad9f29c14644f4e22"
}

for num in range(0, 20, 20):
    # 构造url，翻页变换参数为start=, tag=电影, gender=爱情, 改变start=后面的数字，可以爬取不同的页
    url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=' \
          + str(num) + '&genres=%E7%88%B1%E6%83%85'

    html = requests.get(url, headers=headers).text

    print(html)

    # 转为json格式
    res = json.loads(html, encoding='utf-8')
    for result in res['data']:
        cover = result['cover']
        title = result['title']
        download(cover, title)
