import requests

res = requests.get("http://127.0.0.1:5010/get/").json()
print(res)