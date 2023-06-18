import requests

from config import api_host

if __name__ == '__main__':
    users = requests.get(f'{api_host}/users')
    print(users.json())
