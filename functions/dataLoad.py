

import csv
import numpy as np

def dataLoad(filename):
    """
    INPUT:
        filename: A string containing the full filename (with extension) of a datafile

    OUTPUT:
        data: An N x 3 matrix

    USAGE:
        data = dataLoad(filename)


    Emil Ballermann (s174393) & Simon Moe Sørensen (s174420)
    """

    #Initial variables
    data = [0,0,0]
    read = True
    msg = []

    #Append each row to dataRaw
    with open(filename, newline='') as inputfile:
        for line,row in enumerate(csv.reader(inputfile)):

            arr = np.array(row[0].split(" "), dtype=float) #Creating an array of row
            #Only read line if len is three
            if len(arr) == 3:
                #Checking for error conditions
                if ((10 >= arr[0]) or (arr[0] >= 60)): #Temperature
                    read = False #Do not read line
                    msg.append("Erroneous line at line: {} Temperature did not meet requirements".format(line+1))

                if (arr[1]<0): #Growth rate
                    read = False #Do not read line
                    msg.append("Erroneous line at line: {} Growth rate did not meet requirements".format(line+1))


                if ((0 >= arr[2]) or (arr[2] > 4)): #Bacteria type
                    read = False #Do not read line
                    msg.append("Erroneous line at line: {} Bacteria type did not meet requirements".format(line+1))

                if read:
                    data = np.vstack((data,arr)) #Stack row into N x 3 matrix

                read = True #reset read

            else:
                print("Erroneous line at line:",line+1,"Length of row was not 3")

    msg = "\n".join(msg)
    data = data[1:len(data)] #Remove placeholder of [0,0,0]

    return data,msg
