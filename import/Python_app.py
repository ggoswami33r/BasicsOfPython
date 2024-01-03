#import my_module
from my_module import my_function
from my_module import my_var

#from my_module import * / if we want to import everything then we can use it, but its not recommended because unnecessarily it gives unused resource

print("Hello Python")

'''
Till now the o/p is as below :
This code is from the outside of the function
Hello Python

explanation : If you call it or not , if you have imported something and there something to be executed, that would get 
executed even if you are not explicitly calling that functionality

here simply importing my_module is responsible for "print("This code is from the outside of the function")" this to be printed
'''

#print("This is the variable from imported my_module -->" + str(my_module.my_var))
#my_module.my_function()
print("This the variable from imported my_module-->"  + str(my_var));
my_function() # I am not adding my_module because it's already there in from imported line


# import can be done in below as well apart from the first line
 #from my_module import my_function
