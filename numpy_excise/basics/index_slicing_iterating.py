'''
Created on 2017年4月19日

@author: xiaoyuan
'''
from numpy import *

#一维数组索引、切片、迭代
a=arange(10) **3
print(a[2])
print(a[2:5])
#从索引值为0到6的元素，每间隔两个设置1000
a[:6:2]=-1000
print(a)