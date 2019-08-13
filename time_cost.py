
# coding: utf-8

# In[2]:


import random
import math
import numpy as np

def time_cost_calc(stack,top_val1,neighbor_nodes,l):
    key=0
    dup=0
    length=0
    top_val2=top_val1
    time=1
    test=0
#     print (str(top_val1))
    while(test<100):      #(not(top_val1==-1 and top_val2==(l-1))):
        if(top_val1==-1):
            top_val1=top_val2
#             print(stack)
#             print(top_val1)
            time=time+1
            test=test+1
            if(top_val1+1==l):
                break
        else:
            key=int(stack[top_val1])
            length=len(neighbor_nodes[key-1])
            for i in range(length):
                for j in range(top_val2+1):
                    if(neighbor_nodes[key-1][i]==stack[j]):
                        dup=1
                        break
                    else:
                        dup=0
                    
                if(dup==0):
                    top_val2=top_val2+1
                    stack[top_val2]=neighbor_nodes[key-1][i]
            top_val1=top_val1-1
#     print ""
    return(time)
    

