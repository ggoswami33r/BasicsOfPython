def my_first_function():
    "This is my first function !!"
    print("This is first defined function in python..")

"""
help(my_first_function())

>>> help(my_first_function())
My first function
Help on NoneType object:

class NoneType(object)
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
>>> help(my_first_function)
Help on function my_first_function in module __main__:

my_first_function()
    This is my first function in Python!!
"""

'''
calling the function

'''
'''
its commented because from here there is no use, it s giving here error
my_fist_function();
'''


'''
>>> 
>>> def my_second_function(x):
	print(x)

	
>>> my_second_function("Hello Python")
Hello Python
'''


"""
>>> def my_third_function(x,y):
	print("Hello " + x)
	print("Hello " + y)

	
>>> my_third_function("Java","Python")
Hello Java
Hello Python
>>> 
"""


"""

>>> def another_method(x,y,z):
	sum =  (x+y)*z;
	return sum ** 2;

>>> another_method(2,3,2);
100
"""

'''
>>> def return_none_method(x,y,z):
	sum = ((x+y)*z)**2;
	return

>>> 
>>> return_none_method(1,2,3)
>>> 

see its not returning anything
'''

'''
>>> another_method(1,2)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    another_method(1,2)
TypeError: another_method() missing 1 required positional argument: 'z'
>>> 
>>> 
>>> another_method(1,2,"str")
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    another_method(1,2,"str")
  File "<pyshell#50>", line 3, in another_method
    return sum ** 2;
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int' 
'''

"""
positional arguments
>>> 
>>> another_method(x=2,y=3,z=4)  #this is keyword arguments
400

keyword argument
>>> another_method (z=2,x=8,y=1)  # here the position changed and based on keyword calculations are getting performed
324
"""

'''
>>> another_method(x=2,y=4,3)
SyntaxError: positional argument follows keyword argument

here keyword argument should be followed by positional argument , the rule for processing the value is 
first positional argument should be followed by keyword arguments

1. Positional arguments
2. Keyword arguments that's why line no 118 is throwing an error, there first keyword arguments is there, then positional arguments

'''

'''
  but if we keep positional arguments first and then keyword arguments, then there would be no problem like below
  >>> another_method(1,2,z=3)
81

#here positional arguments placed first and then keyword arguments have been placed
'''

'''

#Using positional and keyword arguments the method can be called like below as well

>>> def my_first_function(x,y,z=3):
	sum = (x+y)*z;
	return sum;

>>> my_first_function(1,2,3)
9
>>> 
>>> my_first_function(1,2)
9  # the same method has been processed here


'''

"""
 def function1(a,*args):
	print(a)
	print(args)

	
>>> function1("Str",100,200)
Str
(100, 200)
>>> 
>>> 

here *args is being considered as a tuple

>>> function1(10)
10
()
>>> 

>>> def function1(x , *args):
	print(x)
	for elements in args:
		print(elements)
		
		
>>> function1("Hello Python",1,2,3,4,5,6,7,8)
Hello Python
1
2
3
4
5
6
7
8
>>> 



another process to implement positional and keyword arguments is as below 

>>> function2(**kwargs, *args):
	
SyntaxError: iterable argument unpacking follows keyword argument unpacking
>>> def function2(**kwargs, *args):
	
SyntaxError: invalid syntax
>>> def function22(*args,**kwargs):
	print(args)
	print(kwargs)

	
>>> function22(4,5,6, x=1,y,6,z=9)
SyntaxError: positional argument follows keyword argument
>>> function22(4,5,6, x=1,y=6,z=9)
(4, 5, 6)
{'x': 1, 'y': 6, 'z': 9}



*args is used for positional arguments
**kwargs us used for keyword arguments


#Functions - Basics
def my_first_function(x, y): #defining a function that takes two parameters
    sum = x + y
    return sum #this statement is used to exit a function and return something when the function is called
    
my_first_function(1, 2) #calling a function and passing two POSITIONAL arguments, the values of 1 and 2; result is 3
 
my_first_function(x = 1, y = 2) #calling a function and passing two KEYWORD arguments, the values of 1 and 2; result is 3
 
my_first_function(1, y = 2) #calling a function and passing mixed types of arguments, the values of 1 and 2; result is 3; rule: positional arguments always before keyword arguments!
 
def my_first_function(x, y, z = 3): #specifying a default parameter value in a function definition
 
def my_first_function(x, *args) #specifying a variable number of positional parameters in a function definition; args is a tuple
 
def my_first_function(x, **kwargs) #specifying a variable number of keyword parameters in a function definition; kwargs is a dictionary
 
global my_var #"importing" a variable in the global namespace to the local namespace of a function


"""