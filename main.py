# -*- coding: utf-8 -*-
"""
This is the main script of the project.

It prints a series of menus for the user to navigate in.

It can do the following:
    - Load data
    - Filter data
    - Display statistics
    - Generate plots
    - Show data

The user will be informed of any ACTIVE filters throughout the menus.

For the sake of the user, a menu header has been added to each menu as well
in order to make navigation easier.


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
conditions = ["No active bacteria filter","No active range filter",np.array([],dtype=int),None,None]

#Keep menu until user quits
while True:
    header("MAIN MENU") #Interface
    printFilter(conditions[0],conditions[1]) #Print any active filters
    #User Menu
    menu = displayMenu(["Load data","Filter data","Display statistics", "Generate plots", "Show data", "Quit"])
    
    #Load data
    if menu == 1:
        #Check for correct filename
        header("LOAD DATA MENU") #Interface
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
            header("FILTER MENU") #Interface
            print("Please specify a filter")
            #Print any active filters
            printFilter(conditions[0],conditions[1])
            
            menu2 = displayMenu(["Bacteria filter","Range filter","Back"])
            
            #Bacteria type filter
            if menu2 == 1:
                data,conditions = filterData("Bacteria filter",data,dataOld,conditions)
                
            #Range filter
            elif menu2 == 2:
                data,conditions = filterData("Range filter",data,dataOld,conditions)
            
            #Back
            elif menu2 == 3:
                break
                        
    
    #Display statistics
    elif (menu == 3) and dataLoaded:
        statStr = ["Mean Temperature","Mean Growth rate","Std Temperature","Std Growth rate",
                             "Rows","Mean Cold Growth rate","Mean Hot Growth rate","Back"]
        
        header("STATISTICS MENU") #Interface
        while True:   
            #Print any active filters
            printFilter(conditions[0],conditions[1])
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
        np.set_printoptions(suppress=True)
        print(data)
        np.set_printoptions(threshold=8)
        
        
    #Quit
    elif menu == 6:
        break
    
    #No data loaded msg
    else:
        print("\nERROR: No data has been loaded\n")