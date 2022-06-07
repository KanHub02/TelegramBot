from bs4 import BeautifulSoup
import requests
import time

HOST1 = "https://ru.sputnik.kg/Kyrgyzstan/"
HEADERS1 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
}


def get_html(URL):
    request = requests.get(url=URL, headers=HEADERS)
    return request


def get_data_news(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="list__item")
    global news
    news = []
    for item in items:
        news.append(
            {
                item.find("a").get("href"),
                # 'title': item.find('a').get('title'),
                # 'image': item.find('picture').find('img').get('src'),
            }
        )
    return news


def scrapy_script_news():
    html = get_html(HOST1)
    if html.status_code == 200:
        links = []
        links.extend(get_data_news(html.text))
        return links

    else:
        raise Exception("Error in scrapy script function")


URL = "https://jut.su/anime/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
}


def get_requests(url, params=""):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="all_anime_global")
    domen = "https://jut.su"
    anime = []

    for item in items:
        anime.append({domen + item.find("a").get("href")})
    return anime


def scrapy_script():
    html = get_requests(URL)
    if html.status_code == 200:

        return get_data(html.text)

    else:
        raise Exception("Error in scrapy script function")


# html = get_requests(URL)
# print(get_data(html.text))
