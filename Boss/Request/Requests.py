import requests

r = requests.head("http://www.baidu.com")
print(r.headers)

payload = {"key":"value"}

p = requests.post("http://httpbin.org/post" , data = payload)
print(p.text)