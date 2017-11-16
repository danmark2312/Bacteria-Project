# -*- coding: utf-8 -*-

from functions.userinput import displayMenu,inputLimit,header
import numpy as np

def printFilter(bacActive,growthActive,tempActive):
    """
    INPUT:
        bacActive: A list specifying the active bacteria filters, if none
            then it is a string stating there is no active filter of given type
<<<<<<< HEAD

        rangeActive: A list specifying the active range filter, if none
=======
            
        growthActive: A list specifying the active range filter, if none
>>>>>>> test
            then it is a string stating there is no active filter of given type

    OUTPUT:
        Message specifying current filters
    """
<<<<<<< HEAD

    if (type(bacActive) == np.ndarray) or (type(rangeActive) == list):
=======
    
    if (type(bacActive) == np.ndarray) or (type(growthActive) == list) or (type(tempActive) == list): 
>>>>>>> test
    #Print active filters if any
        print("""=======================================================
                     ACTIVE FILTERS

Current filters:
<<<<<<< HEAD
Bacteria: {}
Range: {}
=======================================================
                      """.format(bacActive,rangeActive))

=======
Bacteria: {} 
Growth rate range: {}
Temperature range: {}
=======================================================
                      """.format(bacActive,growthActive,tempActive))
    
>>>>>>> test

def filterData(filtertype,data,dataOld,conditions):
    """
    INPUT:
        filtertype: A string specifying how to filter the data

        data: Current data

        dataOld: Unfiltered data

        conditions: Collection of filtering information

    OUTPUT:
        data: Filtered data

        conditions: Collection of filtering information

    USAGE:
        data,conditions = filterData(filtertype,data,dataOld,conditions)

    Emil Ballermann (s174393) & Simon Moe Sørensen (s174420)
    """
    #Initial variables
    bacStr = ["Salmonella enterica","Bacillus cereus","Listeria",
          "Brochothrix thermosphacta"]
    r1,r2 = None,None

    #Extracting variables from condition list
    bacActive = conditions[0] #Active bacteria filters
<<<<<<< HEAD
    rangeActive = conditions[1] #Active range filters
    bacList = conditions[2] #Array of bacteria types, integers
    range_ = conditions[3] #Boolean array where range was true
    mask = conditions[4] #Boolean array where bacList is in data

    #Growth rate filter  
    if filtertype == "Range filter":
        header("RANGE FILTER MENU") #Interface
        print("""You have chosen to filter for range.
Type "clear" to clear range""")

=======
    growthActive = conditions[1] #Active range filters
    tempActive = conditions[2]#Active temperature filter
    bacList = conditions[3] #Array of bacteria types, integers
    range_ = conditions[4] #Boolean array where range was true
    mask = conditions[5] #Boolean array where bacList is in data
        
    #Growth rate range filter    
    if filtertype == "Growth rate range filter":
        header("GROWTH RATE RANGE FILTER MENU") #Interface
        print("""You have chosen to filter for growth rate range.
Type "clear" to clear range or "back" to go back""")
        
>>>>>>> test
        while True:
            r1 = inputLimit("Please enter a lower limit: ")
            #Break if clear
            if r1 == "clear":
                growthActive = "No active range filter"
                break
            #Exit without changing anything
            elif r1 == "back":
                break

            r2 = inputLimit("Please enter an upper limit: ")
            #Break if clear
            if r2 == "clear":
                growthActive = "No active range filter"
                break
            #Exit without changing anything
            elif r2 == "back":
                break

            #Get min and max, in case of wrong order
            growthActive = [min(r1,r2),max(r1,r2)]
            break
<<<<<<< HEAD

=======
        
    #Temperature range filter     
    elif filtertype == "Temperature range filter":
        header("TEMPERATURE FILTER MENU") #Interface
        print("""You have chosen to filter for a temperature range.
Type "clear" to clear range and "back" to go back""")
        
        while True:
            r1 = inputLimit("Please enter a lower limit: ") 
            #Break if clear
            if r1 == "clear":
                tempActive = "No active temperature range filter"
                break
            #Exit without changing anything
            elif r1 == "back":
                break
            
            r2 = inputLimit("Please enter an upper limit: ")
            #Break if clear
            if r2 == "clear":
                tempActive = "No active temperature range filter"
                break
            #Exit without changing anything
            elif r2 == "back":
                break
                
            #Get min and max, in case of wrong order
            tempActive = [min(r1,r2),max(r1,r2)]
            break
        
>>>>>>> test
    #Bacteria filter
    elif filtertype == "Bacteria filter":
        header("BACTERIA FILTER MENU") #Interface
        print("""You have chosen to filter for bacteria.
Select the bacteria you want to filter
If it is already a filter, it will be removed\n""")

        while True:
            printFilter(bacActive,growthActive,tempActive) #Print filter
            menu = int(displayMenu(bacStr+["Back"])) #Display a menu

            #Back
            if menu == 5:
                break

            #Check if menu (bacteria chosen) is in bacList
            if menu in bacList:
                bacList = bacList[bacList != menu] #Remove from array
            else:
                bacList = np.append(bacList,menu) #Add to array

            bacActive = np.array(bacStr)[bacList-1] #Active bacteria filter

            if len(bacActive) == 0:
                bacActive = "No active bacteria filter"

    #Use mask and range_ to filter data if filter is active (specific type)
    if type(bacActive) != str: #For bacteria
        mask = np.in1d(dataOld[:,2],bacList) #Where each value of bacList is in dataOld
        data = dataOld[mask] #Masking from unfiltered data

    else:
        data = dataOld #Data is the same as old
<<<<<<< HEAD

    if type(rangeActive) != str: #For range
        range_ = ((rangeActive[0] < data[:,1]) & (data[:,1] < rangeActive[1]))
        data = data[range_] #Data is filtered for range

    if not (type(bacActive) != str) or (type(rangeActive) != str):
=======
    
    if type(growthActive) != str: #For growth rate range
        range_ = ((growthActive[0] < data[:,1]) & (data[:,1] < growthActive[1]))   
        data = data[range_] #Data is filtered for growth rate range
        
    if type(tempActive) != str: #For temperature range
        range_ = ((tempActive[0] < data[:,0]) & (data[:,0] < tempActive[1]))   
        data = data[range_] #Data is filtered for temperature range
        
    if not (type(bacActive) != str) or (type(growthActive) != str) or (type(tempActive) != str):
>>>>>>> test
        data = data #No changes to data, but it is pre-filtered

    #Contain conditions from filter function in list
<<<<<<< HEAD
    conditions = [bacActive,rangeActive,bacList,range_,mask]

    return data,conditions
=======
    conditions = [bacActive,growthActive,tempActive,bacList,range_,mask]
    
    return data,conditions
>>>>>>> test
