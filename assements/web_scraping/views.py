# django imports
from django.shortcuts import render

# external imports
from bs4 import BeautifulSoup
import requests

# internal imports
from logger.log import Log, get_logger


def index(request):
    log = Log()
    logger = get_logger(__name__)
    try:
        log.write_log(request, 20)
        logger.debug('This is an informational message.')
        url_link = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
        result = requests.get(url_link).text
        doc = BeautifulSoup(result, "html.parser")
        content = doc.find(id='content')
        title = doc.find(id='firstHeading').text
        # Ex: California, United States
        search_text = 'California'  # input('Enter Search Text:')
        find_by_text = content.find_all(text=search_text)
        map_img_url = doc.find(class_='thumbinner').next.next.get('src')
        return render(request, 'web_scraping/index.html',
                      {'content': content,
                       'title': title,
                       'find_by_text': find_by_text,
                       'search_text': search_text,
                       'map_img_url': map_img_url
                       })

    except Exception as error:
        log.write_log(str(error), 40)
        logger.error('An error occurred!')
        return render(request, 'web_scraping/index.html', {'content': error})
