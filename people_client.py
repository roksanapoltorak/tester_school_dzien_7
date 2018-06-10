import hashlib
import requests

class PeopleClientError(Exception):
    pass

class PeopleClient():

    FIELDS = ('first_name', 'last_name', 'email', 'phone', 'ip_address')

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def get_all(self, limit=None):

        if limit is None:
            return requests.get(self.base_url).json()

        if limit <= 0:
            raise ValueError('Limit has to be positive.')

        response = requests.get(self.base_url, params={'_limit': limit})


        total_records = int(response.headers['X-Total-Count'])

        pages_count = total_records // limit

        if total_records % limit != 0:
            pages_count += 1
        people = response.json()

        for page in range(2, pages_count + 1):
            chunk = requests.get(self.base_url, params={'_limit': limit, '_page': page}).json()


            for person in chunk:
                people.append(person)     # to jest równe :  people.extend(chunk)
        return people

    def add_person(self, first_name, last_name, email, phone, ip_address):

        headers = {'Authorization': 'Bearer ' + self.token}
        person = {'first_name': first_name, 'last_name': last_name, 'email': email,
                      'phone': phone, 'ip_address': ip_address}
        response = requests.post(self.base_url, json=person, headers=headers)

        if not response.ok:
            raise PeopleClientError(response.json()['error'])

        return response.json()


    def person_by_id(self, person_id):

        url = self.base_url + person_id
        response = requests.get(url)

        if response.status_code == 404:
            raise PeopleClientError('User given is not found')
        elif not response.ok:
            raise PeopleClientError('Uknown error')
        return response.json()

    def query(self, **criteria):

        for key in criteria:
            if key not in self.FIELDS:
                raise ValueError('Unknown parameter ' + key)

        response = requests.get(self.base_url, params=criteria)
        return response.json()

    def people_by_partial_ip(self, partial_ip):

        ip_regexp = '^' + partial_ip
        response = requests.get(self.base_url, params={'ip_address_like': ip_regexp})
        return response.json()


if __name__ == '__main__':
    token = hashlib.md5('relayr'.encode('ascii')).hexdigest()
    client = PeopleClient('http://polakow.eu:3000/people/', token)

    new = client.people_by_partial_ip('21.211')
    print(new)



