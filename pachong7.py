from bs4 import BeautifulSoup
import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Host": "httpbin.org",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-5e5f9a40-ce990b3ad9f29c14644f4e22"
}

# url = 'https://www.infoq.cn/'
# url = 'https://learnku.com/laravel'
url = 'https://segmentfault.com/'


# info

def craw2(url):
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)

    # news__item-info
    for title_href in soup.find_all('div',
                                    class_='news__item-info'):
        for k in title_href.find_all('h4'):
            print(k.string)


craw2(url)
