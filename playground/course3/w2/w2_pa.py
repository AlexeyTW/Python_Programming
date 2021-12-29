from bs4 import BeautifulSoup
import re

def parse(path_to_file):
	with open(path_to_file, 'r', encoding='utf-8') as file:
		data = BeautifulSoup(file.read(), 'lxml')
		soup = data.find(id="bodyContent")

		imgs_source = soup.find_all(name='img')
		img_count = len([img for img in imgs_source if int(img['width']) >= 200]) # RETURN

		headers_source = [h.text for h in soup.find_all(re.compile('h\d'))]
		headers_count = len([h for h in headers_source if str(h).startswith(('E', 'T', 'C'))]) # RETURN

		a_source = soup.find_all('a')
		a_list = []
		for i in a_source:
			a_list.append(count_siblings(i))
		a_max_len = sorted(a_list)[-1]

		#print(a.find_next_sibling())
		#print(a)
		#print(count_siblings(a))
	print(img_count, headers_count, a_max_len)


def count_siblings(a, c=1):
	count = c
	if a.find_next_sibling() is not None and a.find_next_sibling().name == 'a':
		count += 1
		a_next = a.find_next_sibling()
		return count_siblings(a_next, count)
	return count


parse('wiki/Stone_Age')