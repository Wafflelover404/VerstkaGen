import requests

def check_internet():
    url = "http://www.google.com"
    timeout = 5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False

if __name__ == "__main__":
    if check_internet():
        print("Internet connection is active")
    else:
        print("No internet connection available")