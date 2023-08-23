import random
from bs4 import BeautifulSoup

with open('batman_movies.html') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

divs = soup.find_all('div', class_="movie")
shuffled = divs[:]
random.shuffle(shuffled)

parent = divs[0].parent
parent_class = divs[0].parent['class']

shuffled_parent = soup.new_tag(parent.name)
shuffled_parent['class'] = parent_class

for shuffled_div in shuffled:
    shuffled_parent.append(shuffled_div)

parent.replace_with(shuffled_parent)

html_text = str(soup)
with open("scrambled_movie.html", 'w')as file:
    file.write(html_text)
