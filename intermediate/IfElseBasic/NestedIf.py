x = "Cisco";

if "i" in x:
    if len(x)>3:
        print(x , len(x))

#the above code code is same as the below code

if "i" in x and len(x)>3 :
    print(x, len(x))


list1 = [1,7,9,4];
list2= [6,9,34,1];
for i in list1:
    for j in list2:
        print(i*j);

print("Numbers are as below ::")
for number in range(10):
    if 5 <= number <= 9:
        print(number);