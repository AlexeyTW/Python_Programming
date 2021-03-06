from bs4 import BeautifulSoup
import re
import os
import glob

def parse(path_to_file):
	with open(path_to_file, 'r', encoding='utf-8') as file:
		data = BeautifulSoup(file.read(), 'lxml')
		soup = data.find(id="bodyContent")

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

	return [imgs, headers, linkslen, lists]


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
		if ('li' or 'ul' or 'ol') not in [i.name for i in lst.find_parents()]:
			count += 1
	return count

def filter_links(link: str):
	if link is not None and link.startswith('/wiki') and os.path.exists(link[1:]):
		return True

def build_bridge(path, start_page, end_page):
	def find_shortest_path(graph, start, end):
		dist = {start: [start]}
		route = [start]
		while len(route):
			at = route.pop(0)
			for next in graph[at]:
				if next not in dist:
					dist[next] = [dist[at], next]
					route.append(next)
		result = dist.get(end)
		return str(result).replace('[', '').replace(']', '').replace("'", '').split(', ')

	return find_shortest_path(graph, start_page, end_page)

def get_statistics(path, start_page, end_page):
	stats = {}
	pages = build_bridge(path, start_page, end_page)
	for page in pages:
		stats[page] = parse(path + page)
	return stats

path = '/grader/nar4I/tests/wiki/'

graph = {}
file_names = [i.split('\\')[-1] for i in glob.glob(path[1:] + '*')]
for name in file_names:
	with open(os.path.join(path[1:], name), 'rb') as source:
		file_data = source.read()
		soup = BeautifulSoup(file_data, 'lxml')
		links = [i.get('href') for i in soup.find_all('a')]
		wiki_links = list(set([i.split('/')[-1] for i in filter(filter_links, links)
							   if i.split('/')[-1] in file_names and i.split('/')[-1] != name]))
		graph[name] = wiki_links

print(build_bridge(path='/grader/nar4I/tests/wiki/', start_page='Stone_Age', end_page='Python_(programming_language)'))