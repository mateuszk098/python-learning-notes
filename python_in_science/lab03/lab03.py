'''
Static web scraping with BeautifulSoup.
Script gather several informations about The Way of Kings' from polish site - lubimyczytac.pl
'''

import requests
import json
from sys import argv
from os import path

from bs4 import BeautifulSoup


def book_scraping(filename: str):

    url = 'https://lubimyczytac.pl/ksiazka/4896952/droga-krolow'
    response = requests.get(url)

    # Was the query successful
    if response.status_code != requests.codes.ok:
        print('Something has gone wrong!')
    else:
        soup = BeautifulSoup(response.text, 'lxml')

        author = soup.find('a', class_='link-name').text.strip()  # type: ignore
        title = soup.find('h1', class_='book__title').text.strip()  # type: ignore
        cycle = soup.find('span', class_='d-none d-sm-block mt-1').a.text.strip()  # type: ignore
        category = soup.find(
            'a', class_='book__category d-sm-block d-none').text.strip()  # type: ignore

        sentence = 'd-sm-inline-block book-pages book__pages pr-2 mr-2 pr-sm-3 mr-sm-3'
        pages = soup.find('span', class_=sentence).text.strip().split()[0]  # type: ignore
        description = soup.find('div', class_='collapse-content').text.strip()  # type: ignore

        # Create dictionary
        keys = ['Author', 'Title', 'Cycle', 'Category', 'Pages', 'Description']
        values = [author, title, cycle, category, pages, description]
        dictionary = dict(zip(keys, values))

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file, ensure_ascii=False, indent=4)
        print(f'Saved information to file \'{filename}\'')


if __name__ == '__main__':

    try:
        filename = argv[1]
    except IndexError:
        print(f'Usage: {path.basename(__file__)} <filename.json>')
        exit(1)

    book_scraping(filename)
