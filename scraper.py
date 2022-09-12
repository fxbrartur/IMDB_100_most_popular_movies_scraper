import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
headers = {"Accept-Language": "en,en-gb;q=0.5"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

movie_name = []
release = []
rating = []

table = soup.find('table', class_='chart full-width')

for movie_data in table.find_all('tbody'):
  rows = movie_data.find_all('tr')

  for row in rows:
      img = row.find('img', alt=True)["alt"]
      movie_name.append(img)

      release_year = row.find('span', attrs={'class': 'secondaryInfo'}).text.replace('(', '').replace(')', '')
      release.append(release_year)

      ratingColumn = row.find('td', attrs={'class': 'ratingColumn imdbRating'}).strong.text
      rating.append(ratingColumn)

imdb_dataframe = pd.DataFrame({"Movie name": movie_name, "Release Year": release, "IMDB's Movie Rating": rating})
imdb_dataframe.to_csv("IMDB_Most_Popular_Movies.csv")

imdb_dataframe.head(20)
