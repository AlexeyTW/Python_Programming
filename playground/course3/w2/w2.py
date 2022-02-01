from bs4 import BeautifulSoup
import requests
import re


url = 'http://help.websiteos.com/websiteos/example_of_a_simple_html_page.htm'
text = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Hello, World! - Learn HTML - Free Interactive HTML Tutorial</title>
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://www.learn-html.org/" />
    <meta property="og:image" content="https://www.learn-html.org/static/img/share-logos/learn-html.org.png" />
    <link rel="stylesheet" type="text/css" href="/static/css/prism-dark.css"/>
    <link rel="stylesheet" type="text/css" href="/static/css/learnpython.css"/>

    <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
    <body class='body' id='js-body'>
   		<p class='text odd'>first <b>bold</b> paragraph</p>>
		<p class='text even'>second <a href='https://mail.ru'>link</a></p>>
		<p class='list odd'>third <a id='paragraph'><b>bold link</b></a></p>>
	</body>
	 <script >
    </script>
</head>
</body>
</html>
'''

soup = BeautifulSoup(text, 'lxml')

#print([i['href'] for i in soup('link')])
#print(soup.b.find_parent('body')['id'])
#print(soup.p.find_next_siblings())
#print(soup.p.contents)
#print(list(soup.p.children))
#print(soup.p.find('b'))
#print(soup.find(id='js-body')['class'])
print(soup.find('b', text='bold'))
#print(soup.find_all('p'))
#print(soup.find_all('p', 'text odd'))
#print(soup.select('p.odd.text'))
#print(soup.select('p:nth-of-type(3)'))
#print(soup.select('a > b'))
#print([i.name for i in soup.find_all(re.compile('^b'))])
#print([i for i in soup(['a', 'b'])])
'''tag = soup.b
tag.name = 'i'
tag['id'] = 'myid'
tag.string = 'italic'
print(soup)'''