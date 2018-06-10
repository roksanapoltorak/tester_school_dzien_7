import hashlib
import requests

BASE_URL = 'http://polakow.eu:3000/people/'

response = requests.get(BASE_URL, params={'_limit': 3, '_page': 2})
print(response.json())

print(response.text)

print(response.headers)

print(response.status_code)

print(response.headers['X-Total-Count'])  #liczba wszystkich rekordów

md5 = hashlib.md5('relayr'.encode('ascii'))

token = md5.hexdigest()

print(token)

headers = {'Authorization': 'Bearer ' + token}
person = {'first_name': 'Janusz', 'last_name': 'Cebularz', 'email': 'janusz.cebularz@op.pl', 'phone': '456 456 456', 'ip_address': '951.85.955.5'}
response = requests.post(BASE_URL, json=person, headers=headers)
print(response.json())

url = BASE_URL + 'Fzu5Uf6'
print(requests.get(url).json())

print(requests.get(BASE_URL, params={'id': 'Fzu5Uf6'}).json())

cebularze = requests.get(BASE_URL, params={'last_name': 'Cebularz', 'first_name': 'Michas'}).json()

print(cebularze)

response= requests.get(BASE_URL, params={'first_name': 'dhwhfwbfuw'})
if not response.json():
    print('No such people')

response = requests.get(BASE_URL, params={'email_like': '@gmail.com'})
print(response.json())