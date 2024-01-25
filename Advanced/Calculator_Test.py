import math

while True:
    print(
        "\nChoose the operation you want to perform .. \n 1 -- Addition \n 2 -- Subtraction \n 3 -- Multiplication \n"
        " 4 -- Division \n 5 -- Modulo \n 6 -- Raising to a power \n 7 -- Square root \n 8 -- Logarithm \n 9 -- Sine \n 10 -- Cosine \n"
        " 11 -- Tangent ");

    oper = input("\n\nYour Option from the menu ..");

    if oper == "1":
        firstValue = float(input("\nEnter First Value.."));
        secondValue = float(input("\nEnter Second Value.."));

        print("\n The Addition result is " + str(firstValue + secondValue) + "\n");
        back = input("Y to continue any other operation else N to exit \n");

        if back == "Y" or "y":
            continue;
        else:
            break;

    elif oper == "2":
        firstValue = float(input("\nEnter First Value.."));
        secondValue = float(input("\nEnter Second Value.."));

        print("\n The Subtraction result is " + str(firstValue - secondValue) + "\n");
        back = input("Y to continue any other operation else N to exit \n");

        if back == "Y" or "y":
            continue;
        else:
            break;
    elif oper == "3":
        firstValue = float(input("\nEnter First Value.."));
        secondValue = float(input("\nEnter Second Value.."));

        print("\n The multiplication result is " + str(firstValue * secondValue) + "\n");
        back = input("Y to continue any other operation else N to exit \n");

        if back == "Y" or "y":
            continue;
        else:
            break;

    elif oper == "4":
        firstValue = float(input("\nEnter First Value.."));
        secondValue = float(input("\nEnter Second Value.."));

        print("\n The Division result is " + str(firstValue / secondValue) + "\n");
        back = input("Y to continue any other operation else N to exit \n");

        if back == "Y" or "y":
            continue;
        else:
            break;
    elif oper == "5":
        firstValue = float(input("\nEnter First Value.."));
        secondValue = float(input("\nEnter Second Value.."));

        print("\n The Modulo result is " + str(firstValue % secondValue) + "\n");
        back = input("Y to continue any other operation else N to exit \n");

        if back == "Y" or "y":
            continue;
        else:
            break;
    elif oper == "6":
        firstValue = float(input("\nEnter First base.."));
        secondValue = float(input("\nEnter the power Value.."));

        print("\n The Power result is " + str(math.pow(firstValue, secondValue)) + "\n");
        back = input("Y to continue any other operation else N to exit \n");

        if back == "Y" or "y":
            continue;
        else:
            break;
    elif oper == "7":
        firstValue = float(input("\nEnter the number for which you want to have root of this number.."));
        secondValue = float(input("\nEnter the root Value.."));

        print("\n The Square root result is " + str(math.sqrt(firstValue, secondValue)) + "\n");
        back = input("Y to continue any other operation else N to exit \n");

        if back == "Y" or "y":
            continue;
        else:
            break;
    elif oper == "8":
        logNumber = float(input("\nEnter the number for which you want to have logarithmic value base 2.."));

        print("\n The Logarithmic result is " + str(math.log(logNumber, 2)) + "\n");
        back = input("Y to continue any other operation else N to exit \n");

        if back == "Y" or "y":
            continue;
        else:
            break;
    elif oper == "9":
        angleDegree = float(input("\nEnter the angle degree for which you want to have sin value.."));

        print("\n The sin result is " + str(math.sin(math.radians(angleDegree))) + "\n");
        back = input("Y to continue any other operation else N to exit \n");

        if back == "Y" or "y":
            continue;
        else:
            break;
    elif oper == "10":
        angleDegree = float(input("\nEnter the angle degree for which you want to have cosine value.."));

        print("\n The Cosine result is " + str(math.cos(math.radians(angleDegree))) + "\n");
        back = input("Y to continue any other operation else N to exit \n");

        if back == "Y" or "y":
            continue;
        else:
            break;
    elif oper == "11":
        angleDegree = float(input("\nEnter the angle degree for which you want to have tangent value.."));

        print("\n The Tangent result is " + str(math.tan(math.radians(angleDegree))) + "\n");
        back = input("Y to continue any other operation else N to exit \n");

        if back == "Y" or "y":
            continue;
        else:
            break;
    else:
        print("\nInvalid Option\n");
        continue;