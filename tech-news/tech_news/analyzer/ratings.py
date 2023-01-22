from tech_news.database import db, find_news
from collections import Counter

# Requisito 10
def top_5_news():
    result = db.news.find({}, {"_id": False}).sort(
            [
                ("comments_count", -1),
                ("title", 1),
            ]
        ).limit(5)

    post_list = []
    for post in result:
        post_list.append((post["title"], post["url"]))
    return post_list


# Requisito 11
def top_5_categories():
    result = find_news()
    post_list = []
    for post in result:
        post_list.append(post["category"])

    order_response = sorted(post_list)

    response = dict(Counter(order_response).most_common())

    new_response = [*response]

    return new_response

