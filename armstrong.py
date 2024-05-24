num = int(input("Enter the number:"))
n = num
armstrong = 0
while(n>0):
    rem = n%10
    armstrong = armstrong + rem*rem*rem
    n = n//10
print(armstrong)
if(num==armstrong):
    print("Armstrong")
else:
    print("Not Armstrong")