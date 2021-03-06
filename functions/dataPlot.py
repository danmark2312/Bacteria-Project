# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.style.use('ggplot') #Use a prettier plot

def dataPlot(data):
    """
    INPUT:
        data: An N x 3 matrix
        
    OUTPUT:
        A bar plot of number of bacteria and a line plot of each bacteria's
        temperature to growth rate graph
        
    USAGE:
        dataPlot(data)
        
    
    Emil Ballermann (s174393) & Simon Moe Sørensen (s174420)
    """
    
    #Plot "Number of bacteria"
    x,y = np.unique(data[:,2],return_counts=True) #get x and y values
    x = x.astype(int) #Convert to integers
    bacStr = np.array(["Salmonella enterica","Bacillus cereus","Listeria",
             "Brochothrix thermosphacta"]) #x-labes
    prop_iter = iter(plt.rcParams['axes.prop_cycle']) #Iterate through colors
    
    for i in range(0,len(x)):
        plt.bar(x[i],y[i],color=next(prop_iter)['color']) #Plot bar plot with colors
    
    plt.xticks(x,[bacStr[int(i)-1] for i in x],rotation=35) #Set labes and rotation
    plt.title("Number of bacteria") #Set title
    plt.show() #Show
    
    #Plot "Distribution of bacteria", only if relevant
    if len(y) > 1:
        plt.figure(figsize=(6,6)) #Set 1:1 ratio
        
        #Function to make pretty percentages
        def make_autopct(values):
            def my_autopct(pct):
                total = sum(values)
                val = int(round(pct*total/100.0))
                return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
            return my_autopct
        
        explode = np.linspace(0.06,0.06,len(y)) #Create array of len(y) with 0.05 values
        plt.pie(y,labels=bacStr[x-1],shadow=True,explode=explode,autopct=make_autopct(y)) #Plot pie chart
        plt.title("Distribution of bacteria types")
        plt.show() #Show plot
    
    #Plot "Growth rate by temperature"
  
    dataSort = data[data[:,0].argsort()] #Sort data for temperature
    
    #Plot different graphs for each bacteria
    for bac in np.unique(data[:,2]):
        mat = dataSort[np.where(dataSort[:,2] == int(bac))] #Define matrix of bacteria
        #Check if matrix is not empty
        if len(mat) != 0:    
            x,y = mat[:,0],mat[:,1] #get x and y axis
            plt.plot(x,y, label=bacStr[int(bac)-1]) #plot graph
    
    plt.legend(bbox_to_anchor=(1.05, 0.65), loc=2, borderaxespad=0.) #Set legend
    plt.title("Growth rate by temperature") #Set title
    plt.show() #Show