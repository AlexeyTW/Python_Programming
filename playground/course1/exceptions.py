import requests, sys
from requests import exceptions

url = sys.argv[1]

try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
except requests.Timeout:
    print('Timeout error, url: {}'.format(url))
except requests.HTTPError as err:
    code = err.response.status_code
    print('URL is incorrect: {0}. Code: {1}'.format(url, code))
except requests.RequestException:
    print('Download error. URL: {}'.format(url))
else:
    print(response.content)