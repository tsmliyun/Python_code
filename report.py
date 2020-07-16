from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from PIL import Image
import numpy as np


# wc = WordCloud(
#     background_color='white',  # 设置背景颜色
#     mask='',  # 设置背景图片
#     font_path='./SimHei.ttf',  # 设置字体，针对中文的情况需要设置中文字体，否则显示乱码 max_words=100, # 设置最大的字数
#     # stopwords=STOPWORDS,  # 设置停用词
#     max_font_size=150,  # 设置字体最大值 width=2000,# 设置画布的宽度 height=1200,# 设置画布的高度
#     random_state=30  # 设置多少种随机状态，即多少种颜色
# )


# 生成词云

def create_word_cloud(f):
    print('根据词频计算词云')

    text = " ".join(jieba.cut(f, cut_all=False, HMM=True))
    wc = WordCloud(
        font_path="./SimHei.ttf",
        max_words=100,
        width=2000,
        height=1200,
    )

    wordcloud = wc.generate(text)

    # 写词云图片
    wordcloud.to_file("wordcloud.jpg")

    # 显示词云文件
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

def remove_stop_words(f):
    stop_words = ['学会', '就是', '什么']
    for stop_word in stop_words:
        f = f.replace(stop_word, '')
    return f


f = '数据分析全景图及修炼指南\
26 学习数据挖掘的最佳学习路径是什么?\
27 Python 基础语法:开始你的 Python 之旅\
28 Python 科学计算:NumPy\
29 Python 科学计算:Pandas\
30 学习数据分析要掌握哪些基本概念?\
31 用户画像:标签化就是数据的抽象能力\
32 数据采集:如何自动化采集数据?\
33 数据采集:如何用八爪鱼采集微博上的“D&G”评论?\
34 Python 爬虫:如何自动化下载王祖贤海报?\
35 数据清洗:数据科学家 80% 时间都花费在了这里?\
36 数据集成:这些大号一共 20 亿粉丝?\
37 数据变换:大学成绩要求正态分布合理么?\
38 数据可视化:掌握数据领域的万金油技能\
39 一次学会 Python 数据可视化的 10 种技能'

f = remove_stop_words(f)
create_word_cloud(f)



