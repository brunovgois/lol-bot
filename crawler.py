import requests
from bs4 import BeautifulSoup

base_url = 'https://br.leagueoflegends.com'

page = requests.get('https://br.leagueoflegends.com/pt-br/news/tags/patch-notes')
soup = BeautifulSoup(page.text, 'html.parser')


gatsbySoup = soup.find(id='___gatsby')
gatsbySoup_img_items = gatsbySoup.find_all('a')
link = gatsbySoup_img_items[0]['href']
link_to_patch_page = base_url + link

print(link_to_patch_page)


page2 = requests.get(link_to_patch_page)
soup2 = BeautifulSoup(page2.text, 'html.parser')

# temp
gatsbySoupPatch = soup2.find(id='___gatsby')
g2 = gatsbySoupPatch.find_all('a', attrs={'class': 'skins cboxElement'})

print(g2)