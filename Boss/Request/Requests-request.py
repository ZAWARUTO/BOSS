import requests



def __request__(method,url,**kwargs):
    requests.request(method,url,**kwargs)
    # method:"post","get",
    # url:"http://www.baidu.com"
    # params:      kv = {"key":"value"}    字典或者字节序列,作为参数增加到url中


kv = {"key": "value"}
r = requests.request("GET","http://www.baidu.com",params = kv)
print(r.url)  #http://www.baidu.com/?key=value


