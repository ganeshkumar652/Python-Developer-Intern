def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "Error! No number is divide by zero"
    return a/b
while True:
    print("====== Simple Calculator ======")
    print("1.Addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.Division")
    print("5.Exit!")


    choice = input("Enter your choice (1-5) : ")

    if choice=="5":
        print("Its Time to EXIT!")
        break
    
    number1 = float(input("Enter the 1st number : "))
    number2 = float(input("Enter the 2nd number : "))

    

    if choice=="1":
        print(f"The Addition of two number is : {add(number1, number2)}")
    elif choice=="2":
        print(f"The subtraction of two number is : {sub(number1,number2)}")
    elif choice=="3":
        print(f"The Multiplication of two number is : {mul(number1,number2)}")
    elif choice=="4":
        print(f"The Division of two number is :{div(number1,number2)}")
    else:
        print("Invalid Operation")

