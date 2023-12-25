list1 = ["Cisco","Jupiter","Avaya",10,23,87];
print(list1);
# how to determine the length of a list

print(len(list1));

print(list1[2]);

list1[2]= "HP";

print(list1);


list2 = [1,4,6];

# to get the minimum entry from the above list we need to use min()

print(min(list2));
#1

# max()  to be used to get maximum entry

print(max(list2));
#6


list3 = ["a","b","c"];

print(min(list3));  #a
print(max(list3));  #c


#to get extra element within an existing list

list1.append(100) # this would add a number at the end of the list
list1.insert(9,"Hello") # if you want to add something at 9th index you can use index method

print(list1);

del list1[4]; # this would delete a number within the list at 5th index
print("the last list ")
print(list1);


# to remove the element you want
list1.pop(0)

print(list1)


#to remove the exact elemtn you can mention the direct element or string

list1.remove("Cisco")

print(list1)


# if we eant to extend the list of an existing list we can do using extend method

list1.extend(list2)

list2.extend(list1)


# if we eant to know the exact index of an elemtn we can do using the index method
list1.index(87  ## it would give the exact index of that element)


list1.count(87) # it would return the count of the element you are looking for


# using sort method you can use sort a list
#list1.sort() or list2.sort();  # it would throuw an error because both the list a combination of int and str
#so the sort method can't work here

#reverse() would help you to sort the list in descending order

list2.reverse();

#apart from sort method we can use sorted method to sort or reverse sort a list

sorted(list1)

sorted(list2,reverse= False)


#concatenation and multiplication of a list works like below
#list1 + list2 and list*3


#string slicing
"""
>>> list3 = [1,2,3,"a","b","c"]
>>>
>>>
>>>
>>> list3[-1]
'c'

#the above code describes how to fetch the last element from the list 
>>>
>>>


>>> list3[-3:]
['a', 'b', 'c']
# the above code represents how to fetch the last 3 element from the list
>>>
>>>
>>> list3[:-3]
[1, 2, 3]
#the above code represents how to fetch the first 3 elements
>>>
>>>
>>>
>>>
>>>
>>> list3[2:-2]
[3, 'a']

the above code represents how to fetch from the second element to last second element
>>> list3[1:-1]
[2, 3, 'a', 'b']

the above code represents how to fetch from the first element to last element

>>>
>>>
>>>
>>> list3[-5:-1]
[2, 3, 'a', 'b']

the above code represents how to fetch 5th from the last to 1st from the last element
>>>
>>>
>>>
>>> list3[2:5:2]
[3, 'b']

the above code represents the first indexed element and 5th indexed element and the interval out of it
>>>
>>>
>>>
>>> list3[::-1]
['c', 'b', 'a', 3, 2, 1]

the above code represents how to reverse a string


"""