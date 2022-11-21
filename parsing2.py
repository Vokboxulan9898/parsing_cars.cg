# python3 -m venv venv
# venv/bin/activate

# pip3 install -r requirements.txt


import requests
from bs4 import BeautifulSoup
import csv

def write_to_csv(data):
    with open('cars.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'], data['price'], data['img']])

def get_html(url):
    response = requests.get(url)
    return response.text
def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    page_list = soup.find('div', class_ = 'pages fl'). find_all('a') last_page = page_list[-2].text
    return last_page

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    cars = soup.find('div', class_ = 'catalog-list').find_all('a', class_ = 'catalog-list-item')
    # print(cars)
    for car in cars:
        try:
            title = car.find('span', class_='catalog-item-caption').text.strip()
        except:
            title = ''
        try:
            img = car.find('img', class_ = 'catalog-iteam-cover-img').get('src')
        except:
            img = ''
        try:
            price = car.find('span', class_='catalog-iteam-prece').text
        except:
            price = ''

        data = {'title': title, 'price': price, 'img': img}
        write_to_csv(data)

            

        #         print(price)
        # print(img)
        #     # print(title)

def main():
    url = 'https://cars.kg/offers'
    html = get_html(url)
    # get_data(html)
    get_total_pages(html)

with open('cars.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow([ti])
main()