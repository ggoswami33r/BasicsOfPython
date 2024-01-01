for i in range(5):
    try:
        print(i/0)
    except ZeroDivisionError as e:
        print(e, " --> Error by zero division..");

'''for i in range(10):
    try:
        print(i/0);
    except NameError:
        print("Error created by 0 division")
'''
#the above one is commented because its preventing the below block of code to be executed.


#skipping the exception block for i > 0


for i in range(5):
    try:
        print(i/i)
    except ZeroDivisionError:
        print("Error created by division by 0")



for i in range(10):
    try:
        print(i/1)
    except ZeroDivisionError as e:
        print(e, "--> Error created by division with 0")
    except NameError as e:
        print(e , "--> Error created by naming problem")
    except ValueError as e:
        print(e, "--> Error created by value error")



try:
    print(4/2)
except NameError:
    print("Name Error");
else:
    print(" There is no such error to be highlighted..")
finally:
    print("This block will definitely be executed")


try:
    print (10 / 0)
except NameError as e:
    print(e, "--> Error created by Zero Division")
else:
    print("This else block will be executed")
finally:
    print("This block will definitely be executed at least")