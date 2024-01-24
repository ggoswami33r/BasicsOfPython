
#Generator function
>> > my_object = my_gen(10, 5)
>> >
>> > next(my_object)
i is 0
y is 5
50
>> > next(my_object)
i is 1
y is 5
50
>> >
>> > next(my_object)
i is 2
y is 5
50
>> > next(my_object)
i is 3
y is 5
50
>> > next(my_object)
i is 4
y is 5
50
>> > next(my_object)
i is 5
y is 5
50
>> > next(my_object)
i is 6
y is 5
50
>> > next(my_object)
i is 7
y is 5
50


#Another process
>> gen_exp = (x for x in range(5))
>>> next(gen_exp)
0
>>> next(gen_exp)
1
>>> next(gen_exp)
2
next(gen_exp)
>>>
>>> next(gen_exp)
3
>>> next(gen_exp)
4
>>> next(gen_exp)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    next(gen_exp)
StopIteration
>>> next(gen_exp)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    next(gen_exp)
StopIteration