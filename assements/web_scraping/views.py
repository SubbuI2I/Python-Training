from django.shortcuts import render

# External Imports
from bs4 import BeautifulSoup
import requests


def index(request):
    try:
        url_link = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
        result = requests.get(url_link).text
        doc = BeautifulSoup(result, "html.parser")
        content = doc.find(id='content')
        title = doc.find(id='firstHeading').text
        # Ex: California, United States
        search_text = input('Enter Search Text:')
        find_by_text = content.find_all(text=search_text)
        return render(request, 'web_scraping/index.html',
                      {'content': content,
                       'title': title,
                       'find_by_text': find_by_text,
                       'search_text': search_text
                       })
    except Exception as error:
        return render(request, 'web_scraping/index.html', {'content': error})
