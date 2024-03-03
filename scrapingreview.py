import requests
from bs4 import BeautifulSoup
import json
import time
import concurrent.futures

# グローバルセッションの初期化
session = requests.Session()

# レビューの最大ページ取得
def get_last_pagination(soup):

    pagination = soup.find('a', class_='c-pagination__last')
    lastpage_href = pagination.get('href')
    last_page = lastpage_href.split('=')[-1]

    return int(last_page)

# 映画のタイトル取得
def get_title(soup):
    
    script_tag = soup.find("script", type='application/ld+json')
    if script_tag:
        script_json = script_tag.string.strip()
        script_content = json.loads(script_json)
        title = script_content['name']
        
    return title

# そのページのレビューを取得
def get_reviews_on_page(soup):
    reviews = []
    for review in soup.find_all('div', class_='p-mark__review'):
        content = review.text.strip()
        reviews.append(content)
    return reviews

# 単一のページのレビュー取得
def scrape_single_page(page_url):
    r = session.get(page_url)  # セッションを使用してリクエスト
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        return get_reviews_on_page(soup)
    else:
        print(f"Failed to retrieve HTML data for URL: {page_url}")
        return

# 全ページ分のレビューを取得
def scrape_reviews(movie_url):
    
    # HTTP GETリクエストを送信してWebページのHTMLデータを取得
    r = session.get(movie_url)
    if r.status_code == 200:
        html_doc = r.text
    else:
        print("Failed to retrieve HTML data. Status code:", r.status_code)
        return
    
    # BeautifulSoupを使ってHTMLを解析
    soup = BeautifulSoup(html_doc, 'html.parser')
    title = get_title(soup)
    last_page = get_last_pagination(soup)
    all_reviews = []

    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        
        page_urls = [f"{movie_url}?page={page_number}" for page_number in range(1, last_page + 1)]
        reviews_lists = executor.map(scrape_single_page, page_urls)
        for reviews in reviews_lists:
            if reviews is not None:  # Noneチェックを追加
                all_reviews.extend(reviews)
            
    filename = f"{title}_reviews.jsonl"
    with open(filename, 'w') as f:
        for review in all_reviews:
            data = {"title": title, "review": review}
            json.dump(data, f, ensure_ascii=False)
            f.write('\n')
    print("作品のレビュー抽出が終了しました。:", title)

"""  
    # JSONLファイルを読み込んで表示する関数
    with open(filename, 'r') as file:
        for line in file:
            # 各行のJSONオブジェクトを読み込む
            data = json.loads(line)
            # 読み込んだデータを表示する
            print(data)
"""            

if __name__ == "__main__":
    
    # 処理を開始する前の時間を記録
    start_time = time.time()
    
    # WebページのURL
    movie_url = 'https://filmarks.com/movies/109465'
    #reviewを取得
    scrape_reviews(movie_url)

    # 処理を終了する時間を記録
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("処理にかかった時間:", elapsed_time, "秒")
