import requests
import base64

headers = {'Authorization': 'Basic YWxsYWRpbjpvcGVuc2VzYW1l'}

request1 = requests.post('https://datasend.webpython.graders.eldf.ru/submissions/1/', headers=headers)

print(request1.json())

headers2 = {'Authorization': 'Basic YWxpYmFiYTo0MHJhemJvaW5pa292'}
request2 = requests.put('https://datasend.webpython.graders.eldf.ru/submissions/secretlocation/', headers=headers2)

print(request2.text)