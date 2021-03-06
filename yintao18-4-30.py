# -*- coding: utf-8 -*-
# Create Time : 2018-05-04
# Author : JosiahMg
# Env : python3.6

import numpy as np
from matplotlib import pyplot as plt

# for python2.7
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

#week 1-7
week_count = [20, 26, 15, 15, 15, 13, 14]

#month 1703-.
month_count = [22, 17, 12, 9, 13, 9, 7, 5, 2, 5, 7, 5, 2, 3]


week_index = np.arange(len(week_count))+1
month_index = np.arange(len(month_count))+1

AXS1 = np.array(['Mon.', 'Tues.', 'Wed.', 'Thur.', 'Fri.', 'Sat.', 'Sun.'])

# 画每周统计的个数
plt.bar(week_index, week_count, width=0.35, facecolor='#ff9999', edgecolor='white')
plt.ylabel('发微博天数', fontproperties='SimHei', fontsize=10)
plt.title('20180430', fontsize=15)
group_labels = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
plt.xticks(week_index, group_labels, rotation=0, fontproperties='SimHei', fontsize=15)
for x, y in zip(week_index, week_count):
    plt.text(x, y+0.05, '%d' % y, ha='center', va='bottom')
plt.show()


# 画每个月统计的个数
plt.bar(month_index, month_count, width = 0.35, facecolor='yellowgreen', edgecolor='white')
plt.ylabel('发微博天数', fontproperties='SimHei', fontsize=10)
plt.title('2018-04-30', fontproperties='SimHei', fontsize=15)
group_labels = ['17年03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '01', '02', '03', '04']
plt.xticks(month_index, group_labels, rotation=0, fontproperties='SimHei', fontsize=15)
for x, y in zip(month_index, month_count):
    plt.text(x, y+0.05, '%d' % y, ha='center', va= 'bottom')
plt.show()

# 画每周的饼状图
labels = ['Mon.', 'Tues.', 'Wed.', 'Thur.', 'Fri.', 'Sat.', 'Sun.']
sizes = week_count
explode = [0, 0.05, 0, 0, 0, 0, 0]
sum = 0
sizes_ratio = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

for i in range(len(sizes)):
    sum = sum + sizes[i]

for i in range(len(sizes)):
    sizes_ratio[i] = sizes[i]*1.0/sum

tmp_ratio = sizes_ratio
tmp_ratio.reverse()
print(sizes_ratio)

tmp_lables = labels
tmp_lables.reverse()
print(tmp_lables)

tmp_explode = explode
tmp_explode.reverse()
print(tmp_explode)

plt.title(r'20180430', fontproperties='SimHei', fontsize=15)
plt.pie(tmp_ratio, explode=tmp_explode, labels=tmp_lables, autopct='%1.2f%%', shadow=False, startangle=180)
plt.show()


# 画每个月统计的个数
plt.bar(month_index, month_count, width = 0.35, facecolor='yellowgreen', edgecolor='white')
plt.ylabel('发微博天数', fontproperties='SimHei', fontsize=10)
plt.title('2018-04-30', fontproperties='SimHei', fontsize=15)
group_labels = ['17年03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '01', '02', '03', '04']
plt.xticks(month_index, group_labels, rotation=0, fontproperties='SimHei', fontsize=15)
for x, y in zip(month_index, month_count):
    plt.text(x, y+0.05, '%d' % y, ha='center', va= 'bottom')
plt.show()
