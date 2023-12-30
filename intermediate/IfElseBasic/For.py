vendors = ["HP","Nortel","Avaya","Junipher","Cisco"];
for each_vendors in vendors:
    print(each_vendors);

user_input = input("Hello User: please say something...")
for letters in user_input.replace(" ",""):
    print(letters);

# This below method will print a string in reverse order
#str = "";
#for letters in  user_input.replace(" ",""):
#    #print(letters)
#    str = letters + str;
#    print(str)

#Now if I want to make string in multiplied way

for letters in user_input.replace(" ",""):
    print(letters)
    print(letters*2)
    print(letters*3)

#* print
for i in range(10):
    print(i * "*");

# I will print one by one router stored in vendors variable using range() method
len(vendors)

list(range(5))

print("in normal order the vendors are as below...")
for element_index in range(len(vendors)):
    print(vendors[element_index])
    #vendors printing in reverse order

#in natural order
for index,element in  enumerate(vendors):
    print(index+1,element)

print("In reverse order the vendors are as below")
for element_index in range(len(vendors)):
    print(vendors[len(vendors)-1-element_index]);

print("in reverse order..")
for element_index,element_reverse in enumerate(vendors):
    print(len(vendors)-element_index,vendors[len(vendors)-1-element_index]);

for element in vendors:
    print(element);
else:
    print("The list has been reached..")

#printing the list in reverse order
for index_reverse in range(len(vendors)):
    print(vendors[len(vendors)-1-index_reverse])