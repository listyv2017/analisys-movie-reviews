import requests
from bs4 import BeautifulSoup

# WebページのURL
url = 'https://filmarks.com/list/now?view=poster'
mainpage_url = 'https://filmarks.com'

# HTTP GETリクエストを送信してWebページのHTMLデータを取得
r = requests.get(url)

# もしリクエストが成功した場合（ステータスコードが200の場合）
if r.status_code == 200:
    # HTMLデータを取得
    url_html = r.text
    # HTMLデータを表示
    #print(html_doc)
else:
    print("Failed to retrieve HTML data. Status code:", r.status_code)


# BeautifulSoupを使ってHTMLを解析
soup = BeautifulSoup(url_html, 'html.parser')

# 特定のクラス名を持つ<a>タグを抽出
#links_with_class = soup.find_all('a', class_="swiper-no-swiping")

# 抽出された<a>タグを出力
#for link in links_with_class:
#    print(link)

href_set = set()
for tag in soup.find_all('a', class_='swiper-no-swiping'):
    href = tag.get('href')
    href_set.add(href)
    
#for i, href in enumerate(href_set):
#    print(i+1, href)

href_list = list(href_set)
for i in range(len(href_list)):
    print(i+1, href_list[i])

#それぞれの映画のURLを作成

movies_url = []
for i, href in enumerate(href_list):
    movies_url.append(mainpage_url + href_list[i])
    print("movie_url:"+ movies_url[i])


# HTTP GETリクエストを送信してWebページのHTMLデータを取得
r = requests.get(movies_url[0])

# もしリクエストが成功した場合（ステータスコードが200の場合）
if r.status_code == 200:
    # HTMLデータを取得
    movie_html = r.text
    # HTMLデータを表示
    #print(movie_html)
else:
    print("Failed to retrieve HTML data. Status code:", r.status_code)


# BeautifulSoupを使ってHTMLを解析
soup = BeautifulSoup(movie_html, 'html.parser')

revies_list = []
for tag in soup.find_all('a', ):
    href = tag.get('href')
    href_set.add(href)