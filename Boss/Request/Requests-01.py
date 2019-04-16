# 引入requests库
import requests

r = requests.get("http://www.baidu.com")
# requests.get(url, params=None, **Kwargs)
# 构造一个向服务器请求资源的request的对象

s = r.status_code
print(s)
# 生成HTTP请求的状态码  200：访问成功   404：失败，无此文件

r.encoding = "utf-8"
# 从HTTP中header中猜测的响应内容编码形式

t = r.text
print(t)
# HTTP响应内容的字符串形式，即，url对应的页面内容

a = r.apparent_encoding
# 从内容中分析的响应内容编码形式（备选编码形式）

c = r.content
# HTTP响应内容的二进制形式



