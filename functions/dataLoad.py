"""

INPUT: 
    
OUTPUT:
    
USAGE:
    

Emil Ballermann (s174393) & Simon Moe Sørensen (s174420)
"""

import csv

def dataLoad(filename):
    
    #Initial variables
    dataRaw = []
    
    #Append each row to dataRaw
    with open(filename, newline='') as inputfile:
        for row in csv.reader(inputfile):
            dataRaw.append(row)
    
    
    
    
    return dataRaw