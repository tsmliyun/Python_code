import math
import sys

# 求最小公倍数

# a, b = [int(i) for i in input().strip().split(' ')]
#
# s = max(a, b)
#
# for i in range(1, s + 1):
#     if s * i % a == 0 and s * i % b == 0:
#         break
#
# print(int(s * i))


# 计算一个数字的立方根

# while True:
#     n = sys.stdin.readline().strip()
#     if n:
#         n = float(n)
#         print('%.1f' % math.pow(n, 1.0 / 3))
#     else:
#         break


# 将一个字符串颠倒过来 并输出
# print(input()[::-1])

# 从输入任意个整型数，统计其中的负数个数并求所有非负数的平均值，结果保留一位小数，如果没有非负数，则平均值为0
# while True:
#     try:
#         li = map(int, input().split())
#         count1 = 0
#         count2 = 0
#         su = 0
#         for i in li:
#             if i < 0:
#                 count1 += 1
#             else:
#                 count2 += 1
#                 su += i
#         print(count1)
#         print('%.1f' % (float(su) / count2))
#     except:
#         break

# 连续输入字符串(输出次数为N,字符串长度小于100)，请按长度为8拆分每个字符串后输出到新的字符串数组，长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
# 首先输入一个整数，为要输入的字符串个数。
while True:
    try:
        a = int(input())
        for i in range(a):
            s = input()
            while len(s) > 8:
                print(s[:8])
                s = s[8:]
            print(s.ljust(8, "0"))
    except:
        break
