# 三国中名字出现次数分析
import re


def find_item(hero):
    with open('sanguo.txt', encoding='UTF-8') as f:
        data = f.read().replace('\n', '')
        name_num = re.findall(hero, data)
        print('主角 %s 出现 %s 次' % (hero, len(name_num)))

        return len(name_num)


name_dict = {}
with open('name.txt') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            name_num = find_item(n)
            name_dict[n] = name_num

name_sorted = sorted(name_dict.items(),key=lambda item:item[1],reverse=True)

print(name_dict)

print(name_sorted)


