'''
#Decorators - functions that take another function as a parameter and extend its functionality and behavior without modifying it
>>> def my_decorator(target_function):
	def function_wrapper():
		return "Python is a " + target_function() + " language. ";
	return function_wrapper;

>>> def target_function
SyntaxError: invalid syntax
>>> @Decorator
def target_function():
	return " Cool ";

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    @Decorator
NameError: name 'Decorator' is not defined
>>> @my_decorator
def target_function():
	return " Cool ";

>>> target_function();
'Python is a  Cool  language. '
'''

'''
Another Example
'''
'''

def my_decorator(target):
    def function_wrapper():
        return "I like solving " + target() + " in Python. It's my hobby, really!"

    return function_wrapper


@my_decorator
def target():
    return "coding exercises"


print(target())

'''