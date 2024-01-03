'''>> > global my_var = 10;
SyntaxError: invalid
syntax
>> > global my_var=10;
SyntaxError: invalid
syntax
>> > my_var = 10;
>> >

def my_function():
    global my_var;
    print(my_var);
    my_var = 10;

>> > my_function()
10
>> >

def my_function():
    global my_var;
    print(my_var);
    my_var = 220;

>> > my_function()
10
>> > '''