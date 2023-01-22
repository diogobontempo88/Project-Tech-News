import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    def scrape_novidades(html_content: str) -> list:
    selector = Selector(html_content)
    list = []
    for news in selector.css("div.post-outer"):
        text = news.css("h2.entry-title ::attr(href)").get()
        list.append(text)

    return list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)

    link = selector.css("div.nav-links a.next::attr(href)").get()

    return link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
