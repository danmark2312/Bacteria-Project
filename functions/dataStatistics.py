# -*- coding: utf-8 -*-
import numpy as np

def dataStatistics(data,statistics):
    """
    INPUT:
        data: An N x 3 matrix
        statistics: A string of one of the following statistics:
            "Mean Temperature"
            "Mean Growth rate"
            "Std Temperature"
            "Std Growth rate"
            "Mean Cold Growth rate"
            "Mean Hot Growth rate"
            "Min Growth rate"
            "Max Growth rate"
            "Min Temperature"
            "Max Temperature"
            "Rows"
    OUTPUT:
        result = A float representing the given statistic

    USAGE:
        stat = dataStatistics(data,statistics)

    Emil Ballermann (s174393) & Simon Moe Sørensen (s174420)
    """
    #Check for length of data
    if len(data) != 0:
        #Initial variables
        result = np.nan
        #Defining average temperature
        if statistics == "Mean Temperature":
            result=np.mean(data[:,0])

        #Defining average growth rate
        elif statistics == "Mean Growth rate":
            result=np.mean(data[:,1])

        #Defining standard deviation of temperature
        elif statistics == "Std Temperature":
            result=np.std(data[:,0])

        #Defining standard deviation of growth rate
        elif statistics == "Std Growth rate":
            result=np.std(data[:,1])

        #Counting numbers of rows in data
        elif statistics == "Rows":
            result=len(data)

        #Defining average growth rate for every data under 20 degrees
        elif statistics == "Mean Cold Growth rate":
            index1 = np.where(data[:,0]<20)
            result = np.mean(data[index1,1])

        #Defining average growth rate for every data above 50 degrees
        elif statistics == "Mean Hot Growth rate":
            index2 = np.where(data[:,0]>50)
            result=np.mean(data[index2,1])

        #Define minimum values for growth rate
        elif statistics == "Min Growth rate":
            result = min(data[:,0])

        elif statistics == "Max Growth rate":
            result = max(data[:,0])

        #Define maximum values for temp
        elif statistics == "Min Temperature":
            result = min(data[:,1])

        elif statistics == "Max Temperature":
            result = max(data[:,1])
    return result
