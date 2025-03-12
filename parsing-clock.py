import requests
from bs4 import BeautifulSoup
import json

def get_clock():
    clocks = []
    for i in range(4):
        url = f'https://parsinger.ru/html/index1_page_{i+1}.html'
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            rows = soup.find_all('div', class_='item')
            for row in rows:
                name = row.find('a', class_='name_item').text.encode('latin1').decode('utf-8')
                description = row.find('div', class_='description').text.encode('latin1').decode('utf-8').strip()
                url_ = row.find('a').get('href')
                cost = row.find('p', class_='price').text.encode('latin1').decode('utf-8')
                print(f'Наименование: {name}\n{description}\nСсылка: {url_}\nСтоимость: {cost}\n')
                clock ={
                    'Наименование': name,
                    'Описание': description,
                    'Ссылка': url_,
                    'Стоимость': cost
                }
                clocks.append(clock)
    return clocks

clock_base = get_clock()

def write_clock_json (clock_base: list):
    with open ('clock.json', 'w', encoding='utf-8') as file:
        json.dump(clock_base, file, indent=2, ensure_ascii=False)
write_clock_json(clock_base)