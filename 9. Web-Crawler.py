import requests
from bs4 import BeautifulSoup


# This is a simple WebCrawler which is compiling the list of top 250 movies from IMDB.

def worm(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.imdb.com/chart/top'                                  #+ str(page) + '/'#      Use this part is there are multiple pages
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="html.parser")                # BeautifulSoup is a useful package which helps pre-processing data from web
        rank = 1
        for link in soup.findAll('td', {'class': 'titleColumn'}):
            new_link = link.contents[1]                                         # .contents is used to the children of the current tag. You can read documentation here :- https://www.crummy.com/software/BeautifulSoup/bs4/doc/
            href = ('https://www.imdb.com' + new_link.get('href'))
            print(str(rank) + '. ', end='')
            item_data(href)
            rank += 1
        page += 1


def item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    for header in soup.findAll('div', {'class': 'title_wrapper'}):
        print(header.contents[1].contents[0], end='(')
    for year in soup.findAll('span', {'id': 'titleYear'}):
        print(year.contents[1].string + ')')
    for header in soup.findAll('span', {'itemprop': 'ratingValue'}):
        print('Rating: ' + header.string)
    print('Link: ' + item_url, end='\n\n')


worm(1)