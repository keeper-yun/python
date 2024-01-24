
from lxml import etree
import requests

# 发送地址
url='https://nba.hupu.com/stats/players'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}

# 发送请求
response = requests.get(url,headers=headers)
# print(response.text)

# 处理结果
e=etree.HTML(response.text)

# 解析响应的数据
numbers=e.xpath('//table[@class="players_table"]//tr/td[1]/text()')
names=e.xpath('//table[@class="players_table"]//tr/td[2]/a/text()')
teams=e.xpath('//table[@class="players_table"]//tr/td[3]/a/text()')
point=e.xpath('//table[@class="players_table"]//tr/td[4]/text()')
names.insert(0,'姓名')

# 是否保存
with open('nba.txt','w',encoding='utf-8')as f:
    f.write('\n本赛季NBA球员得分情况——虎扑\n\n')
    for numbers, names, teams, point in zip(numbers, names, teams, point):
        f.write(f'排名:{numbers},姓名:{names},球队:{teams},得分:{point}\n')

