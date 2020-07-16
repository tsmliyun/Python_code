# 这是一个元组 demo

# zoo = ('python', 'elephant', 'penguin')
# print('Number of animals in the zoo is', len(zoo))
#
# print(zoo[1])
#
# new_zoo = 'monkey', 'camel', zoo
# print('Number of cages in the new zoo is', len(new_zoo))
#
# print('all animals in the new zoo', new_zoo)
# print('Animals brought from old zoo are', new_zoo[2])
# print('Last animal brought from old zoo is', new_zoo[2][2])
# print('Number of animals in the new zoo is',
#       len(new_zoo) - 1 + len(new_zoo[2]))


# l = [1,2,"hello","world"]
# # print(l)
#
# tup = (1,2,"hello","world")
# # print(tup)
#
# new_tup = tup + (5,)
# # print(new_tup)
#
# l.append(5)
# # print(l)
#
# # Python 中的列表和元组都支持负数索引
# print(l[-1])
# print(tup[-1])
#
# # 列表和元组都支持切片操作
# print(l[1:3])
# print(tup[1:3])
#
#
# print(list((1, 2, 3)))
# print(tuple([4,5,6]))


l = [1,2,3]
tup = (1,2,3)

print(l.__sizeof__())
print(tup.__sizeof__())



