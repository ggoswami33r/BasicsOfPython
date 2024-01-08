myfile = open("F:\\Python\\Basic Practices\\BasicsOfPython\\FileOperation\\routers.txt");

print(myfile.mode)
#result would be r

print(myfile.read())
# result would be as followed -->'CISCO\nJUNIPER\nHP\nAVAYA\nNORTEL\nARISTA\nLINKEYS'


print(myfile.read(5))
# result would be as follows -->  ''  # here what happening is cursor is at the end of the file after the file read operation
# to change that or if I want my cursor to be appeared in first location then I should use seek method

print(myfile.seek(0))  # if I want my cursor to be positioned at 0th position then I can use seek(0)


print(myfile.tell()) # it tells us at what position the cursor is present

#0
myfile.read(5)
# 'CISCO'

'''
>>> myfile.readline()
'CISCO\n'
>>> myfile.readline()
'JUNIPER\n'
>>> myfile.readline()
'HP\n'
>>> myfile.readline()
'AVAYA\n'
>>> myfile.readline()
'NORTEL\n'
>>> myfile.readline()
'ARISTA\n'
>>> myfile.readline()
'LINKEYS'
>>> myfile.readline()
''

This reflects elements of the routers one by one and then at the end of the file it returns nothing
'''

'''
myfile.readlines() 

['CISCO\n', 'JUNIPER\n', 'HP\n', 'AVAYA\n', 'NORTEL\n', 'ARISTA\n', 'LINKEYS']
'''

"""
>>> for line in myfile.readlines():
	if line.startswith('A'):
		print(line)

		
AVAYA

ARISTA

but first we need to do myfile.seek(0)

"""

'''
to create a file we can use x mode as follows

myfile1 = open("F:\\Python\\Basic Practices\\BasicsOfPython\\FileOperation\\routers.txt","x");
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    myfile1 = open("F:\\Python\\Basic Practices\\BasicsOfPython\\FileOperation\\routers.txt","x");
FileExistsError: [Errno 17] File exists: 'F:\\Python\\Basic Practices\\BasicsOfPython\\FileOperation\\routers.txt'

# the above error occurs because the routers.txt file still exists

>>> myfile1 = open("F:\\Python\\Basic Practices\\BasicsOfPython\\FileOperation\\routers1.txt","x");


>>> myfile1 = open("F:\\Python\\Basic Practices\\BasicsOfPython\\FileOperation\\routers1.txt","r");
>>> myfile1 = open("F:\Python\Basic Practices\BasicsOfPython\FileOperation\routers1.txt","r");
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    myfile1 = open("F:\Python\Basic Practices\BasicsOfPython\FileOperation\routers1.txt","r");
OSError: [Errno 22] Invalid argument: 'F:\\Python\\Basic Practices\\BasicsOfPython\\FileOperation\routers1.txt'
>>> 
>>> myfile1 = open("F:\\Python\\Basic Practices\\BasicsOfPython\\FileOperation\\routers1.txt","r");




for windows path having \ wont work, \\ would work

myfile1 = open(r"F:\Python\Basic Practices\BasicsOfPython\FileOperation\routers1234.txt","w");

another way to remove unicode problem is adding r before the path.

>>> newFile = open(r"F:\Python\Basic Practices\BasicsOfPython\FileOperation\newfile.txt","w");

>>> 
>>> newFile = open(r"F:\Python\Basic Practices\BasicsOfPython\FileOperation\newfile.txt","w+");
>>> 
>>> newFile.write("Hello Python")
12
>>> 
>>> newFile.seek(0)
0
>>> 
>>> newFile.read()
'Hello Python'
>>> 
>>> 
>>> 
>>> newFile = open(r"F:\Python\Basic Practices\BasicsOfPython\FileOperation\newfile.txt","w+");
>>> 
>>> newFile.write("Hello GG")
8
>>> 
>>> newFile.seek(0)
0
>>> newFile.close()


whenever u use w+ or a+ or r + , you need to use either seek(0) or close method to get the content immediately reflected


newFile.closed
True
>>> 

to check whether a a file is closed or not we can use closed

>> with open (r"F:\Python\Basic Practices\BasicsOfPython\FileOperation\newfile1.txt","w") as  f:
	f.write("Hello Python")

	
12
>>> f.closed
True

another way to close a file using with ... as f



>>> newFile = open(r"F:\Python\Basic Practices\BasicsOfPython\FileOperation\newfile.txt","w+");
>>> 
>>> newFile.write("asdjhasj a dasd ioa iohas d iasdf iuasd uiasd ui asdb shfbv uisv uad iuvah uva uhfe")
83
>>> newFile.seek(0)
0
>>> 
>>> newFile.truncate(3)
3
>>> 



'''