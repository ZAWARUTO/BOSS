import requests

url = "http://www.baidu.com"

try:
	kv = {"user-agent" : "Mozilla/5.0"}
	r = requests.get(url , headers = kv)
	# 修改request中的客户端代理头，将爬虫修改为Mozilla,否则会被服务器拒绝访问
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.request.headers)
except:
	print("设置错误")

