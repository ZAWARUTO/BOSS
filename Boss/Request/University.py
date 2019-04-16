import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url , timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("error")


def fillUiveList(ulist,html):
    soup = BeautifulSoup(html , "html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr , bs4.element.Tag):
            tds = tr("td")
            ulist.append([tds[0].string , tds[1].string , tds[2].string])


def printUniveList(ulist,num):
    print("{:^10}\t{:^6}".format("排名" , "学校" ))
    for i in range(num):
        item = ulist[i]
        print("{:^10}\t{:^6}".format(item[0],item[1]))

def main():
    uinfo = []
    url = "http://www.zuihaodaxue.cn/ARWU2018.html"
    html = getHTMLText(url)
    fillUiveList(uinfo , html)
    printUniveList(uinfo , 20)

if __name__ == '__main__':
    main()