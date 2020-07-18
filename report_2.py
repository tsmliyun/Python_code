import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 数据准备
# N = 1000
# x = np.random.randn(N)
# y = np.random.randn(N)

# 用Matplotlib画散点图
# plt.scatter(x, y, marker='x')
# plt.show()

# 用seaborn 画散点图
# df = pd.DataFrame({'x': x, 'y': y})
# sns.jointplot(x="x", y="y", data=df, kind='scatter')
# plt.show()


# 折线图
# 折线图可以用来表示数据随着时间变化的趋势。

# x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
# y = [5, 3, 6, 20, 17, 16, 19, 30, 32, 35]

# 使用Matplotlib
# plt.plot(x,y)
# plt.show()

# df = pd.DataFrame({'x':x,'y':y})
# sns.lineplot(x="x",y="y",data=df)
# plt.show()

# 直方图

# 数据准备
# a = np.random.randn(100)
# s = pd.Series(a)

# plt.hist(s)
# plt.show()


# sns.distplot(s,kde=False)
# plt.show()


# sns.distplot(s)
# plt.show()


# 条形图
x = ['Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5']
y = [5, 4, 8, 12, 7]

# 用Matplotlib 画图
# plt.bar(x, y)
# plt.show()

# 用Seaborn画条形图
# sns.barplot(x, y)
# plt.show()


# 箱线图，又称盒式图，
# 它是在 1977 年提出的，由五个数值点组成:最大值 (max)、最小值 (min)、中位数 (median) 和上下四分位数 (Q3, Q1)。它可以帮我们分析出数据的差异性、 离散程度和异常值等


# 数据准备
# 生成 0-1之间 10*4 的维度数据
data = np.random.normal(size=(10, 4))
lables = ['A', 'B', 'C', 'D']

# 用Matplotlib 画箱线图
# plt.boxplot(data, labels=lables)
# plt.show()

# 用 Seaborn 绘制
df = pd.DataFrame(data, columns=lables)
sns.boxplot(data=df)
plt.show()
