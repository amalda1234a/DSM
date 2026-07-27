#!/usr/bin/env python
# coding: utf-8

# In[8]:


a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number"))
ch=int(input("enter your choice"))
if(ch==1):
 sum=a+b
 print(sum)
elif(ch==2):
 sub=a-b
 print(sub)
elif(ch==3):
 mul=a*b
 print(mul)
elif(ch==4):
 div=a/b
 print(div)
else:
    print("invalid")


# In[16]:


a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number"))
print(a and b==5)
print(a==5 or b==5)
print(a>=b)
print(a<=b)
print(a>b)
print(a<b)


# In[29]:


dict1 = {"roll":4,"name":"amalda","age":22}
dict2 = {"place":"kozhikode","phn":9778508986}
dict1.update(dict2)


# In[32]:


print (dict1)


# In[36]:


a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number"))
c=int(input("enter the 3rd number:"))
if (a>b and a>c):
    print (a)
elif (b>a and b>c):
    print(b)
elif (c>a and c>b):
    print(c)


# In[51]:


a = [5,6,7,4]
print(a)
a.append(3)
print(a)
a.remove(3)
print(a)
a.pop(2)
a.insert(3,9)
print(a)
b=a.copy()
print(b)


# In[ ]:




