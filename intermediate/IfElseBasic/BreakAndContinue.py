for number in range(10):
    if number == 7:
        print("The 7 number has been reached.. and want to break from the loop", number);
        break;
print("Now control has come out of loop")

list1 = [4,5,6];
list2 = [10,20,30]
for i in list1 :
    for j in list2 :
        if  j==20:
            break;
        print(i * j);
print("Outside of the for loop")

list1 = [4,5,6];
list2 = [10,20,30]
for i in list1 :
    for j in list2 :
        if  j == 20:     # here in this condition I want my code to ignore the line and continue so multiplication with 20 is not happenning and its getting ignored
           continue;
        print(i * j);
print("Outside of the for loop next")



for i in range(10):
    pass  # here pass means do not do anything

# if we use this line this will give an error

#for j in range(10:)   # here I am getting compilation error, so commenting this line of code
