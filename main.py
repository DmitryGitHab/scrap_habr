import requests
from bs4 import BeautifulSoup


KEYWORDS = ['GitHub', 'Python *', 'Java *', 'Big Data *', 'Хакатоны']
HEADERS = {
    'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415; _gid=GA1.2.512914915.1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru; _ym_isad=2; __gads=ID=87f529752d2e0de1-221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'sec-ch-ua-mobile': '?0'}

base_url = 'https://habr.com'
url = base_url + '/ru/all/'

response = requests.get(url, headers=HEADERS)
response.raise_for_status()  # проверка, что данные пришли

text = response.text
soup = BeautifulSoup(text, features='html.parser')
posts = soup.find_all('article')

for post in posts:
    hubs = post.find_all(class_='tm-article-snippet__hubs-item')
    hubs = set(hub.text.strip() for hub in hubs)

    for hub in hubs:
        if hub in KEYWORDS:
            title = post.find(class_='tm-article-snippet__title-link').text
            href = url + post.find(class_='tm-article-snippet__title-link').attrs['href']
            time = post.find(class_='tm-article-snippet__datetime-published').time['datetime'][:10]
            print(time, title, href)
            break
