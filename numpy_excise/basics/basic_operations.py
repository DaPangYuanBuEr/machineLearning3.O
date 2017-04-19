'''
Created on 2017年4月19日

@author: xiaoyuan
'''
from numpy import *

a=array([20,30,40,50])
b=arange(4)

c=a-b
print(c)


d = b**2
print(d)

e= 10*sin(a)
print(e)


f=a<35
print(f)


g=array([[1,1],[0,1]])
h=array([[2,0],[3,4]])
#计算内积
i=g*h
print(i)

#计算矩阵
j=dot(g,h)
print(j)


k=ones((2,3),dtype=int)
l=random.random((2,3))
k *= 3
print(k)
l += k
print(l)


m=random.random((2,3))
print(a.sum())
print(a.min())
print(a.max())

#axis＝0表示按列，axis＝1表示按行的方向
n=arange(12).reshape(3,4)
o=n.sum(axis =0)
print(o)
p=n.min(axis =1)
print(p)





