print("This is a Simple calculator!")
print("""Choose from the options what you want to do -->
      Addition : 1
      Subtraction : 2
      Multiplication : 3
      Division : 4
      Exit : 5
      """)
while True :
    choice=int(input("Enter your choice 1/2/3/4/5 :"))

    if choice == 1:
        num1=int(input("Enter the first number "))
        num2=int(input("Enter the second number "))
        print("The answer is :", num1 + num2)
    elif choice==2:
        num1=int(input("Enter the first number "))
        num2=int(input("Enter the second number "))
        print("The answer is :", num1 - num2)
    elif choice==3:
        num1=int(input("Enter the first number "))
        num2=int(input("Enter the second number "))
        print("The answer is :", num1 * num2)
    elif choice==4:
        num1=int(input("Enter the first number "))
        num2=int(input("Enter the second number "))
        print("The answer is :", num1 / num2)
    elif choice==5:
        exit()
    else:
        print("Enter a valid choice!")