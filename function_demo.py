def addition():
    num1 = int(input("Enter the value for num1"))
    num2 = int(input("Enter the value for num2"))
    result = num1 + num2
    print("Result of Addition:",result)

def subtraction(x,y):
    result = x - y
    print("Result of Subtraction:",result)

def division():
    n1 = int(input("Enter the value for n1:"))
    n2 = int(input("Enter the value for n2:"))
    result = n1//n2
    return result

def multiplication(x1,x2):
    return x1*x2

addition()
subtraction(10,5)
print("Result of division:",division())
print("Result of multiplication:",multiplication(2,2))