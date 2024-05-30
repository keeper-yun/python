

import requests

url = f"https://fanyi.baidu.com/sug"
headers = {
    'User-Agent': 'Mozilla/5.0 \
    (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

kword = input(f"请输入想要翻译的内容: ")

data = {
    'kw': kword
}

resp = requests.post(url, data, headers=headers)

json_data = resp.json()

translations = []
if 'data' in json_data:
    for item in json_data['data']:
        if 'v' in item:
            translations.append(item['v'])

print("译文：")
for translation in translations:
    print(translation)
