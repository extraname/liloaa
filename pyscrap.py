import requests
from bs4 import BeautifulSoup

response = requests.get('http://python-3.ru')
soup = BeautifulSoup(response.text, 'html.parser')
# news = soup.find_all('div', {'class': "page_only"})

links = soup.find_all('h1', {"class": 'title'})


def nice_try_man():
    url = []
    for link in range(len(links)):
        url.append(links[link].a["href"])
    tit = []
    for title in range(0, len(links)):
        tit.append(links[title].a['title'])
    result = dict(zip(url, tit))

    return result


# some problems with github

print(nice_try_man())
