import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,10])
print("Original array:\n",arr)

newarr=arr.reshape(2,5)
print("\nReshaped array:\n",newarr)

a=np.array([10,10,10,10,10])
print("\nSecond array:\n",a)

print("\nAdd the two arrays:\n",np.add(newarr,a))