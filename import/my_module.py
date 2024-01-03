my_var = 10
def my_function():
    print("This code is getting invoked inside my function")

# if I dont want the below code to be executed without being invoked then instead of the below line we can use the below chunk of code
#print("This code is from the outside of the function")
if __name__ == "__main__" "":
    print("This code is from the outside of the function")
#also this functionality will executed if this current file is being run


'''
#Modules and importing - Basics
 
#Importing the sys module; the import statements should be placed before any other code in your application
import sys 
 
#Importing only a variable (pi) from the math module
from math import pi 
 
#Importing only a function (sin()) from the math module; there's no need to add the parentheses of the function when importing it
from math import sin 
 
#Importing all the names (variables and functions) from the math module
from math import * 
'''