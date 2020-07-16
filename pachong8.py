from bs4 import BeautifulSoup
import requests
import os
import shutil

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Host": "httpbin.org",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-5e5f9a40-ce990b3ad9f29c14644f4e22"
}

url = 'https://segmentfault.com/lives'

# 抓取图片
def craw3(url):
    response = requests.post(url, headers=headers)
    # print(112)
    soup = BeautifulSoup(response.text, 'lxml')

    # print(soup)

    for pic_href in soup.find_all('div', class_='rounded-top'):
        for pic in pic_href.find_all('img'):
            imgurl = pic.get('src')
            dir = os.path.abspath('./img/')
            filename = os.path.basename(imgurl)
            imgpath = os.path.join(dir, filename)
            print(imgpath)
            print('开始下载%s' % imgurl)
            download_jpg(imgurl, imgpath)


# 下载图片
def download_jpg(image_url, image_localpath):
    response = requests.get(image_url, stream=True)

    if response.status_code == 200:
        with open(image_localpath, 'wb') as f:
            response.raw.deconde_content = True
            shutil.copyfileobj(response.raw, f)

craw3(url)

# 翻页
# for i in range():
#     拼接url