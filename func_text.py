# print('abc')
#
# print('abc',end='\n\n')
# print('bcd')


# def func(a, b=2, c=3):
#     print('a= %s' % a)
#     print('b= %s' % b)
#     print('c= %s' % c)
#
#
# func(1,c=3,b=2)
#
# func(1,c=3)


# # 取得参数的个数
# def howlong(first, *other):
#     return print(1 + len(other))
#
#
# howlong(123, 234, 456)


# var1 = 123
#
# def func():
#     global  var1
#     var1 = 456
#     print(var1)
#
# func()
#
# print(var1)


# list1 = [1,2,3]
# it = iter(list1)
#
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# for i in range(10,20,2):
#     print(i)

# 迭代器
# def frange(start,stop,step):
#     x = start
#     while True:
#         while x < stop:
#             yield x
#             x += step
#
#
# for i in frange(10,20,0.5):
#     print(i)

# def true(): return True
# lambda : True
#
# lambda x: x <= (month, day)
#
# def func1(x):
#     return x<= (month,day)
#
# lambda item:item[1]
#
# def func2(item):
#     return item[1]


# filter()
# map()
# reduce()
# zip()


# a = [1, 3, 4, 5, 6, 7]
# print(list(filter(lambda x: x > 2, a)))


# a = [1, 2, 3]
# b = [4, 5, 6]
# print(list(map(lambda x, y: x + y, a, b)))

# from functools import reduce
#
# print(reduce(lambda x, y: x + y, [2, 3, 4], 1))


# a = (1, 2, 3)
# b = (4, 5, 6)
# c = zip(a, b)
#
# # print(c)
#
# for i in c:
#     print(i)

#
# dicta = {'a': 'aa', 'b': 'bb'}
# print(dicta.values())
# print(dicta.keys())
#
# dictb = zip(dicta.values(), dicta.keys())
# print(dictb)
# print(dict(dictb))  # 字典


def sum(a):
    def add(b):
        return a + b

    return add


num = sum(2)
print(num(4))
