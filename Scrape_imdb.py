import openpyxl
import requests
from bs4 import BeautifulSoup

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Top 250 Highest Rated Movies'

sheet.append(['Rank', 'Movie Name', 'Year', 'Genre', 'Ratings', 'Runtime'])

for i in range(1, 250, 50):
    html = requests.get(
        f'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start={i}&ref_=adv_nxt').text
    soup = BeautifulSoup(html, 'lxml')
    next = soup.find('a', class_='lister-page-next next-page')
    movies = soup.find_all('div', class_='lister-item-content')
    for item in movies:
        rank = item.find('span').text
        name = item.find('a').text
        year = item.find('span', class_='lister-item-year text-muted unbold').text
        genre = item.find('span', class_='genre').text.replace("\n", "")
        rating = item.find('strong').text
        runtime = item.p.find('span', class_='runtime').text

        sheet.append([rank, name, year[-5:-1], genre, rating, runtime])

excel.save('IMDB250.xlsx')
print("All Information Stored In Excel File : IMDB250.xlsx SuccessFully")

