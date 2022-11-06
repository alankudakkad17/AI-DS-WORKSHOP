#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
a=np.array([[1,2,3],[5,6,7]])
print(a)
print(type(a))


# In[22]:


import numpy as np
j=np.array([1,2,8,9],dtype='i')
print(j.dtype)


# In[8]:


import numpy as np
a=np.array([[[1,2,3,],[4,5,6]],[[7,8,9],[3,4,5]]])
print(a)
print(type(a))


# In[34]:


import numpy as np 
a=np.array([1,2,3])
b=np.array([[1,2,3],[3,4,5]])
c=np.array([[[1,2,3,],[2,3,4]],[[3,4,5],[3,4,5]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(b[0,0])
print(c[0,1,2])
print(b[0,0:])
print(c.shape)


# In[26]:


import numpy as np
arr=([1,2,3,4,5,6,7])
print(arr[4:])


# In[39]:


import  numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x=a.copy()
y=a.view()
a[0]=42
print(a)
print(x)
print(y)
newarr=a.reshape(4,3)
print(newarr)
#flatterning
n=newarr.reshape(-1)
print(n)


# In[42]:


import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
for x in arr:
    print(x)
for x in arr:
    for y in x:
        print(y)


# In[43]:


c=np.array([[[1,2,3,],[2,3,4]],[[3,4,5],[3,4,5]]])
for x in np.nditer(c):
    print(x)


# In[46]:


av1=np.array([1,2,3])
av2=np.array([5,6,7])
avv=np.concatenate((av1,av2))
print(avv)


# In[6]:


import numpy as np
a=np.array([1,2,3,4,5,4,4])
x=np.where(a==4)
print(x)


# In[13]:


import numpy as np
arr=np.array([6,9])
x=np.searchsorted(arr,3)
print(x)


# In[15]:


import numpy as np
a=np.array([7,8,3,4,5,1,4])
print(np.sort(a))


# In[17]:


import numpy  as np
a=np.array(["basil","tom","alan","pakkaran love franki"])
print(np.sort(a))


# In[22]:


import numpy as np
arr=np.array([[3,2,1],[5,0,1]])
x=np.sort(arr)
print(x)


# In[26]:


from numpy import random
x=random.randint(100,size=(5))
y=random.randint(100,size=(5,3))
print(x)
print(y)


# In[29]:


from numpy import random
x=random.choice([3,5,6,7],p=[0.1,0.3,0.6,0.0],size=(100))
print(x)


# In[ ]:




