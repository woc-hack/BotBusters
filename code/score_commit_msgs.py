
# coding: utf-8

# In[93]:


import pandas as pd 
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
import numpy as np


# In[2]:


commit_content = pd.read_csv('commit_content', 
                             encoding='iso-8859-15', 
                             sep=';', 
                             header=None, 
                             names=['sha','name','time', 'commit_msg'])


# In[44]:


#commit_content.to_pickle('commit_content.pickle')


# In[45]:


res = commit_content.groupby('name')['commit_msg'].unique().reset_index()


# In[197]:


def score_row(row):
    #print(row)
    score_list = []
    for n in range(len(row)):
        if len(row) > 1: 
            exclude = np.delete(row,n)
            exclude

            scores = pd.DataFrame(process.extract(row[n],exclude))
            scores.columns = ['message','score']
            score_list.append(scores.score.mean())

        return(np.mean(score_list))


# In[203]:


subset = res.iloc[0:100]
subset['score'] = subset['commit_msg'].apply(lambda x: score_row(x))


# In[210]:


print(subset['score'][1])
subset['commit_msg'][1]


# In[211]:


print(subset['score'][5])
subset['commit_msg'][5]


# In[212]:


print(subset['score'][88])
subset['commit_msg'][88]


# In[216]:


subset.sort_values('score', ascending=False)


# In[214]:


print(subset['score'][38])
subset['commit_msg'][38]


# In[215]:


print(subset['score'][49])
subset['commit_msg'][49]


# In[217]:


print(subset['score'][90])
subset['commit_msg'][90]

