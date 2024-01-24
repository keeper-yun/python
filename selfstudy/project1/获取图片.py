
import requests
import os
from lxml import etree

i=1

headers = {'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}

hero_url='https://pvp.qq.com/web201605/herodetail/ailin.shtml'
hero_response=requests.get(hero_url,headers=headers)
hero_response.encoding='gbk'
e=etree.HTML(hero_response.text)
name = e.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname')[0]
name=[name[0:name.index('&')] for name in name.split('|')]



for i,n in enumerate(name):
    url = f'https://game.gtimg.cn/images/yxzj/img201606/heroimg/155/155-mobileskin-{i}.jpg'
    response = requests.get(url,headers=headers)

    wantpath='/Users/11043/Pictures/图片/'
    wantname=f'艾琳-{n}.jpg'
    path=os.path.join(wantpath,wantname)
    with open(path,'wb') as f:
        f.write(response.content)

