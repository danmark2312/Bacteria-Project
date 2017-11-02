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
