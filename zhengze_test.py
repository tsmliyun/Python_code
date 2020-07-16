import re

# p = re.compile('ca*t')
# # print(p.match('a'))
# print(p.match('caaaaat'))

# 元字符
# . 匹配任意一个字符
# p = re.compile('.')
# print(p.match('b'))

# ^ 以什么开头
# p = re.compile('^d')
# print(p.match('d'))

# $ 以什么结尾
# p = re.compile('jpg$')
# print(p.match('aaajpg'))

# * 匹配前面的字符出现0次或者多次
# p = re.compile('ca*t')
# print(p.match('ct'))

# + 匹配前面的字符出现1次或者多次
# p = re.compile('c+t')
# print(p.match('ct'))

# ? 匹配前面的字符出现0次或者1次
# p = re.compile('ca?t')
# print(p.match('caat'))

# {} 匹配前面的字符出现指定的次数
# p = re.compile('ca{4,6}t')
# print(p.match('caaaaaaat'))

# [] 匹配前面的字符出现指定的字符
# p = re.compile('c[bac]t')
# print(p.match('cbt'))

# | 字符选择左边或者右边

# 转义的符号
# \d 匹配的内容是一串数字
# p = re.compile('[0-9]+')
# p = re.compile('\d+')
# print(p.match('123123123'))

# \D   反之 \d  不包含数字的
# p = re.compile('\D')
# print(p.match('123-34-544'))

# \s 匹配的是字符串 包含 a-z

# () 进行分组

# (2018)-(03)-(04)
# (03|04)


# ^$ 表示空行


# .*? 表示不使用贪婪模式
# <img  /img>
# <img  /img>


# p = re.compile('.{3}')
# print(p.match('bat'))

# p = re.compile('....-..-..')
# p = re.compile(r'(\d+)-(\d+)-(\d+)')
# print(p.match('2018-08-10').groups())
# print(p.match('aaa2018-aa08-10').groups())

# year, month, day = p.match('2018-08-10').groups()
# print(year)
# print(r'\n')
# print(p.search('aa2018-08-10bb'))

# match 匹配  search搜索 的区别

# sub 字符串替换
phone = '123-456-789 # 这是电话号码'
p2 = re.sub(r'#.*$', '', phone)
print(p2)
p3 = re.sub(r'\D','',phone)
print(p3)

# findall()