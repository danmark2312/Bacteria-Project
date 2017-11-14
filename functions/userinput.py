# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 03:58:30 2017

This file contains multiple functions that contribute to userinput

Emil Ballermann (s174393) & Simon Moe Sørensen (s174420)
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

def inputLimit(prompt):
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
                print("Not a valid number. Please try again")
    return num

def displayMenu(options):
    """
    
    INPUT:
        options: An array of strings
        
    OUTPUT:
        menu: an integer of the user's choice
    
    USAGE:
        menu = displayMenu(options)
    """
    
    #Print menu
    for i in range(len(options)):
        print("{}. {}".format(i+1,options[i]))
    
    #Initial variable
    choice = None
    
    #Get menu choice
    while not choice in np.arange(1,len(options)+1):
        choice = inputNumber("Please choose a menu item: ")
        if choice > len(options) or choice <= 0:
            print("\nChoice out of menu range")

    return choice






