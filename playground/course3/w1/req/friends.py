import requests

token = '4240476e4240476e4240476ebb423ade78442404240476e2384a22b753f658a431e8153'
userid = 'id2224960'
url = f'https://api.vk.com/method/users.get'
payload = {"v":"5.81",
           "access_token":"4240476e4240476e4240476ebb423ade78442404240476e2384a22b753f658a431e8153",
           "user_ids": "id2224960",
           "fields": "bdate"}

r = requests.get(url, params=payload)

print(r.url)
print(r.text)