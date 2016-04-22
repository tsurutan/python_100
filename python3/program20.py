# coding: UTF-8
import json

with open("jawiki-country.json") as f:
    article_json = f.readline()
    while article_json:
        article_dict = json.loads(article_json)
        if article_dict["title"] == u"イギリス":
            print(article_dict["text"])
        article_json = f.readline()
