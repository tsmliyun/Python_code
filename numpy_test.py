import numpy as np

#
# a = np.array([1, 2, 3])
#
# b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 8]])
#
# b[1, 1] = 10
#
# # shape 获取数组的大小
# print(a.shape)
# print(b.shape)
#
# # 获取元素的属性
# print(a.dtype)
#
# print(b)


persontype = np.dtype({
    'names': ['name', 'age', 'chinese', 'math', 'english'],
    'formats': ['S32', 'i', 'i', 'i', 'f']
})

peoples = np.array(
    [("ZhangFei", 32, 75, 100, 90), ('Gy', 24, 85, 96, 88.5), ("ZY", 28, 85, 92, 96.5), ("HZ", 29, 65, 85, 100)],
    dtype=persontype)

ages = peoples[:]['age']
chineses = peoples[:]['chinese']
math = peoples[:]['math']
english = peoples[:]['english']

# print(ages)
# print(chineses)
# print(math)
# print(english)

# 计算平均值
print(np.mean(ages))
print(np.mean(chineses))
print(np.mean(math))
print(np.mean(english))

# 连续数组的创建
x1 = np.arange(1, 11, 2)
x2 = np.linspace(1, 9, 5)
print(x1)
print(x2)

# +
print(np.add(x1, x2))

# -
print(np.subtract(x1, x2))

# *
print(np.multiply(x1, x2))

# /
print(np.divide(x1, x2))

# n次方
print(np.power(x1, x2))

# 取余数
print(np.remainder(x1, x2))

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.amin(a))
print(np.amin(a, 0))
print(np.amax(a))
print(np.amax(a, 0))
print(np.amax(a, 1))
print(np.ptp(a))
print(np.ptp(a, 0))
print(np.ptp(a, 1))

print(np.percentile(a, 50))
print(np.percentile(a, 50, axis=0))
print(np.percentile(a, 50, axis=1))


# 加权平均值
a = np.array([1,2,3,4])
wts = np.array([1,2,3,4])
print(np.average(a))
print(np.average(a,weights=wts))

# 标准差
print(np.std(a))

# 方差
print(np.var(a))