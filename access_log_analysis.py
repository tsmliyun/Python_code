# 分析接口的调用次数
import re


def find_item(hero):
    with open('/Users/yunli/Desktop/az-api-access-2020-03-02.log', encoding='UTF-8') as f:
        data = f.read().replace('\n', '')
        name_num = re.findall(hero, data)
        print('接口 %s 出现 %s 次' % (hero, len(name_num)))

        return len(name_num)


with open('api.txt') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            name_num = find_item(n)
