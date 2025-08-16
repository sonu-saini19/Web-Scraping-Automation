
#Step-1: Import all necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_3_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_3_0_na_na_na&as-pos=3&as-type=TRENDING&suggestionId=mobiles&requestId=b45fbf47-3c36-4bf1-9757-9f45c0e4e8c9"
headers = {"User -Agent": "Mozilla/5.0 (Window NT 10.0; Win64) AppleWebkit/537.36 Chrome/117.0.0.0"}

response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text,"html.parser")
print(response)
#print(soup.prettify)
mobiles = soup.find_all('div', class_ = 'col col-7-12')
print(len(mobiles))
names = []   #KrHvwW
#prices = []
ratings = []
for mobile in mobiles:
    name = mobile.find("div",class_="KzDlHZ")
    rating = mobile.find("div",class_="_5OesEi")
    print(name,rating)
    if name and rating:
        names.append(name.get_text())
        ratings.append(rating.get_text())

df = pd.DataFrame({
    "names" : names,
    "ratings" : ratings
})

df.to_csv("flipkart_mobiles.csv",index=True)
print("Data scraped and saved to 'flipkart_mobiles.csv'")


