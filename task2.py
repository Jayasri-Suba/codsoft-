while True:
    num1 = int(input("enter the 1st number:"))
    num2 = int(input("enter the 2nd number:"))


    print("\n Simple calculator")
    print("1. addition of two numbers")
    print("2. subraction of two numbers")
    print("3. multiplication of two numbers")
    print("4.division of teo numbers")
    print("5. exit")

    choice = input("enter your choice")
    if choice == "1":
        add = num1 + num2
        print("addition of two numbers:",add)
    elif choice == "2":
        sub = num1 - num2
        print("subraction oftwo numbers:",sub)
    elif choice == "3":
        multi = num1 * num2
        print("multiplication of two numbers:",multi)
    elif choice == "4": 
        if num2 != 0:
            div = num1 / num2
            print("division of two numbers:",div)
        else:
            print("division by zero is not possible")
    elif choice == "5":
         print("exiting.......")
    break
else:
    print("invalid choice") 