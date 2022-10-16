#To save the array
import numpy as np
arr=np.arange(10)
print(arr)
np.save('saved_array',arr)

#Load a single array
load_array=np.load('saved_array.npy')
print(load_array)

#saving and loading multiple array

arr2=np.arange(25)
arr3=np.arange(5)
np.savez('saved_archive.npz',x=arr2,y=arr3)

load_npz=np.load('saved_archive.npz')
print(load_npz['x'])
print(load_npz['y'])
