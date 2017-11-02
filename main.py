# -*- coding: utf-8 -*-
"""
COMMENT ON MAIN SCRIPT
"""


from functions.dataLoad import dataLoad
from functions.dataPlot import dataPlot
from functions.dataStatitics import dataStatistics
from functions.userinput import displayMenu,inputNumber,inputStr

#Add welcoming message


#Initial variables
dataLoaded = False

#Keep menu until user quits
while True:
    #User Menu
    menu = displayMenu(["Load data","Filter data","Display statistics", "Generate plots", "Quit"])
    
    #Load data
    if menu == 1:
        #Check for correct filename
        print("\nIf you wish to exit, type 'exit'")
        
        while not dataLoaded:
            try:
                filename = inputStr("Please enter the name of the datafile: ")
                
                #Check for exit
                if filename != "exit":
                    data = dataLoad(filename) #Load data
                    print("\nData loaded succesfully from",filename,"\n")
                    dataLoaded = True #Set data as loaded
                    break
                
                #exit
                else:
                    break
                
            except FileNotFoundError:
                print("File not found, please try again")
    
    #Filter data
    elif (menu == 2) and dataLoaded:
        print("goat")
    
    #Display statistics
    elif (menu == 3) and dataLoaded:
        statStr = ["Mean Temperature","Mean Growth rate","Std Temperature","Std Growth rate",
                             "Rows","Mean Cold Growth rate","Mean Hot Growth rate","Back"]
        
        while True:            
            menu2 = displayMenu(statStr) #Show different statistics to be computed
            if menu2 == 8: #Quit
                break
            else:
                stat = dataStatistics(data,statStr[int(menu2-1)]) #Compute statistic
            
            #Print statistic
            print("""
==================================================   
{} | {}
==================================================""".format(statStr[int(menu2-1)],stat))
            
    #Generate plots
    elif (menu == 4) and dataLoaded:
        dataPlot(data)
    
    #Break
    elif menu == 5:
        break
    
    #No data loaded msg
    else:
        print("\nERROR: No data has been loaded\n")