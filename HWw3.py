import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

songs_info = soup.select ('table.list-wrap>tbody>tr>td.info')
rank=1
for song in songs_info:
    a_tag = song.select('a.artist.ellipsis')
    t_tag = song.select('a.title.ellipsis')
    artist = a_tag[0].text
    title = t_tag[0].text.strip()
    print (rank, artist, title)
    rank +=1







