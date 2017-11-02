# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:25:01 2017

@author: s174393
"""

def dataStatistics(data,statistics):
    if statistics == "Mean Temperature":
        result=np.mean(data[:,0])
    elif statistics == "Mean Growth rate":
        result=np.mean(data[:,1])
    elif statistics == "Std Temperature":
        result=np.std(data[:,0])
    elif statistics == "Std Growth rate":
        result=np.std(data[:,1])
    elif statistics == "Rows":
        result=len(data)
    elif statistics == "Mean Cold Growth rate":
        if data[:,0]<20:
            result=np.mean(data[:,1])
    elif statistics == "Mean Hot Growth rate":
        if data[:,0]>50:
            result=np.mean(data[:,1])
    return result