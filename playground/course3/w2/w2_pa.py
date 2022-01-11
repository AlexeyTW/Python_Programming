from bs4 import BeautifulSoup
import re
import os
import glob
import pickle

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
	if link is not None and link.startswith('/wiki') and os.path.exists('C:/Temp/' + link[1:]):
		return True


def build_bridge(path, start_page, end_page):
	graph = {}
	graph_map = {}
	c = 0
	for file in glob.glob(path + '*'):
		with open(os.path.join(path, file.split('\\')[-1]), 'rb') as source:
			file_data = source.read()
			name = source.name.split('/')[-1]
			soup = BeautifulSoup(file_data, 'lxml')
			links = [i.get('href') for i in soup.find_all('a')]
			wiki_links = list(set([i.split('/')[-1] for i in filter(filter_links, links)]))
			graph[name] = wiki_links
			graph_map[name] = c
			c += 1

	print(graph_map)
	print(graph)

	m = [[0 for j in range(len(graph))] for i in range(len(graph))]

	for key in graph.keys():
		for value in graph[key]:
			if key != value:
				m[graph_map[key]][graph_map[value]] = 1

	print(graph_map)
	print(graph)
	for i in range(len(m)):
		print(m[i], list(graph_map.keys())[i], i)


	def find_shortest_path(matrix, start_page, end_page, route=[]):
		route = route + [end_page]
		page_ind = graph_map[end_page]
		page_refs = [i for i in range(len(matrix)) if matrix[i][page_ind] == 1]
		matrix[page_ind] = [0 for i in range(len(matrix))]
		if graph_map[start_page] not in page_refs:
			for ref in page_refs:
				end_page = list(graph.keys())[ref]
				return find_shortest_path(matrix, start_page, end_page, route)
		return route

	route = find_shortest_path(m, start_page, end_page) + [start_page]

	return #route[::-1]


'''
	def find_shortest_path(graph, start, end, route):
		route = route + [start]
		if start == end:
			return route
		if start not in graph.keys():
			return None
		shortest = None
		for node in graph[start]:
			if node not in route:
				newpath = find_shortest_path(graph, node, end, route)
				#if newpath:
				if not shortest or len(newpath) < len(shortest):
					shortest = newpath
		return shortest
'''
PATH = 'C:/Temp/wiki/'

print(build_bridge(PATH, 'The_New_York_Times', 'Stone_Age'))
#parse('wiki/Wild_Arms_(video_game)')

