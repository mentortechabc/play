import time

import requests

if __name__ == '__main__':
    while True:
        r = requests.get("http://localhost:5000/")
        r.raise_for_status()
        print(r.text)
        time.sleep(1)
        print(time.time())