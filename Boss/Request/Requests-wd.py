import requests

kv = {"wd" : "python"}

try:
	r = requests.get("http://www.baidu.com/s" , params = kv)
	r.raise_for_status()

	print(len(r.text))
except:
	"chucuo"