import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

respose = requests.get(URL)
website_html = respose.text

soup = BeautifulSoup(website_html, "html.parser")

movies = soup.find_all(name='h3', class_="title")

titles = [movie.getText() for movie in movies]
titles = titles [::-1]

with open('Day 45\\movies.txt', mode='w') as file:
    for title in titles:
        print(title)
        file.write(f'{title}\n')

