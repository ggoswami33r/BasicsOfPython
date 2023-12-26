# set can be defined in the below way
list1 = [12,87,36,9,236];
set1 = set(list1) # it does not support any duplicate element


# a set can also be defined in the below way
set2 = {87,98,124,65,45,34,76}

# the process for checking whether an element is present in the set or not

print(98 in set1)

print(98 in set2)


# an element can be added in the set by add method
set1.add(12332);


set2.add(982);

#an element can be removed by using remove method
set2.remove(98)



## to fetch the common element we can use intersect method


set1.intersection(set2)

set2.intersection(set1)

## to see the difference between two set the below method can be used

set1.difference(set2)

set2.difference(set1)


# two set can be merged using union method
set1.union(set2)

set2.union(set1);




# the first element can be removed using pop method

set1.pop();

# to clear the entire element from a set we can use clear method

set1.clear()

#frozen set is immutable set, add, remove, pop can't used here

"""
fs1 = frozenset(list1)



type(fs1)
<class 'frozenset'>



fs2 = frozenset(set2)


fs2
frozenset({98, 73, 237, 25, 127})


fs1
frozenset({2346, 76, 236, 947, 439, 126, 127})



fs1.intersection(fs2)
frozenset({127})


fs1.difference(fs2)
frozenset({2346, 76, 236, 947, 439, 126})




fs1.union(fs2)
frozenset({98, 73, 2346, 236, 76, 237, 947, 439, 25, 126, 127})

"""