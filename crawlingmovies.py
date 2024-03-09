import requests
from bs4 import BeautifulSoup
import json

#上映中の36個の映画のurlを取得する
def extract_all_movies(soup):
    mainpage_url = 'https://filmarks.com'
    href_set = set()
    for tag in soup.find_all('a', class_='swiper-no-swiping'):
        href = tag.get('href')
        href_set.add(href)


    href_list = list(href_set)
    for i in range(len(href_list)):
        print(i+1, href_list[i])

    #それぞれの映画のURLを作成
    movies_url = []
    for i, href in enumerate(href_list):
        movies_url.append(mainpage_url + href_list[i])
        print("movie_url:"+ movies_url[i])

    return movies_url

# レビューの最大ページ取得
def get_last_pagination(soup):
    
    pagination = soup.find('a', class_='c-pagination__last')
    lastpage_href = pagination.get('href')
    last_page = lastpage_href.split('=')[-1]
    print(last_page)

    return last_page

#レビューのみを抽出
def get_review(soup):
    # 映画のタイトル取得
    script_tag = soup.find("script", type='application/ld+json')
    if script_tag:
        script_json = script_tag.string.strip()
        script_content = json.loads(script_json)
        title = script_content['name']
        print(title)

    # 1ページ目のレビューを取得　
    content = []
    i = 0

    # JSONファイルに書き込み

    with open('reviews.json', 'w') as f:

        for review in soup.find_all('div', class_='p-mark__review'):
            content = review.text
            #print(content)
            i += 1
            #辞書型に変換
            data = {"title": title, "review":content}
            try:
                json.dump(data, f, ensure_ascii=False)
                f.write('\n')
                print(f"{i}:書き込みが正常に完了しました。")
            
            except Exception as e:
                print("CSVファイルの書き込み中にエラーが発生しました:", e)
            
    # JSONLファイルを読み込んで表示する関数
    with open('reviews.json', 'r') as file:
        for line in file:
            # 各行のJSONオブジェクトを読み込む
            data = json.loads(line)
            # 読み込んだデータを表示する
            print(data)

    
if __name__ == "__main__":
    
    # WebページのURL
    movie_url = 'https://filmarks.com/movies/109465'
    
   # WebページのURL
    url = 'https://filmarks.com/list/now?view=poster'
    

    # HTTP GETリクエストを送信してWebページのHTMLデータを取得
    r = requests.get(movie_url)
    if r.status_code == 200:
        html_doc = r.text
        #print(html_doc)
    else:
        print("Failed to retrieve HTML data. Status code:", r.status_code)


    # BeautifulSoupを使ってHTMLを解析
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    extract_all_movies(soup)
    
    #reviewを取得
    get_review(soup)
