from bs4 import BeautifulSoup

with open('batman_movies.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    movie = soup.find_all('div', class_ = 'movie')
    for name in movie:
        print(name.h3.text +" "+ name.p.text)