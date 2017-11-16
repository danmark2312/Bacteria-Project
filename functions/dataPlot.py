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
    
    plt.figure(1,figsize=(6,6)) #Set first figure with 1:1 ratio
    plt.subplots_adjust(top=0.88, bottom=0.225, left=0.11, right=0.9,
                        hspace=0.2,wspace=0.2) #Adjust size
    for i in range(0,len(x)):
        plt.bar(x[i],y[i],color=next(prop_iter)['color']) #Plot bar plot with colors

    plt.xticks(x,[bacStr[int(i)-1] for i in x],rotation=35) #Set labes and rotation
    plt.title("Number of bacteria") #Set title

    
    #Plot "Distribution of bacteria", only if relevant
    if len(y) > 1:
        plt.figure(2,figsize=(6,6)) #Set second figure with 1:1 ratio
        plt.subplots_adjust(top=0.901, bottom=0.276, left=0.09, right=0.71,
                            hspace=0.2, wspace=0.2) #Adjust size

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
    
    #Plot "Growth rate by temperature"
    plt.figure(3,figsize=(9,4)) #Set third figure with 9:4 ratio
    plt.subplots_adjust(top=0.932,bottom=0.119, left=0.275, right=0.689, 
                        hspace=0.2, wspace=0.2) #Adjust size
    dataSort = data[data[:,0].argsort()] #Sort data for temperature

    #Plot different graphs for each bacteria
    for bac in np.unique(data[:,2]):
        mat = dataSort[np.where(dataSort[:,2] == int(bac))] #Define matrix of bacteria
        #Check if matrix is not empty
        if len(mat) != 0:
            x,y = mat[:,0],mat[:,1] #get x and y axis
            plt.plot(x,y, label=bacStr[int(bac)-1]) #plot graph

    plt.legend(bbox_to_anchor=(1.05, 0.65), loc=2, borderaxespad=0.) #Set legend
    plt.xlabel("Temperature")
    plt.ylabel("Growth rate")
    plt.title("Growth rate by temperature") #Set title
    plt.show() #Show

#dataPlot(data)


