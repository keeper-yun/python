

import requests
from lxml import etree

url='https://wap.biqupe.com/book_21570_13116296.html'
headers = {'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}

response = requests.get(url,headers=headers)

# print(response.text)

e = etree.HTML(response.text)

content=e.xpath('//div[@class="read-content"]/p/text()')

# print(content)

i=0

with open('第一章-我的26岁女房客.txt','w',encoding='utf-8') as f:
    for line in content:
        f.write(f'{line}\n')
