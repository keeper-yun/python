# -*- coding: utf-8 -*-

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# student_canteen = 'student_canteen.xlsx'
#
# # 读取数据
# data = pd.read_excel(student_canteen, names=None, header=0, index_col=u'cardID')
#
# data = data.dropna(how='any')
#
# print(data)
#
# # 字体
# plt.rcParams['font.family'] = 'SimHei'
#
#
# plt.figure(figsize=(8, 6))
# plt.bar(range(len(data)), data[u'price'])
# plt.xlabel('卡号18040+xx')
#
# plt.show()




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

student_canteen = 'student_canteen.xlsx'

# 读取数据
data = pd.read_excel(student_canteen, names=None, header=0, index_col=u'cardID')
data = data.dropna(how='any')

# 字体
plt.rcParams['font.family'] = 'SimHei'

plt.figure(figsize=(8, 6))
plt.hist(data[u'price'])
plt.xlabel('价格')
plt.ylabel('频率')

plt.show()

