# -*- coding: utf-8 -*-
"""
COMMENT ON MAIN SCRIPT
"""

loadData = (input("Please type the name of file you want to load"))

from functions.dataLoad import dataLoad
from functions.dataPlot import dataPlot
from functions.dataStatitics import dataStatistics
from functions.userinput import displayMenu,inputNumber,inputStr



dataLoad("test.txt")


# Following code is copy-pasted as a frame/skabelon
def displayMenu(options): 
# DISPLAYMENU Displays a menu of options, ask the user to choose an item 
# and returns the number of the menu item chosen.
# Usage: choice = displayMenu(options) 
# 
# Input options Menu options (array of strings) 
# Output choice Chosen option (integer) 
# 
#
# Display menu options 
for i in range(len(options)):
    print("{:d}. {:s}".format(i+1, options[i]))
#
# Get a valid menu choice
choice = 0
while not(np.any(choice == np.arange(len(options))+1)):
    choice = inputNumber("Please choose a menu item: ")
return choice
