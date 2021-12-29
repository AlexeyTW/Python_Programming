from bs4 import BeautifulSoup
import re

def parse(path_to_file):
	with open(path_to_file, 'r', encoding='utf-8') as file:
		data = BeautifulSoup(file.read(), 'lxml')
		soup = data.find(id="bodyContent")
		imgs_source = soup.find_all(name='img')
		img_count = len([img for img in imgs_source if int(img['width']) >= 200])
		headers_source = [h.string for h in soup.find_all(re.compile('^h\d'))]
		headers_count = [h for h in headers_source if str(h).startswith(('E', 'T', 'C'))]
		print(soup.find(id="Early_Stone_Age_(ESA)").string)
		#print(soup)


parse('wiki/Stone_Age')