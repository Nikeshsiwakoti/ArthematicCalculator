def add(x,y):
    return (x+y)
def subtraction(x,y):
    return (x-y)
def multiplication(x,y):
    return (x*y)
def division(x,y):
    return (x/y)
print("Selection Operation.")
print("1.add")
print("2.subtraction")
print("3.multiplication")
print("4.divison")
choice=input("Enter choice(1/2/3/4):")
num1= float (input("Enter a first Number:"))
num2= float(input("Enter a second Number:"))
if choice =='1':
    print(num1,"+",num2,"=", add(num1,num2))
elif choice =='2':
    print(num1,"-",num2,"=", subtraction(num1,num2))
elif choice =='3':
    print(num1,"*",num2,"=", multiplication(num1,num2))
elif choice =='4':
    print(num1,"/",num2,"=", division(num1,num2))
else:
    print("invalid input")