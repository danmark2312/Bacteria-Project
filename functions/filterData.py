# -*- coding: utf-8 -*-

from functions.userinput import displayMenu,inputNumber,header
import numpy as np

def printFilter(bacActive,rangeActive):
    """
    INPUT:
        bacActive: A list specifying the active bacteria filters, if none
            then it is a string stating there is no active filter of given type
            
        rangeActive: A list specifying the active range filter, if none
            then it is a string stating there is no active filter of given type
    
    OUTPUT:
        Message specifying current filters
    """
    
    if (type(bacActive) == np.ndarray) or (type(rangeActive) == list): 
    #Print active filters if any
        print("""=======================================================
                     ACTIVE FILTERS
         
Current filters:
Bacteria: {} 
Range: {}
=======================================================
                      """.format(bacActive,rangeActive))
    

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
        data,conditions = filterData(filtertype,dataOld,conditions)
    
    Emil Ballermann (s174393) & Simon Moe Sørensen (s174420)
    """
    #Initial variables
    bacStr = ["Salmonella enterica","Bacillus cereus","Listeria",
          "Brochothrix thermosphacta"]
    r1,r2 = -42,-42
    
    #Extracting variables from condition list
    bacActive = conditions[0]
    rangeActive = conditions[1]
    bacList = conditions[2]
    range_ = conditions[3]
    mask = conditions[4]
        
    #Range filter    
    if filtertype == "Range filter":
        header("RANGE FILTER MENU") #Interface
        print("""You have chosen to filter for range.
Select a range of -1 to clear rangefilter""")
        
        r1 = inputNumber("Please enter a lower range: ")            
        r2 = inputNumber("Please enter a upper range: ")
        #Get min and max, just in case user is retarded
        upperRange = max(r1,r2)
        lowerRange = min(r1,r2)
        
        #Define the active range 
        rangeActive = [lowerRange,upperRange]
        
        #Check if user wants to clear the range
        if (r1 or r2) == -1:
            #Reset range variables
            rangeActive = "No active range filter"
            r1,r2 = -42,-42

            
   
    #Bacteria filter
    elif filtertype == "Bacteria filter":
        header("BACTERIA FILTER MENU") #Interface
        print("""You have chosen to filter for bacteria.
Select the bacteria you want to filter
If it is already a filter, it will be removed\n""")
                
        while True:
            printFilter(bacActive,rangeActive) #Print filter
            menu = int(displayMenu(bacStr+["Quit"])) #Display a menu
            
            #Quit
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
    if type(bacActive) != str:
        mask = np.in1d(dataOld[:,2],bacList) #Where each value of bacList is in dataOld
        data = dataOld[mask] #Masking from unfiltered data
        
    else:
        data = dataOld #Data is the same as old
    
    if type(rangeActive) != str:
        range_ = ((lowerRange < data[:,1]) & (data[:,1] < upperRange))   
        data = data[range_] #Data is filtered for range
        
    if not (type(bacActive) != str) or (type(rangeActive) != str):
        data = data #No changes to data, but it is pre-filtered
    
    #Contain conditions from filter function in list
    conditions = [bacActive,rangeActive,bacList,range_,mask]
    
    return data,conditions