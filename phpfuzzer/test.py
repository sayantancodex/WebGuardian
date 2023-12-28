from bs4 import BeautifulSoup
import requests

def phpfuzzer(universal_link):

    html = requests.get(universal_link)
    soup = BeautifulSoup(html.content, 'lxml')

    links = soup.find_all('a')

    for link in links:
        href = link.get('href')
        if 'php?' in href:
            phpfuzz = universal_link+href
            print(phpfuzz)

# print(html.text)
universal_link = "http://testphp.vulnweb.com/artists.php"
phpfuzzer(universal_link)