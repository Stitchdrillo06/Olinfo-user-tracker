
#import libraries

import os
import json
import pandas



jsonpath = "./data/data/users"

#Section to make user json folder path customizable

'''
print("Insert json path, empty for std: ")
x = str(input())
if x:
    jsonpath = x
'''

print("Collecting fillenames... ", end = "")

#Collect list of filenames in directory

jsonnames = [i for i in os.listdir(jsonpath)]

#print(jsonnames)

print("Complete")

usersdata = []

print("Collecting user data as json... ", end = "")

#Iterationg on filenames

for i in jsonnames:
    
    #effective path to the file
    
    fpath = jsonpath + "/" + i
    
    with open(fpath) as f:
        
        jsonfile = json.load(f)
        
        #Converting json file to dict
        
        dx = dict(jsonfile)
        
        #Copying the dict allows us to change the dict size during iteration
        
        dxcopy = dx.copy()
        
        dxkeys = dx.keys()
        
        #Section to put the couples of sub-dicts in the main dict
        
        for kelm in dxkeys:
            
            if type(dx[kelm]) == type({"1":"a"}):
                
                dxkelmkeys = dx[kelm].keys()
        
                for i in dxkelmkeys:
                    
                    dxcopy[i] = dxcopy[kelm][i]
                                    
                del dxcopy[kelm]
                
        dx = dxcopy.copy()
        
        del dxcopy

        usersdata.append(dx)

#print(usersdata)

print("Complete")

print("Converting data to pandas DataFrame... ", end = "")

#Panda magic for organizing data

df = pandas.DataFrame.from_records(usersdata)

print("Complete")

#print(df)

print("Converting pandas DataFrame to csv... ", end = "")

#Converting everything to a csv file, which can be transformed in a DB table

df.to_csv("out.csv")

print("Complete")
