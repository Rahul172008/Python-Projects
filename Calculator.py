print("Welcome to our calculator")
print("Press:1 for Addition \nPress:2 for Subraction\nPress:3 for Multiplication\nPress:4 for Divide\nEnter your choicif operation in [1,2,3,4]:" )
operation = input("Enter your choice: ")
if operation.isdigit():
    operation = int(operation)
else:
    print("Invalid input")
    exit()
if operation  in [1 ,2, 3, 4]:
    num1=(input("Enter your First number="))
    if num1.isdigit():
        num1 = int(num1)
    else:
        print("Invalid input")
        exit()
    num2=(input("Enter your second number="))
    if num2.isdigit():
        num2 = int(num2)
    else:
        print("Invalid input")
        exit()
else:
    print("Invalid choice") 
if operation ==1:
    print("Addition is = ",num1+num2)
elif operation ==2:
    print("Subraction is = ",num1-num2)
elif operation ==3:
    print("Multiplication is = ",num1*num2)
elif operation ==4:
    if num2 ==0:
        print("Can not divide by zero")
    else:
     print("Divide is = ",num1/num2)
  