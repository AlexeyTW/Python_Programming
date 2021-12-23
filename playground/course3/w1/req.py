import requests
import json

url = 'http://httpbin.org/'

#r = requests.get(url + 'get')
#r = requests.post(url + 'post')

payload = {'key1': 'value1', 'k2': 'v2'}

r = requests.get(url + 'get', params=payload)
print(r.url)

#r = requests.put(url + 'put', data={'k1': 'v1'})

#r = requests.post(url + 'post', json={'k1': 'v1'})

#files = {'txtfile': ('text.txt', open('text.txt', 'r'))}

#r = requests.post(url + 'post', files=files)

#headers = {'user-agent': 'my-app/1.1.1'}

#r = requests.get(url + 'get', headers=headers)

#r = requests.get(url + 'get')

#r = requests.get('http://github.com', allow_redirects=False)

#cookies = dict(cookies_are='working')
#r = requests.get(url + 'cookies', cookies=cookies)

s = requests.Session()
s.get(url + 'cookies/set/sessioncookie/12345')
r = s.get(url + 'cookies')

#print(s.cookies)
#print(r.text)
