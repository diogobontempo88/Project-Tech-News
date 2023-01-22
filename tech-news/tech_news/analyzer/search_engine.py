from tech_news.database import search_news
import datetime

# Requisito 6
def search_by_title(title):
    result = search_news({"title": {"$regex": title, "$options": "i"}})
    post_list = []
    for post in result:
        post_list.append((post["title"], post["url"]))
    return post_list


# Requisito 7
def search_by_date(date):
    try:
        data = datetime.datetime.strptime(date, "%Y-%m-%d")
        data_formatada = data.strftime("%d/%m/%Y")
        result = search_news(
            {"timestamp": {"$regex": data_formatada}}
        )
        post_list = []
        for post in result:
            post_list.append((post["title"], post["url"]))
        return post_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    result = search_news({"tags": {"$regex": tag, "$options": "i"}})
    post_list = []
    for post in result:
        post_list.append((post["title"], post["url"]))
    return post_list


# Requisito 9
def search_by_category(category):
    result = search_news({"category": {"$regex": category, "$options": "i"}})
    post_list = []
    for post in result:
        post_list.append((post["title"], post["url"]))
    return post_list
