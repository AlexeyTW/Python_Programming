from bs4 import BeautifulSoup
import requests
url = 'http://help.websiteos.com/websiteos/example_of_a_simple_html_page.htm'
html = requests.get(url)

soup = BeautifulSoup(html.text, 'lxml')
tags = soup('a', 'extiw')
#print([tag['href'] for tag in tags])
#print([tag.name for tag in soup.script.parents])
print(list(soup.script.children))
