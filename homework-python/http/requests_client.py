import requests


base = "http://127.0.0.1:5000"

url = base + "/page"
print("requesting {}".format(url))
response = requests.get(url)
print("response:")
print(response)
print("response text:")
print(response.text)
print("response status_code:")
print(response.status_code)
print("response json:")

try:
    js = response.json()
    print(js)
    print("type: ", type(js))
except:
    print("NO JSON")
