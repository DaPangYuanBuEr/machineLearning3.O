'''
Created on 2017年4月19日

@author: xiaoyuan
'''

from numpy import *
#创建1维数组
a = array([2,3,4])
print (a)
print (a.dtype)

#通过zeros创建0元素
b=zeros((3,4))
print(b)

#通过ones创建1元素
c=ones((2,3,4),dtype=int16)
print(c)

#通过arange创建10-30步长为5的数组
d= arange(10,30,5)
print(d)

#通过设置元素个数创建数组
e = linspace(0,2,9)
print(e)

#创建空元素数组，默认按照磁盘的记忆中读取
f = empty((2,3))
print(f)



