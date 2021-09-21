from bs4 import BeautifulSoup
import requests
import html

anime_site = requests.get("https://jw-webmagazine.com/best-anime/")

anime_html = anime_site.text

anime_soup = BeautifulSoup(anime_html, 'html.parser')

top_animes = anime_soup.find_all('h2')

text_list = []

for i in top_animes:
    anime_text = i.get_text()
    text_list.append(anime_text)

#
#     for i in text_list:
#         file.write(i)
with open('anime_list.txt', 'w', encoding='utf8') as file:
    for i in reversed(text_list):
        word = html.unescape(i)
        print(f"The encoded word is {word}")
        file.write(i+ '\n')