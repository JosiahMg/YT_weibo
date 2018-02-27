# -*- coding: utf-8 -*-


import numpy as np
from matplotlib import pyplot as plt

import sys


reload(sys)
sys.setdefaultencoding('utf8')


Y1 = [19,24,13,13,13,13,13]
Y2 = [22,17,12,9,13,9,7,5,2,5,7]

#plt.figure(figsize=(9,6))
n1 = len(Y1)
n2 = len(Y2)
X1 = np.arange(n1)+1
X2 = np.arange(n2)+1

XS1 = ['Mon.','Tues.','Wed.','Thur.','Fri.','Sat.','Sun.']
AXS1 = np.array(XS1)






plt.bar(X1,Y1,width = 0.35,facecolor = '#ff9999',edgecolor = 'white')
#plt.xlabel('星期',fontproperties='SimHei',fontsize=15)
#plt.ylabel('发微博天数',fontproperties='SimHei',fontsize=15)
plt.ylabel('发微博天数',fontproperties='SimHei',fontsize=10)
#plt.title('20170931',fontproperties='SimHei',fontsize=15)
plt.title('20180131',fontsize=15)

group_labels = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
plt.xticks(X1, group_labels, rotation=0,fontproperties='SimHei',fontsize=15)

for x,y in zip(X1,Y1):
    plt.text(x, y+0.05, '%d' % y, ha='center', va= 'bottom')
    
plt.show()

#plt.subplot(1,2,2)
plt.bar(X2,Y2,width = 0.35,facecolor = 'yellowgreen',edgecolor = 'white')

#plt.xlabel('月份',fontproperties='SimHei',fontsize=15)
#plt.ylabel('天数',fontproperties='SimHei',fontsize=15)

plt.ylabel('发微博天数',fontproperties='SimHei',fontsize=10)
#plt.title(r'截止日期7/31',fontproperties='SimHei',fontsize=20)
plt.title('2018-01-31',fontproperties='SimHei',fontsize=15)


group_labels = ['1703','04','05','06','07','08','09','10','11','12','01']
#plt.xticks(X2, group_labels, rotation=0,fontproperties='SimHei',fontsize=15)
plt.xticks(X2, group_labels,rotation=0,fontproperties='SimHei',fontsize=15)

for x,y in zip(X2,Y2):
    plt.text(x, y+0.05, '%d' % y, ha='center', va= 'bottom')

plt.show()




labels = ['Mon.','Tues.','Wed.','Thur.','Fri.','Sat.','Sun.']
sizes = Y1
explode = [0,0.05,0,0,0,0,0]

sum = 0
sizes_ratio = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

for i in range(len(sizes)):
    sum = sum + sizes[i]
    #print(sum)

for i in range(len(sizes)):
    sizes_ratio[i] = sizes[i]*1.0/sum
    #print(sizes_ratio[i])

tmp_ratio = sizes_ratio
tmp_ratio.reverse()
print(sizes_ratio)

tmp_lables = labels
tmp_lables.reverse()
print(tmp_lables)

tmp_explode = explode
tmp_explode.reverse()
print(tmp_explode)

plt.title(r'20171231',fontproperties='SimHei',fontsize=15)
plt.pie(tmp_ratio,explode=tmp_explode,labels=tmp_lables,autopct='%1.2f%%',shadow=False,startangle=180)
plt.show()


