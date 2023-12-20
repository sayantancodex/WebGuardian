from bs4 import BeautifulSoup
import requests

html = requests.get('http://testphp.vulnweb.com/artists.php')
soup = BeautifulSoup(html.content, 'lxml')

links = soup.find_all('a')

for link in links:
    href = link.get('href')
    if 'php?' in href:
        print(href)

print(html.text)