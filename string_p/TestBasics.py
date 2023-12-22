user_input = input("Use the strings....")


print(user_input.index("Hello"))
print(user_input.count("H"))
print(user_input.upper())
print(user_input.lower())

print(user_input.find("xyz"))
print(user_input.startswith("H"))
print(user_input.endswith("D")) # these are case sensitive

## process to remove space or any particular character inside a string

print("Here I am removing only the spaces which are available at the beginning and end of the string...." + user_input.strip(" "));  # here I want to remove spaces at the beginning and at the end of the string....
print("Here I am removing only the spaces which are available anywhere within the string..." + user_input.replace(" ","")) # here I want to remove all the spaces anywhere within the string...

# if we want to split a branch of string separated by comma and would create a list then we can do use of split
d = "Cisco, Jupiter, Nortel, HP, Avaya";
print(d.split(","))  #['Cisco', ' Jupiter', ' Nortel', ' HP', ' Avaya']

# use of join method
a = "Cisco Switch"
print("_".join(a))   # C_i_s_c_o_ _S_w_i_t_c_h

'''
a = " $$$$$$ Cisco &&&& Router  "
>>> a.strip(" ").strip("$").replace(" ","");
'Cisco&&&&Router'
>>> a.strip(" ").strip("$").replace(" ","").replace("$","");
'Cisco&&&&Router'
'''



"""
+ can be used for concatenation
* can be used for multiplication for string as well
i.e. x = string * 3
the result would be ------------>    "stringstringstring"
"""

"""
 How to check whether a character is present in a string or not 
"""

a = "Cisco Switch"

if ("o" in a):
    print("O is present in a variable");
else:
    print("O is not present in a variable");

print("Cisco Model %s, %d WAN slots, IOS %f" % ("2600XM",2,12.4));

"""
to get the specific no of decimal point of floating number we can use like below
.1f%

.2f%
"""
"""
%s is for string
%d is for integer
%f for float
"""

"""
or we can use this below to get the same result

print("Cisco Model %s, %d WAN slots, IOS %.1f" % ("2600XM",2,12.4));
print("Cisco Model %s, %d WAN slots, IOS %.2f" % ("2600XM",2,12.4));
print("Cisco Model %s, %d WAN slots, IOS %.3f" % ("2600XM",2,12.4));
print("Cisco Model %s, %d WAN slots, IOS %.4f" % ("2600XM",2,12.4));

"""


print("Cisco Model {}, {} WAN slots, IOS {}".format("2600XM",2,12.4));

"""

we can manipulate the positions of the strings by doing the below steps of changing the iedexed with {}
"""


print("Cisco Model {0}, {0} WAN slots, IOS {0}".format("2600XM",2,12.4));
print("Cisco Model {1}, {0} WAN slots, IOS {1}".format("2600XM",2,12.4));
print("Cisco Model {2}, {0} WAN slots, IOS {1}".format("2600XM",2,12.4));

'''
result would be like below 
Cisco Model 2600XM, 2600XM WAN slots, IOS 2600XM
Cisco Model 2, 2600XM WAN slots, IOS 2
Cisco Model 12.4, 2600XM WAN slots, IOS 2
'''

model = "latest"
slots = 4;
os = "Windows"


print(f"Model = {model}, Slots available = {slots*2}, Os = {os}");



'''

string slices

>>> string1 = "asjh asdh asdi asdh asfh sffjh dfhvh asd928745javbf92avjdb 2398ryvabj 19y"
>>> string1[10: 15]
'asdi '
>>> string1[10:]
'asdi asdh asfh sffjh dfhvh asd928745javbf92avjdb 2398ryvabj 19y'
>>> string1[:10]
'asjh asdh '
>>> string1[:]
'asjh asdh asdi asdh asfh sffjh dfhvh asd928745javbf92avjdb 2398ryvabj 19y'
>>> 
>>> 
>>> string1[-1]
'y'
>>> string1[-2]
'9'
>>> string1[-1:-9]
''
>>> string1[-9:-2]
'yvabj 1'

string1[]

to fetch last 5 character
string1[-5:]

extracting and removing last 5 element

string1[:-5]

if we want to extract only those character keeping the interval of 2 character then I would be writing like this 

string1[::2]

>>> string1[::3]
'ahs dahs f h d85v9vb3ra y'
>>> 
>>> 
>>> string1[::4]
'a hdsa jf 94v2d3yjy'

string in reversed order

string1[::-1]

string1[start:stop:interval]

>>> string1="0123456789"
>>> 
>>> string1[::3]
'0369'
>>> string1[1::2]
'13579'
>>> 
>>>
>>> string1[::2]
'02468'

Hello I am going to write in dev branch

'''
