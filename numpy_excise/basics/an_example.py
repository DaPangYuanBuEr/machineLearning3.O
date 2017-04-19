'''
Created on 

@author: xiaoyuan
'''
from numpy import *

a = arange(15).reshape(3,5)
print(a)
print("numpy_shape:"+ str(a.shape))
print("numpy_ndim:"+str(a.ndim))
print("numpy_dtype.name:" + a.dtype.name)
print("numpy_itemsize:" + str(a.itemsize))
print("numpy_size:"+str(a.size))
print(type(a))

if __name__ == '__main__':
     pass





