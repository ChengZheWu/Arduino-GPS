#!/usr/bin/env python
# coding: utf-8

# In[1]:


p1 = [121.5424246, 25.0173750]    
p2 = [121.5435203, 25.0177875]


# In[2]:


from math import radians, cos, sin, asin, sqrt
 
def dis(lon1, lat1, lon2, lat2): 
    
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # 地球平均半徑
    return c * r * 1000


# In[3]:


d = dis(p1[0], p1[1], p2[0], p2[1])
#print(d)


# In[4]:


dif_lon = round(p2[0] - p1[0], 9)
dif_lat = round(p2[1] - p1[1], 9)
#print('精度差:',dif_lon)
#print('緯度差:',dif_lon)
rp_lon = round((dif_lon / 12), 8) # 走一分鐘，60秒，5秒一個點，12個點
rp_lat = round((dif_lat / 12), 8)
#print(rp_lon)
#print(rp_lat)
dif = [rp_lon, rp_lat]
#print(dif)


# In[ ]:


import time

for i in range(13):
    print('%.7f, %.7f' %(p1[0], p1[1]))
    p1 = [sum(x) for x in zip(p1, dif)]
    time.sleep(5)


# In[ ]:




