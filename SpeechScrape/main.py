
from bs4 import BeautifulSoup
import requests
import bs4
from requests.models import Response
import re


def url_to_list():
    url_lst = []
    file = open("urls.txt", "r", encoding="utf-8")  # links txt
    for url in file:
        url_lst.append(url)
    converted_list = []
    for element in url_lst:
        converted_list.append(element.strip())
    return converted_list


converted_list = url_to_list()  # 1
print(converted_list)


for items in converted_list:
    r = requests.get(items)
    title_h = bs4.BeautifulSoup(r.text, "html.parser")
    title = title_h.find("h2", class_="presidential-speeches--title")
    tit = title.text
    x = tit.replace(":", "")
    x = x.rstrip()
    print(type(x))
    file = x + ".txt"
    with open(file, "w", encoding="utf-8") as f:
        f.write(x)
        f.write("\n")
        bs = bs4.BeautifulSoup(r.text, "html.parser")
        paragraphs = bs.findAll("p")
        other_paragraph = [p for p in paragraphs]
        for div in other_paragraph:
            print(div)
            f.write(div.text)
