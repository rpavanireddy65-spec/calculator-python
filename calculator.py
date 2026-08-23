import math
def calculator():
    while True:
        print("\n===== PYTHON CALCULATOR =====\n")
        print("1.Addition")
        print("2.Substraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Modulus")
        print("6.Power")
        print("7.Square Root")
        print("8.Percentage")
        print("9.Exit")
        choice=input("Enter your choice: ")
        if choice=="9":
            print("Thank you for using the calculator!")
            break
        try:
            if choice=="1":
                a=float(input("Enter first number: "))
                b=float(input("Enter second number: "))
                print("Result =",a+b)
            elif choice=="2":
                            a=float(input("Enter first number: "))
                            b=float(input("Enter second number: "))
                            print("Result =",a-b)
            elif choice=="3":
                            a=float(input("Enter first number: "))
                            b=float(input("Enter second number: "))
                            print("Result =",a*b)
            elif choice=="4":
                            a=float(input("Enter first number: "))
                            b=float(input("Enter second number: "))
                            print("Result =",a/b)
            elif choice=="5":
                            a=float(input("Enter first number: "))
                            b=float(input("Enter second number: "))
                            print("Result =",a%b)
            elif choice=="6":
                            a=float(input("Enter first number: "))
                            b=float(input("Enter second number: "))
                            print("Result =",a**b)
            elif choice=="7":
                            a=float(input("Enter first number: "))
                            if a<0:
                                    print("Square root of nagative number is not supported.")
                            else:
                                    print("Result=",math.sqrt(a))
                            
            elif choice=="8":
                            number=float(input("Enter number: "))
                            percentage=float(input("Enter percentage: "))
                            print("Result =",(number*percentage)/100)
            else:
                    print("Invalid choice!")
        except ValueError:
                print("Please enter valid numbers.")
calculator()
            
            
            