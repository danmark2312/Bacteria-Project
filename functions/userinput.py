# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 03:58:30 2017

This file contains multiple functions that contribute to userinput

@author: Simon Moe Sørensen, moe.simon@gmail.com
"""
import numpy as np

def header(headerString):
    """
    Prints a header for displayMenu
    
    INPUT:
        headerString = A string for the header
    
    OUTPUT:
        A printed version of headerString
    
    """
    
    print("""
====================
{}
====================\n""".format(headerString))

def inputStr(prompt):
    """
    Userinput that only allows strings

    INPUT:
        prompt: String

    OUTPUT:
        str: The inputted string

    USAGE:
        inputStr("Please enter a string: ")

    """
    while True:
        try:
            str = input(prompt)
            break
        except ValueError:
            print("Not a valid string. Please try again")
    return str

def inputNumber(prompt):
    """
    Userinput that only allows any number and converts them to float values

    INPUT:
        prompt: any number

    OUTPUT:
        num = Float

    USAGE:
        inputStr("Please enter a number: ")
    """
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            print("Not valid number. Please try again")
    return num

def inputRange(prompt):
    """
    Userinput that only allows any number or the string, "clear", and converts them to float values

    INPUT:
        prompt: any number or "clear"

    OUTPUT:
        num = Float or string "clear"

    USAGE:
        inputStr("Please enter a number: ")
    """
    while True:
        try:
            num = input(prompt) #Get input
            num = float(num) #Try to make a float value
            break
        except ValueError:
            if num == "clear": #If it is clear, break
                num = "clear"
                break
            else:    
                print("Not valid number. Please try again")
    return num

def displayMenu(options):
    """
    DISPLAYMENU Displays a menu of options, ask the user to choose an item
    and returns the number of the menu item chosen.

    Usage: choice = displayMenu(options)

    Input options Menu options (array of strings)
    Output choice Chosen option (integer)


    Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    """

    # Display menu options
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))

    # Get a valid menu choice
    choice = 0

    while not(np.any(choice == np.arange(len(options))+1)):
       choice = inputNumber("Please choose a menu item: ")

    return choice
