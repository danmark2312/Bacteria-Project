# -*- coding: utf-8 -*-

from functions.userinput import displayMenu,inputNumber
import numpy as np

def filterActive(bacActive,rangeActive):
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
        print("""
=======================================================
Current filters:
Bacteria: {} | Range: {}
=======================================================
                      """.format(bacActive,rangeActive))
    

def filterData(filtertype,dataOld):
    """
    INPUT:
        filtertype: A string specifying how to filter the data
        
        dataOld: unfiltered data
        
    OUTPUT:
        data: Filtered data
        
        bacActive: A list specifying the active bacteria filters, if none
            then it is a string stating there is no active filter of given type
            
        rangeActive: A list specifying the active range filter, if none
            then it is a string stating there is no active filter of given type
        
    USAGE:
        data,bacActive,rangeActive = filterData(filtertype,dataOld)
    
    Emil Ballermann (s174393) & Simon Moe Sørensen (s174420)
    """
    #Initial variables
    bacStr = ["Salmonella enterica","Bacillus cereus","Listeria",
          "Brochothrix thermosphacta"]
    r1,r2 = -42,-42
    bacList = np.array([],dtype=int)
    bacActive = "No active bacteria filter"
    rangeActive = "No active range filter"
    
    #Range filter    
    if filtertype == "Range filter":
        print("""
\nYou have chosen to filter for range.
Select a range of -1 to clear rangefilter\n""")
        
        while (r1 or r2) != -1:
            r1 = inputNumber("Please enter a lower range: ")            
            r2 = inputNumber("Please enter a upper range: ")
            
            #Get min and max, just in case user is retarded
            upperRange = max(r1,r2)
            lowerRange = min(r1,r2)
            
            #Get data in the range and filter it
            Range = ((lowerRange < dataOld[:,1]) & (dataOld[:,1] < upperRange))
            data = dataOld[Range]
            rangeActive = [lowerRange,upperRange]
            break
        
        #Check if user wants to clear the range
        if (r1 or r2) == -1:
            data = dataOld
            rangeActive = "No active range filter"
            r1,r2 = -42,-42
            
        #Filter for bacteria type, if active
        if len(bacList) != 0:
            mask = np.in1d(data[:,2],bacList) #Where each value of bacList is in dataOld
            data = data[mask] #Filter from mask
            
   
    #Bacteria filter
    if filtertype == "Bacteria filter":
        
        print("""
\nYou have chosen to filter for bacteria.
Select the bacteria you want to filter
If it is already a filter, it will be removed\n""")
                
        while True:
            
            filterActive(bacActive,rangeActive)
            
            menu = int(displayMenu(bacStr+["Quit"]))
            #Quit
            if menu == 5:
                break
            
            #Check if menu (bacteria chosen) is in bacList
            if menu in bacList:
                bacList = bacList[bacList != menu] #Remove from list
                bacActive = np.array(bacStr)[bacList] #Active bacteria filter
            
            else:
                bacList = np.append(bacList,menu) #Add to list
            
            #Check if there is an active filter
            if len(bacList)!=0:
                #Filter from data
                mask = np.in1d(dataOld[:,2],bacList) #Where each value of bacList is in dataOld
                data = dataOld[mask] #Filter from mask
                bacActive = np.array(bacStr)[bacList-1] #Active bacteria filter
            else:
                bacActive = "No active bacteria filter"
                #Filter for active range filter, if active
                if (r1 or r2) != -42:
                    data = dataOld[Range]
        
    return data,bacActive,rangeActive

