#tuples are also immutables it has parenthesis
"""
>>> a = (1,2,3,4,5)
>>>
>>>
>>>
>>> type (1)
<class 'int'>
>>>
>>>
>>> type(a)
<class 'tuple'>
>>>
>>>
>>> len(a)
5
>>>
>>> min(a)
1
>>> max(a)
5
>>>
>>> a + (7,8,9)
(1, 2, 3, 4, 5, 7, 8, 9)
>>>
>>> a *2
(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
>>>
>>> a
(1, 2, 3, 4, 5)
>>>
>>>
>>>
>>> a[1:]
(2, 3, 4, 5)
>>> a[:1]
(1,)
>>> a[:2]
(1, 2)
>>> a[-1]
5
>>> a[1:-1]
(2, 3, 4)
>>>
>>>
>>> a[-1:-1]
()
>>> a[2:-2]
(3,)
>>> a[-2:]
(4, 5)
>>> a[2,-2]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a[2,-2]
TypeError: tuple indices must be integers or slices, not tuple
>>> a[2,-3]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a[2,-3]
TypeError: tuple indices must be integers or slices, not tuple
>>> a[2:-3]
()
>>> a[2:-3]
()
>>> a[-2:-2]
()
>>> a[2:-2]
(3,)
>>>


>>> 2 in a
True
>>> 6 in a
False
>>> 2
 not in a
False


>>> del a
>>>
>>> a
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a
NameError: name 'a' is not defined

even if a tuple is immutable it can be completely deleted

so immutability does not mean it can't be entirely deleted, it can't be modified


>>> my_tuple = (1, 2, 3, 'a', 'b', 'c', [4, 5, 6])
>>>
>>>
>>> my_tuple[-1]*5
[4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6]
>>>
#since the last element is list the result would also be list
>>>
>>>
a
>>> a = (1,2,3,4,5)
>>>
>>> a[-1]*6
30
>>> b = ('a','v','c')
>>>
>>> b[-1]*3
'ccc'



"""