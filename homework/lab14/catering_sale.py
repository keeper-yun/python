import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

catering_sale = 'catering_sale.xls'
# 读取数据
data = pd.read_excel(catering_sale, names=None, header=0, index_col=u'日期')


# data = data.head(20)

data = data.dropna(how='any')


print(data.describe())

plt.rcParams['font.family'] = 'SimHei'  # 或者其他支持中文的字体

plt.figure(figsize=(8, 6))
plt.boxplot(data[u'销量'])
plt.xlabel('销量')
plt.grid(True)
plt.show()


