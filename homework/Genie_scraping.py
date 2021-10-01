import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


client = MongoClient('localhost',27017)
db=client.dbsparta
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')




songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')



for tr in trs:

    a_tag = tr.select_one('td.info > a.title.ellipsis')
    if a_tag is not None:
        # 순위
        rank = tr.select_one('tr:nth-child(n) > td.number').text[0:2].strip()
        # 곡 정보
        title = tr.select_one(' td.info > a.title.ellipsis').text.strip()
        # 가수
        artist = tr.select_one(' a.artist.ellipsis').text
        print(rank, title, artist)

    doc={
        'rank':rank,
        'title':title,
        'artist':artist
    }
    db.songs.insert_one(doc)