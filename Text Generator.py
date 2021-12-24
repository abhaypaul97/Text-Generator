#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Markov chain 
## Probabilistic model generates sequence with high probability


# In[1]:


def generateTable(data, k=4):
    T={}
    for i in range(len(data)-k):
        x = data[i:i+k]
        y = data[i+k]

        if T.get(x) is None:
            T[x] ={}
            T[x][y]=1
        else:
            if T[x].get(y) is None:
                T[x][y]=1
            else:
                T[x][y] +=1
    return T


# In[2]:


T= generateTable ('hello hello helli helly')


# In[3]:


T
## Transition Table


# In[6]:


def convertFreqIntoProb(T):
    for kx in T.keys():
        s= sum(T[kx].values())
        for k in T[kx].keys():
            T[kx][k] = T[kx][k]/s
            
    return T


# In[8]:


T= convertFreqIntoProb(T)


# In[9]:


T


# In[10]:


# Read our data


# In[12]:


def load_text(filepath):
    with open(filepath) as f:
        return f.read().lower()


# In[14]:


def trainMarkovChain (text, k=4):
    T= generateTable(text,k)
    T= convertFreqIntoProb(T)
    return T


# # Generate Text

# In[19]:


import random


# # Next Letter Generation

# In[16]:


def sample_next ( context, T, k):
    context= context[-k:]
    
    if T.get(context) is None:
        retrun " "
    possible_chars list(T.get(context).keys())
    possible_proabs= list(T.get(context).values())
    return randonchoices(possible_chars, weights=possible_proabs)[0]


# # Next N(user input) letter generation 

# In[18]:


def generateText(starting_sen,T,k=4,maxLen=100):
    sentence = starting_sent
    context = starting_sent[-k:]
    
    
    for i in range(maxLen):
        sample_next(context,T,k)
        sentenct += next_pred
        context= sentence[-k:]
    return sentence


# In[ ]:




