from bs4 import BeautifulSoup
import requests
import pandas as pd


response = requests.get("https://www.nba.com/teams")
NBA_web_page = response.text

# print(NBA_web_page)

soup = BeautifulSoup(NBA_web_page, "html.parser")
article_texts = []
article_links = []
articles = soup.find_all(name="a", class_="TeamFigure_tfMainLink__mH93D Anchor_external__Mh-vB Anchor_complexLink__2NtkO")
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

print(article_texts)
print(article_links)

df1 = pd.DataFrame(article_texts)
df2 = pd.DataFrame(article_links)

result = pd.concat([df1, df2], axis=1)
result.to_csv('team-list.csv', index=False, sep=',')