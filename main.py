# -*- coding: utf-8 -*-
"""
COMMENT ON MAIN SCRIPT
"""


from functions.dataLoad import dataLoad
from functions.dataPlot import dataPlot
from functions.dataStatistics import dataStatistics
from functions.userinput import displayMenu,inputStr,header
from functions.filterData import filterData,printFilter
import numpy as np

#Add welcoming message


#Initial variables
dataLoaded = False
bacActive = "No active bacteria filter"
rangeActive = "No active range filter"

#Keep menu until user quits
while True:
    header("MAIN MENU") #Interface
    printFilter(bacActive,rangeActive) #Print any active filters
    #User Menu
    menu = displayMenu(["Load data","Filter data","Display statistics", "Generate plots", "Show data", "Quit"])
    
    #Load data
    if menu == 1:
        #Check for correct filename
        header("LOAD DATA MENU")
        print("If you wish to exit, type 'exit'")
        while True:
            try:
                filename = inputStr("Please enter the name of the datafile: ")
                print("") #Add space
                
                #Check for exit
                if filename != "exit":
                    data = dataLoad(filename) #Load data
                    print("\nData loaded succesfully from",filename)
                    dataLoaded = True #Set data as loaded
                    dataOld = np.copy(data) #Copy of data
                    break
                
                #exit
                else:
                    break
                
            except FileNotFoundError:
                print("File not found, please try again")
    
    #Filter data
    elif (menu == 2) and dataLoaded:
        while True:
            header("FILTER MENU")
            print("Please specify a filter")
            #Print any active filters
            printFilter(bacActive,rangeActive)
            
            menu2 = displayMenu(["Bacteria filter","Range filter","Back"])
            
            #Bacteria type filter
            if menu2 == 1:
                data,bacActive,rangeActive = filterData("Bacteria filter",dataOld,bacActive,rangeActive)
               
            #Range filter
            elif menu2 == 2:
                data,bacActive,rangeActive = filterData("Range filter",dataOld,bacActive,rangeActive)
            
            #Back
            elif menu2 == 3:
                break
                        
    
    #Display statistics
    elif (menu == 3) and dataLoaded:
        statStr = ["Mean Temperature","Mean Growth rate","Std Temperature","Std Growth rate",
                             "Rows","Mean Cold Growth rate","Mean Hot Growth rate","Back"]
        
        header("STATISTICS MENU")
        while True:   
            #Print any active filters
            printFilter(bacActive,rangeActive)
            menu2 = displayMenu(statStr) #Show different statistics to be computed
            if menu2 == 8: #Quit
                break
            else:
                stat = dataStatistics(data,statStr[int(menu2-1)]) #Compute statistic
            
            #Print statistic
            print("""\n==================================================   
{} | {}
==================================================\n""".format(statStr[int(menu2-1)],stat))
            
    #Generate plots
    elif (menu == 4) and dataLoaded:
        dataPlot(data)
        print("")
    
    #Show all data
    elif (menu == 5) and dataLoaded:
        np.set_printoptions(threshold=np.inf)
        print(data)
        np.set_printoptions(threshold=5000)
        
        
    #Quit
    elif menu == 6:
        break
    
    #No data loaded msg
    else:
        print("\nERROR: No data has been loaded\n")