import requests

# r = requests.get("https://item.jd.hk/8314939.html")
# state = r.status_code
# # status_code 状态码
# r.encoding = "utf-8"
#

url = "https://item.jd.hk/8314939.html"

try:
	r = requests.get(url)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[:1000])
except:
	print("爬取失败")



