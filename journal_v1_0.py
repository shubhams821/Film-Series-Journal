# -*- coding: utf-8 -*-
"""journal-v1.0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TzELPgPru7970GbpevVHCa3nUOEFxTgV
"""

shubhamst

import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Replace this with your Letterboxd username
username = 'shubhamst'
url = f'https://letterboxd.com/{username}/films/diary/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the diary entries on the page
entries = soup.find_all('li', class_='poster-container')

films = []

for entry in entries:
    film_title = entry.find('img')['alt']
    watched_date = entry.find('meta', {'itemprop': 'datePublished'})['content']
    date_object = datetime.strptime(watched_date, '%Y-%m-%d')

    films.append({
        'title': film_title,
        'date': date_object.strftime('%d-%m-%Y')
    })

# Print the films watched this month
for film in films:
    print(f"• {film['date']}: {film['title']}")
print(response.text)

import requests
from bs4 import BeautifulSoup
from collections import defaultdict

# Replace with the URL of your Letterboxd diary page
url = 'https://letterboxd.com/shubhamst/films/diary/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all diary entries
entries = soup.find_all('tr', class_='diary-entry-row')

# Dictionary to store films organized by month
films_by_month = defaultdict(list)

for entry in entries:
    # Extract the viewing date
    day_element = entry.find('td', class_='td-day')
    viewing_date = day_element.text.strip()

    # Extract the film title
    film_title_element = entry.find('h3', class_='headline-3')
    film_title = film_title_element.text.strip()

    # Extract the month and year from the entry's link (assuming it's part of the URL)
    date_link = day_element.find('a')['href']
    date_parts = date_link.split('/')[-4:]  # ['2024', '05', '23']
    year = date_parts[0]
    month_number = date_parts[1]

    # Convert month number to month name
    month_name = datetime.strptime(month_number, "%m").strftime("%B")
    review_link = entry.find('a', class_ ="edit-review-button has-icon icon-16 icon-edit")
    review = review_link.get('data-review-text')

    # Store the film entry in the corresponding month
    films_by_month[f"{month_name} {year}"].append({
        'date': viewing_date,
        'title': film_title,
        "review" : review
    })

# Print the films organized by month
for month, films in films_by_month.items():
    print(f"\n{month}")
    for film in films:
        print(f"{film['date']}: {film['title']}")

for month, films in films_by_month.items():
    for film in films:
        print()
        print(f"{film['title']}\n{film['date']}-{month}\n\n{film['review']}")
        print()

films_by_month

