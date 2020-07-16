from bs4 import BeautifulSoup

html_doc = ''
soup = BeautifulSoup(html_doc, 'lxml')

print(soup.prettify())

# 找到title标签
print(soup.title)

# 找到标签里面的内容
print(soup.title.string)

print(soup.p)

print(soup.p['class'])

print(soup.a)

print(soup.find_all('a'))

print(soup.find(id="link3"))

for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.get_text())

