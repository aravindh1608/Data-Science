#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
  
statecovid19data=pd.read_csv("https://api.covid19india.org/csv/latest/state_wise.csv") 
df = pd.DataFrame(statecovid19data)
df.to_csv(r'C:\Users\aravi\Downloads\filename.csv') 


# In[3]:





# In[ ]:




