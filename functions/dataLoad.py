"""

INPUT: 
    
OUTPUT:
    
USAGE:
    

Emil Ballermann (s174393) & Simon Moe Sørensen (s174420)
"""

import csv
import numpy as np

def dataLoad(filename):
    
    #Initial variables
    data = [0,0,0]
    read = True
    
    #Append each row to dataRaw
    with open(filename, newline='') as inputfile:
        for line,row in enumerate(csv.reader(inputfile)):
            
            arr = np.array(row[0].split(" "), dtype=float) #Creating an array of row
            
            #Checking for error conditions
            if ((10 > arr[0]) or (arr[0] > 60)): #Temperature
                read = False #Do not read line
                print("Erroneous line at line:",line+1,"Temperature did not meet requirements")
                
            elif (arr[1]<0): #Growth rate
                read = False #Do not read line
                print("Erroneous line at line:",line+1,"Growth rate did not meet requirements")
                
            elif ((1 >= arr[2]) and (arr[2] <= 4)): #Bacteria type
                read = False #Do not read line
                print("Erroneous line at line:",line+1,"Bacteria type did not meet requirements")
            
            if read:
                data = np.vstack((data,arr)) #Stack row into N x 3 matrix
          
            read = True #reset read
    
    data = data[1:len(data)] #Remove placeholder of [0,0,0]

    return data