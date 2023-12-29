dict1 = {1:"dict1",2:"dict2"}

"""
>>> dict1 = {1:"dict1",2:"dict2"}
>>> 
>>> 
>>> 
>>> type(dict1)
<class 'dict'>
>>> 
>>> 
>>> dict1
{1: 'dict1', 2: 'dict2'}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> dict1[1]
'dict1'
>>> dict1[1] = "This is the first value"
>>> dict1
{1: 'This is the first value', 2: 'dict2'}
>>> dict1 [2] = "This is the second value";
>>> dict1
{1: 'This is the first value', 2: 'This is the second value'}
>>> 
>>> 
>>> dict1.update [3] = "This is  the 3rd value"
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dict1.update [3] = "This is  the 3rd value"
TypeError: 'builtin_function_or_method' object does not support item assignment
>>> 
>>> 
>>> del dict1[2]
>>> dict1
{1: 'This is the first value'}
>>> 
>>> 
>>> len(dict1)
1
>>> 1 in dict1
True
>>> 
>>> 
>>> 4 in dict1
False
>>> 
>>> 1 not in dict1
False
>>> dict1.keys
<built-in method keys of dict object at 0x0000011208403280>
>>> dict1.keys()
dict_keys([1])
>>> 
>>> 
>>> 
>>> 
>>> dict1.values()
dict_values(['This is the first value'])
>>> 
>>> dict1.items
<built-in method items of dict object at 0x0000011208403280>
>>> dict1.items()
dict_items([(1, 'This is the first value')])
>>> 
>>> 
>>> type(dict1.keys())
<class 'dict_keys'>
>>> 
>>> list(dict1.keys())
[1]
>>> 
>>> list(dict1.values())
['This is the first value']
>>> 
>>> 
>>> list(dict1.items())
[(1, 'This is the first value')]

In python the order for actual output is maintained here, whatever you use, keys, values or items , if there is multiple items available in the dictionary
if you use keys or values or items the same key / item(keys:values) would be printed.


>>> type(list(dict1.keys()))
<class 'list'>
>>> 
>>> 
>>> 
>>> type(list(dict1.values()))
<class 'list'>

>>> 
>>> type(list(dict1.items()))
<class 'list'>
>>> 
"""