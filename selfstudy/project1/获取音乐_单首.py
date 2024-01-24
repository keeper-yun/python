

# 单首歌曲爬取

import requests
import os

music_id=316100
music_url='http://music.163.com/song/media/outer/url?id=' + str(music_id)


headers = {
    'Cookie':'NMTID=00OL0Y2yEi1jFHm401qnULiwq_t_FcAAAGJLouI8Q; _iuqxldmzr_=32; WEVNSM=1.0.0; WNMCID=axpsax.1688703046071.01.0; WM_TID=NmPZy8jsIY5EEUUFEEaU0g251NuCTbNU; ntes_utid=tid._.MZTgL36TR0BAR1AUAEbR01j41JqSTj1u._.0; sDeviceId=YD-4pK7A5Y14y5FBwBBAUPBhwntXvVyUwiv; WM_NI=jBZA3rvNt5EqCkxWf%2BlElcD3tv9fAEAQRU%2BdMjqD4u8DoxsuYwvbKsS%2FQfyOsTEz9tdq%2Fgs6Js7d6a1yH8vkbGmO6dkP%2F%2B3JMwPAyZFE5ZZtTKXyoI9GdkwIe%2B9XSLMWZG8%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee89ae70f2ecfeb3b7598db88fa6c55e879f9bb0c13fbcf58dadf16788898eb2aa2af0fea7c3b92aaa9e96a2b27ab692bcd6c87b81b5b8b8e521b09ba484c739b8aaf787c44f838f9eb6aa708fb6bfa5b77ffc9ca199f27f9ba9ba83ca7991f19f87fc45b18c8b9bbc80a8afe188f23e8aadf985b56bf3a788d9f561a299a3b0b570a990e1ccb2428fa9a0a2fc52869bfbbbd9809895989aee43fb99ac8cf643a7f5f7b9d2488f8996a8bb37e2a3; __snaker__id=VZZqJUafAjQgTb0l; gdxidpyhxdE=lHqaCvGyNHSMClRXDMaYAgclmrytm2di0PeyUCAxwYVPwvwcmmnA3NPkZbQ999Qij2Y%2BB0%2BU6oi4%5Ca5zfpJ3k9mNLtrulQ6bW0ETyQM4fSSCoBiIBLx8ZEK7eIn56KoQvxow05w%2FnsxDS3vcjsaka3BcHcJksZSZCpDLJNHpXY0aeUSj%3A1706067518753; JSESSIONID-WYYY=5nYw8IXe0v4%5CRXC07Bbr%2FX0gEPvlszs%5CNpd3NTU2EBdH0KVPg%2FZZuHDQuZci3NA4lnIFQfreh7ORYc6povJwPpT3eAcK890zToscdpKu%5CbxnYMgv3XW8y9dwpYF1gcGt%5CgKPb6ZIgXyUUvns4R1i9%5CwMCnYBWPtorIvCpMcMvp0Kah%2FM%3A1706088363271; playerid=83555431',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

response = requests.get(url=music_url,headers=headers)

content=response.content

wantpath='E:/音乐'
wantname=f'雨爱.mp3'
path=os.path.join(wantpath,wantname)

with open(path,'wb')as f:
    f.write(content)
