import requests
import os

url = "http://image.ngchina.com.cn/2019/0203/20190203044147594.jpg"
root = "C:/Users/Administrator/Desktop/py"
path = root + "/" + url.split("/")[-1]
try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		r.raise_for_status()
		print(r.status_code)
		with open(path ,"wb") as f:
			f.write(r.content)
		f.close()
	else:
		print("文件已存在")
except:
	"error"



