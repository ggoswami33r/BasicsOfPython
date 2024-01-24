"""
>> > for i in range(10):
    result = i ** 2;
    list1 = list1.append(result)

Traceback(most
recent
call
last):
File
"<pyshell#4>", line
3, in < module >
list1 = list1.append(result)
NameError: name
'list1' is not defined
>> >
>> >
>> > list1 = []
>> > for i in range(10):
    result = i ** 2;
    list1.append(result);

>> > list1
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>> >
>> >
>> > list2 = [x ** 2 for x in range(10)]
>> >
>> > list2
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>> >
>> > list3 = [x ** 2 for x in range(10) if x > 5]
>> >
>> > list3
[36, 49, 64, 81]
>> >
>> >
>> > set1 = {x ** 3 for x in range(10) if x > 2}
>> >
>> > dict1 = {x: x ** 2 for x in range(10) if x > 2}
>> > set1
{64, 512, 343, 216, 729, 27, 125}
>> > dict1
{3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>> > type(dict1)
<

class 'dict'>

>> >
"""


#using list compresention if I want to print a list of square of a list of number we can do using the below method
a = [x*2 for x in range(10) if x>5] #x>5 I want the sq of number if number > 5
#now simply print a like below
>>> a = [x*2 for x in range(10) if x>5]
>>>
>>>
>>>
>>> a
[12, 14, 16, 18]


#we can do the same thing using lambda
a = lambda x : [x**2 for x in range(10) if x>5]

>>> a = lambda x : [x**2 for x in range(10) if x>5]
>>>
>>> a
<function <lambda> at 0x000001725F7FEDC0>
>>> a(0)
[36, 49, 64, 81]
>>>



## other types of advantages we have using lambda


>>> def myFunction(initialList):
	result_list = [];
	for i in range(10):
		for l in range(5):
			result = i * l;
			result_list.append(result)
	result_list = initialList + result_list;
	return result_list;

>>> myFunction([101,122,123])
[101, 122, 123, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 0, 2, 4, 6, 8, 0, 3, 6, 9, 12, 0, 4, 8, 12, 16, 0, 5, 10, 15, 20, 0, 6, 12, 18, 24, 0, 7, 14, 21, 28, 0, 8, 16, 24, 32, 0, 9, 18, 27, 36]
>>>



# the above method can be used using lambda

#use of lambda and its advantage
def myFunction(myList):
	result = []
	for x in range(10):
		for y in range(5):
			mul = x*y;
			result.append(mul);
	return result + myList;

>>> myFunction([1,2,3,4,5])
[0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 0, 2, 4, 6, 8, 0, 3, 6, 9, 12, 0, 4, 8, 12, 16, 0, 5, 10, 15, 20, 0, 6, 12, 18, 24, 0, 7, 14, 21, 28, 0, 8, 16, 24, 32, 0, 9, 18, 27, 36, 1, 2, 3, 4, 5]
>>>
>>>
>>> m = lambda myList:[x*y for x in range(10) for y in range(5)] + myList
>>> m([1,2,3,4,5])
[0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 0, 2, 4, 6, 8, 0, 3, 6, 9, 12, 0, 4, 8, 12, 16, 0, 5, 10, 15, 20, 0, 6, 12, 18, 24, 0, 7, 14, 21, 28, 0, 8, 16, 24, 32, 0, 9, 18, 27, 36, 1, 2, 3, 4, 5]
>>>



a = lambda x,y : x*y;
>>> a(8,7)
56
>>> a = lambda x,y : x/y
>>> a (9,0)
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    a (9,0)
  File "<pyshell#198>", line 1, in <lambda>
    a = lambda x,y : x/y
ZeroDivisionError: division by zero
>>>

list3 = [x*3 for x in range(10) if x>5]
>>> list3
[18, 21, 24, 27]
>>>

# converting this above one into lambda
list3 = lambda x: [x*3 for x in range(10) if x>5]
>>> list3
<function <lambda> at 0x000001725F7FEEE0>
>>> list3(0)
[18, 21, 24, 27]
>>>


>>> r1 = range(10)
>>>
>>> def product10(a):
	return a*10;

>>>
>>> r1 = range(10)
>>>
>>> list(map(product10, r1))
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>>
>>>
>>>
>>> list(map(lambda a : a*10, r1))
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>>

list(filter(lambda a: a>5, r1))
[6, 7, 8, 9]


def my_gen(x, y):
	for i in range(10):
		print("i is %d" % i);
		print("y is %d" % y);
		yield x * y;


