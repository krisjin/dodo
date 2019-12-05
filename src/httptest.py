import requests

url = "http://172.25.223.55:8999"
path = "/usr/local/tools/a.txt"
print(path)
files = {'file': open(path, 'rb')}
r = requests.post(url, files =files)
print(r.url)
print(r.text)
