# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

catering_sale = 'canteen_persons.xlsx'
# 读取数据
data = pd.read_excel(catering_sale, names=None, header=0, index_col=u'时间')


# data = data.head(20)

data = data.dropna(how='any')

data_list = []

for i in data.index:
    i = i.split(' ')
    data_list.append(i[1])

plt.plot(data_list, data[u'人数'])

plt.ylabel(u'金额', fontproperties='SimHei')
plt.xlabel(u'时间:2018/10/9', fontproperties='SimHei')

plt.xticks(rotation=45)
plt.grid(True)
plt.show()

