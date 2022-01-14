from bs4 import BeautifulSoup
import re
import os
import time

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

def filter_links(link):
	i = link.get('href')
	if i is not None and i.startswith('/wiki'):
		return True

def build_bridge(path, start_page, end_page):
	t1 = time.time()
	print(f'Start building graph: {t1}')
	graph = {}
	file_names = os.listdir(path)
	for name in file_names:
		with open(os.path.join(path, name), 'r', encoding='utf-8') as source:
			file_data = source.read()
			soup = BeautifulSoup(file_data, 'lxml')
			#links = set(re.findall(r"(?<=/wiki/)[\w()]+", str(soup)))
			links = set([i.get('href').split('/')[-1] for i in filter(filter_links, soup.find_all('a'))])
			wiki_links = [i for i in links if i in file_names]
			graph[name] = wiki_links
	print(f'Graph building time: {time.time() - t1}')

	def find_shortest_path(graph, start, end):
		t2 = time.time()
		print(f'Start finding path: {t2}')
		dist = {start: [start]}
		route = [start]
		while len(route):
			at = route.pop(0)
			for next in graph[at]:
				if next not in dist:
					dist[next] = [dist[at], next]
					route.append(next)
		result = dist.get(end)
		print(f'Path is found for: {time.time() - t2} seconds')
		return str(result).replace('[', '').replace(']', '').replace("'", '').split(', ')

	return find_shortest_path(graph, start_page, end_page)
	#return graph

def get_statistics(path, start_page, end_page):
	stats = {}
	pages = build_bridge(path, start_page, end_page)
	for page in pages:
		stats[page] = parse(path + page)
	return stats
#print(build_bridge(path='grader/nar4I/tests/wiki/', start_page='Stone_Age', end_page='Python_(programming_language)'))

t1 = time.time()
print(build_bridge(path='wiki/', start_page='Stone_Age', end_page='Python_(programming_language)'))
#print(get_statistics('wiki/', 'The_New_York_Times', "Binyamina_train_station_suicide_bombing"))
t2 = time.time()
print(t2 - t1)