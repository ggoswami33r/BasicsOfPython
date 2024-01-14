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