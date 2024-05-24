def factorial(num):
    if num==1:
        return 1
    else:
        return(num * factorial(num -1))
    
number = int(input("Enter the number: "))
temp = factorial(number)
print("Factorial of",number,"is",temp)