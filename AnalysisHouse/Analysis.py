#-*- coding: utf-8 -*-
import csv
import matplotlib.pyplot as plt
import re

#解决可视化图形中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

address=[]
count=[]
price=[]
priceaddress=[]
address1=[]
addressname=[]
addressnum=[]
SW=[]
WW=[]
QW=[]
JW=[]
TW=[]

#在文本中截到所需的价格与地点
with open('C:/Users/Administrator/Desktop/lianjia.csv',encoding='utf-8') as f:
    read_lianjia = csv.reader(f)
    for line in read_lianjia:
        if read_lianjia.line_num==1:
            continue
        numprice = line[2]
        result = re.findall(".*价(.*)元.*", numprice)
        for x in result:
          price.append(int(x))
        if line[3] not in address:
            address.append(line[3])
        priceaddress.append([line[3],int(x)])
price.sort(reverse=True)

#获取每个地区的名字与对应的出售数量,与每平方的价格
for i in range(len(address)):
    with open('C:/Users/Administrator/Desktop/lianjia.csv',encoding='utf-8') as f:
        sum = 0
        cout = 0
        read_lianjia = csv.reader(f)
        for j in read_lianjia:
           if j[3] == address[i]:
               sum=sum+1
        address1.append([address[i],sum])
address1.sort(key=lambda x:x[1],reverse=True)

#计算地区出售房屋数量
for i in range(len(address1)):
    if i<=10:
        addressname.append(address1[i][0])
        addressnum.append(address1[i][1])

#计算每个地区房价平均值
AVGaddress=[]
for i in range(len(address)):
    num = 1
    m = 0
    for j in range(len(priceaddress)):
            if priceaddress[j][0]==address[i]:
                num=num+1
                m=int(priceaddress[j][1])+int(m)
            avg=int(m)/int(num)
    AVGaddress.append([address[i],round(avg,1)])
AVGaddress.sort(key=lambda x:x[1],reverse=True)

#计算每个价格区间的房屋数量
for i in range(len(price)):
    if int(price[i])>10000 and int(price[i]) <=30000:
        SW.append('1')
    elif int(price[i]) > 30000 and int(price[i]) <= 50000:
        WW.append('1')
    elif int(price[i]) > 50000 and int(price[i]) <= 70000:
        QW.append('1')
    elif int(price[i]) > 70000 and int(price[i]) <= 90000:
        JW.append('1')
    elif int(price[i]) > 90000:
        TW.append('1')

#显示直方图数量函数
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.,1.02*height, '%s元' % int(height))
def autolabel1(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.,1.02*height, '%s' % int(height))

#出售房屋数量前十地区直方图
fig=plt.figure()
rects3=plt.bar(addressname,addressnum,color=('red','yellowgreen','lightskyblue','yellow','orange'))
autolabel1(rects3)
plt.xlabel('地区')
plt.ylabel('数量')
plt.title('出售房屋数量前十地区直方图')
plt.show()

#价格区间饼图
labels=['1万到3万','3万到5万','5万到7万','7万到9万','9万以上']
share=[len(SW),len(WW),len(QW),len(JW),len(TW)]
colors = ['red','yellowgreen','lightskyblue','yellow','orange']
labels1=[len(SW),len(WW),len(QW),len(JW),len(TW)]
plt.axes(aspect=1)
explode = [0, 0.1, 0, 0,0]
plt.pie(x=share, explode=explode,labels=labels, colors=colors,autopct='%3.1f %%',
        shadow=False, labeldistance=1.1, startangle=90, pctdistance=0.6)
plt.legend(fontsize=12,
           labels=labels1,
           title="个数图",
           bbox_to_anchor=(1, 0, 0.3, 1))
plt.title('价格区间饼图')
plt.show()

#每平米最贵前十地区
fig1=plt.figure(2)
address2=[]
avgPrice=[]
for i in range(len(AVGaddress)):
    address2.append(AVGaddress[i][0])
    avgPrice.append(AVGaddress[i][1])
rects=plt.bar(address2[0:9],avgPrice[0:9],color=('red','yellowgreen','lightskyblue','yellow','orange'),width=0.5)
autolabel(rects)
plt.xlabel('地区')
plt.ylabel('价格')
plt.title('每平米最贵前十地区')
plt.show()

#每平米最便宜前十地区
fig1=plt.figure(2)
address2=[]
avgPrice=[]
for i in range(len(AVGaddress)):
    address2.append(AVGaddress[i][0])
    avgPrice.append(AVGaddress[i][1])
rects2=plt.bar(address2[-9:],avgPrice[-9:],color=('red','yellowgreen','lightskyblue','yellow','orange'),width=0.5)
autolabel(rects2)
plt.xlabel('地区')
plt.ylabel('价格')
plt.title('每平米最便宜前十地区')
plt.show()

