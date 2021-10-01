import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, 팀순위 표를 가져오기
ranking_table = soup.select('#regularTeamRecordList_table > tr')
# print(ranking_table)

# ranking_table (tr들) 의 반복문을 돌리기
for ranking_info in ranking_table:
    # print('######', ranking_info)
    rank = ranking_info.select_one('th > strong').text
    name = ranking_info.select_one('td.tm > div > span').text
    win_rate = ranking_info.select_one('td:nth-child(7) > strong').text

    # 문자열(string) 을 부동소숫점형(float)으로 강제 형변환
    if float(win_rate) > 0.5:
        print(rank, name, win_rate)