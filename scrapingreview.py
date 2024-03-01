import requests
from bs4 import BeautifulSoup
import csv
import json

#最大ページ数の取得
# WebページのURL
movie_url = 'https://filmarks.com/movies/109465'

# HTTP GETリクエストを送信してWebページのHTMLデータを取得
r = requests.get(movie_url)

# もしリクエストが成功した場合（ステータスコードが200の場合）
if r.status_code == 200:
    # HTMLデータを取得
    html_doc = r.text
    # HTMLデータを表示
    #print(html_doc)
else:
    print("Failed to retrieve HTML data. Status code:", r.status_code)


# BeautifulSoupを使ってHTMLを解析
soup = BeautifulSoup(html_doc, 'html.parser')

pagination = soup.find('a', class_='c-pagination__last')
lastpage_href = pagination.get('href')
last_page = lastpage_href.split('=')[-1]

print(last_page)

# 映画のタイトル取得
script_tag = soup.find("script", type='application/ld+json')
if script_tag:
    script_json = script_tag.string.strip()
    script_content = json.loads(script_json)
    print(script_content['name'])

# 1ページ目のレビューを取得　
content = []
i = 0
# csvファイルの作成
"""with open('reviews.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    for review in soup.find_all('div', class_='p-mark__review'):
        content = review.text
        print(content)
        i += 1
        try:
            writer.writerow([content])
            print(f"{i}:書き込みが正常に完了しました。")
        except Exception as e:
            print("CSVファイルの書き込み中にエラーが発生しました:", e)

"""

# JSONファイルに書き込み
"""
with open('reviews.json', 'w', newline='', encoding='utf-8') as outfiles:
    writer = csv.writer(f)

    for review in soup.find_all('div', class_='p-mark__review'):
        content = review.text
        #print(content)
        i += 1
        try:
            writer.writerow([content])
            #print(f"{i}:書き込みが正常に完了しました。")
        except Exception as e:
            print("CSVファイルの書き込み中にエラーが発生しました:", e)"""