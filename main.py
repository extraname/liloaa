import requests
from bs4 import BeautifulSoup


def parse_start_page(link):
    result = requests.get(link)
    soup = BeautifulSoup(result.text, 'html.parser')
    necessary_block = soup.find("div", {"id": "posts"})
    result = necessary_block.find_all_next("a", {'class': "mainlink"})
    for a in result:
        print(a['href'])


parse_start_page("https://gidonline.io/")


# def parse_one_page(url):
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     infoblock = soup.find("div", {'id': "single"})
#     # # print(infoblock)
#     film_name = url.split('/')[-2]
#
#     jpg_path = infoblock.find("img", {'class': "t-img"})['src']
#     jpg = f"https://gidonline.io{jpg_path}"
#
#     with open(f'results/{film_name}.jpg', 'wb') as f:
#         f.write(requests.get(jpg).content)
#
#     content = infoblock.find('div', {'class': 'infotext'})
#     t = content.find('p')
#     tt = t.text.encode('utf-8')
#     print(tt.decode('cp1251'))
#
#
#     # with open(f'results/{film_name}.txt', 'w', encoding='utf-8') as file:
#     #     file.write(t)
#
#
# parse_one_page('https://gidonline.io/film/pochemu-zhenshhiny-ubivayut/')
