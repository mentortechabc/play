import os
import sys
import time
import traceback

import requests

if __name__ == '__main__':
    host = os.environ.get('TARGET_HOST')
    if not host:
        raise RuntimeError("Unable to get target host from the environment variables.")
    print(f"using host {host}")
    while True:
        try:
            r = requests.get(f"http://{host}:5000/")
            r.raise_for_status()
        except Exception:
            print("failed.")
            print(traceback.format_exc())
        else:
            print("response json", r.json())
            print(time.time())
        time.sleep(1)
        sys.stdout.flush()  # to force showing the output in the docker-compose