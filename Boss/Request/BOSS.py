import requests
import os

def GetContent(url,root,path,agent):
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):

            r = requests.get(url, timeout=30, headers=agent)
            print(r.status_code)
            r.raise_for_status()
            r.encoding = "utf-8"
            with open(path ,"wb") as f:
                f.write(r.content)
            f.close()
        else:
            print("文件已存在")
    except:
        print("error")

def AutoDownlord(filename):
    page = 100000
    # page += 1
    agent = {"user-agent" : "Mozilla/5.0"}
    url = "https://www.zhipin.com/c101270100-p100101/?page=" + page.__str__() + "&ka=page-" + page.__str__()

    # url = "https://www.zhipin.com/c101270100-p100101/?page=1&ka=page-1"  JAVA
    # url = "https://www.zhipin.com/c101270100-p100901/?page=2&ka=page-2"  WEB
    # url = "https://www.zhipin.com/c101270100-p100101/?page=2&ka=page-2"
    root = "C:/Users/Administrator/Desktop/py/resource/" + filename
    path = root + "/" + page.__str__() + ".html"
    GetContent(url, root, path, agent)

def OrderHTML():
	print("1")

AutoDownlord("java")