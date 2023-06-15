#selection sort 
import time 
import numpy as np 

def selection_sort(ar):
    for i in range(len(ar)):
        min=i
        for j in range(i+1,len(ar)):
            if(ar[min]>ar[j]):
                min=j
        ar[i],ar[min]=ar[min],ar[i]

def mean(a):
    sum(a)/len(a)

def test():
    worst_lsit=[]
    best_list=[]
    avg_list=[]

    g_list_x=[]
    g_list_y=[]
    random_list=[]
    range_list=1500

  
    
    
    
            



