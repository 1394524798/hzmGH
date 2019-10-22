import requests
from  bs4 import  BeautifulSoup
import csv
address=()
#headers可以在网页打开F12后查找，具体按ctrl+o，如果不请求回返回403，拒绝访问
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'
}
#先给csv加上索引
def setcsv():
    with open('C:/Users/Administrator/Desktop/lianjia.csv', 'a', encoding='utf-8-sig') as file:
        house_csv = csv.writer(file)
        house_csv.writerow(["标题", "总价格(万)", "单价", "地点", "基础信息", '关注数与发布时间'])

#获取网页源码
def getHTMLtext(url):
    html=requests.get(url,headers=headers).content
    html=html.decode('utf-8')
    return html
#提取数据
def get_data(html):
    soup=BeautifulSoup(html,"html.parser")
    # 在网页找到数据所在的标签，然后提取出来
    infos=soup.find('ul',{ 'class':"sellListContent"}).find_all('li')
    with open('C:/Users/Administrator/Desktop/lianjia.csv','a',encoding='utf-8-sig') as file:
         # file.write('标题, 总价格, 单价, 地点, 基础信息,关注数与发布时间')
         for i in infos:
            #获取每个房子的标题
            title = i.find('div',{'class':'title'}).find('a').get_text()
            #获取每个房子的价格
            priceinfo=i.find('div',{'class':'priceInfo'}).find('div',{'class':'totalPrice'}).find('span').get_text()
            price=i.find('div',{'class':'priceInfo'}).find('div',{'class':'unitPrice'}).find('span').get_text()
            #获取房子的地址
            address=i.find('div',{'class':'flood'}).find_all('a')
            #获取房子的信息
            houseInfo=i.find('div',{'class':'houseInfo'}).get_text()
            #获取房子的发布日期与关注人数
            followInfo=i.find('div',{'class':'followInfo'}).get_text()
            for j in address:
                address=j.get_text()
            #打印检查
            # print('{},{},{},{},{},{}\n'.format(title,priceinfo,price,address,houseInfo,followInfo))
            #写入csv
            file.write('{},{},{},{},{},{}\n'.format(title,priceinfo,price,address,houseInfo,followInfo))
#主函数
def main():
    j=1
    num=10
    #用来自动翻页，num是页数
    for i in range(num):
        url= 'https://sh.lianjia.com/ershoufang/pg' + str(j)+'/'
        html=getHTMLtext(url)
        get_data(html)
        j=j+1
setcsv()
main()
