from bs4 import BeautifulSoup
import requests

search = input("Enter name of Mobile brand : ").replace(" ", "+")

filename = input("Enter Name of file to save the Data : ")
url = f"https://www.flipkart.com/search?q={search}+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=realme+mobile%7CMobiles&requestId=ac189964-6c00-46dc-8ba0-79a059d755f7&as-searchtext=realm&page="

mobiles = requests.get(url).text
soup = BeautifulSoup(mobiles, 'lxml')

pages = soup.find('div', class_="_2MImiq")
total_pages = int(pages.span.text.split()[-1]) + 1
for i in range(1, total_pages):

    mobiles = requests.get(url + str(i)).text
    soup = BeautifulSoup(mobiles, 'lxml')

    mob = soup.find_all('div', class_='_1AtVbE col-12-12')
    for item in mob:
        name = item.find('div', class_='_4rR01T')
        price = item.find('div', class_='_30jeq3 _1_WHN1')
        specs = item.find('ul', class_='_1xgFaf')
        if name is not None:
            spec = ""
            for j in specs:
                spec = spec + str(j.text) + "\n"
            with open(f"{filename}.txt", 'a', encoding='utf-8') as file:
                file.write(f'Name : {name.text}\nPrice : {price.text}\nSpecification : {spec}\n\n')

print(f"All Information Stored In File : {filename}.txt SuccessFully")
