# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:25:00 2017

@author: s174420
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from cycler import cycler

mpl.style.use('ggplot') #Use a prettier plot

def dataPlot(data):
    
    #Plot "Number of bacteria"
    x,y = np.unique(data[:,2],return_counts=True) #get x and y values
    
    xLabel = ["Salmonella enterica","Bacillus cereus","Listeria",
             "Brochothrix thermosphacta"] #x-labes
    
    prop_iter = iter(plt.rcParams['axes.prop_cycle'])
    
    plt.rc('axes',prop_cycle=plt.rcParams['axes.prop_cycle'])    
    
    plt.bar(x,y) #Plot bar plot
    
    plt.xticks(x,xLabel,rotation=45)
    
    plt.show()
    
    
    
    
    