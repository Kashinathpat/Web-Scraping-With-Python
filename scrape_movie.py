from bs4 import BeautifulSoup
import requests

movie_name = input("Enter the Movie name to search: ")

movies = requests.get(f'https://vegamovies.photos/?s={movie_name}').text
soup = BeautifulSoup(movies, 'lxml')

movie_found = soup.find_all('h3', class_="entry-title")
for item in movie_found:
    print(item.text)


