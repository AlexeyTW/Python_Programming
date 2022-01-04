from bs4 import BeautifulSoup
import re
import os

def parse(path_to_file):
	with open(path_to_file, 'r', encoding='utf-8') as file:
		data = BeautifulSoup(file.read(), 'lxml')
		soup = data.find(id="bodyContent")
		#print(soup)

		imgs_source = soup.find_all(name='img')
		imgs = len([img for img in imgs_source if img.has_attr('width') and int(img['width']) >= 200])

		headers_source = [h.text for h in soup.find_all(re.compile('h\d'))]
		headers = len([h for h in headers_source if str(h).startswith(('E', 'T', 'C'))])

		a_source = soup.find_all('a')
		a_list = []
		for i in a_source:
			a_list.append(count_siblings(i))
		linkslen = sorted(a_list)[-1]

		lists_source = [l for l in soup.find_all('ul')] + [l for l in soup.find_all('ol')]
		lists = count_parent_lists(lists_source)

	print(imgs, headers, linkslen, lists)


def count_siblings(a, c=1):
	count = c
	if a.find_next_sibling() is not None and a.find_next_sibling().name == 'a':
		count += 1
		a_next = a.find_next_sibling()
		return count_siblings(a_next, count)
	return count

def count_parent_lists(lists):
	count = 0
	for lst in lists:
		if lst.find_parent().name not in ['li', 'ul', 'ol']:
			count += 1
	return count

def filter_links(link: str):
	if link is not None and link.startswith('/wiki') and os.path.exists(link[1:]):
		return True

def build_bridge(path, start_page, end_page):
	#print(f'Start: {start_page}, end: {end_page}')
	route = [start_page]
	if start_page == end_page:
		return route
	with open(os.path.join(path, start_page), 'rb') as file:
		data = file.read()
		soup = BeautifulSoup(data, 'lxml')
		links = [i.get('href') for i in soup.find_all('a')]
		wiki_links = [i for i in filter(filter_links, links)]
		print(wiki_links)
		if end_page in wiki_links:
			route.append(end_page)
			return route
		for link in wiki_links:
			#build_bridge('wiki', link.split('/')[-1], end_page)
			print(link)

		print(route)
		#print([i for i in links if i is not None and filter_links(i)])




build_bridge('wiki', 'The_New_York_Times', 'Stone_Age')
#parse('wiki/Spectrogram')
#print(os.path.exists('wiki/London'))
