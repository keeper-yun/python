

import requests
from lxml import etree

url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0\
     Safari/537.36 Edg/120.0.0.0'
}

resp = requests.get(url, headers=headers)

html = etree.HTML(resp.text)

movies_list = []

def get_data_movie(*args):
    title = ''
    for text in args:
        if text:
            title += text[0]
    return title

for li in html.xpath('//*[@id="content"]/div/div[1]/ol/li'):
    tem_title = li.xpath('./div/div[2]/div[1]/a/span/text()')
    tem_title2 = li.xpath('./div/div[2]/div[1]/a/span[2]/text()')
    tem_title3 = li.xpath('./div/div[2]/div[1]/a/span[3]/text()')
    title = get_data_movie(tem_title, tem_title2, tem_title3)
    context = li.xpath('./div/div[2]/div[2]/p[1]/text()[1]')
    point = li.xpath('./div/div[2]/div[2]/div/span[2]/text()')

    context = context[0]
    context_split = context.split('导演:')

    director = (context_split[1].split('主演:')[0].strip()
                if len(context_split) > 1
                else "未知")

    cast = (context_split[1].split('主演:')[1].split('/')[0].strip()
            if len(context_split) > 1 and '主演:' in context_split[1]
            else "未知")

    point = point[0]

    movies_list.append((title, director, cast, point))

with open('movies.txt', 'w', encoding='utf-8') as f:
    for movie in movies_list:
        f.write(f"Top {movies_list.index(movie) + 1}\n")
        f.write(f"电影标题: {movie[0]}\n")
        f.write(f"导演: {movie[1]}\n")
        f.write(f"主演: {movie[2]}\n")
        f.write(f"评分: {movie[3]}\n")
        f.write("\n")

