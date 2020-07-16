# 爬虫demo2 妹子图
import requests
from lxml import etree
import os

name = 0

# 模拟header
def header(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Referer': url
    }
    return header


def get_img(url):
    global name
    name += 1
    img_name = '{}.jpg'.format(name)
    img = requests.get(url, headers=header(url)).content
    with open(img_name, 'wb') as save_img:
        save_img.write(img)


def get_url(url):
    html = requests.get(url, headers=header(url)).text
    etree_html = etree.HTML(html)
    img_url = etree_html.xpath('//div[@class="main-image"]/p/a/img/@src')
    return img_url


def get_mainpic_url(url):
    html = requests.get(url, headers=header(url)).text
    etree_html = etree.HTML(html)
    page_url = etree_html.xpath('//div[@class="pagenavi"]/a/@href')
    return page_url


def get_subset(url):
    html = requests.get(url, headers=header(url)).text
    etree_html = etree.HTML(html)
    page_url = etree_html.xpath('//div[@class="postlist"]/ul[@id="pins"]/li/a/@href')
    return page_url


def main():
    number = 0
    url = 'https://www.mzitu.com'
    addrlist_main = get_subset(url)  # 首页的子页 url
    n = 0
    original_folder = "/Users/yunli/pic"
    maxnumber = int(input("你想爬取多少图册:"))
    for subaddr in addrlist_main:
        os.chdir(original_folder)  # 初始文件夹
        if n < maxnumber:
            n += 1
            folder_name = "第 {} 个图册".format(n)  # 创建子文件夹
            exist = os.path.exists(folder_name)
            if exist == True:
                os.chdir(folder_name)
            else:
                os.mkdir(folder_name)
                os.chdir(folder_name)
            pagelist_sub = get_mainpic_url(subaddr)  # 子页里获取后面几页的 url??
            for page in pagelist_sub:
                if page != "/hot/":
                    img_list = get_url(page)  # 获取子集中的主图片
                    for img in img_list:
                        get_img(img)  # 下载图片
        else:
            exit()


main()
