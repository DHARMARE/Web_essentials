num = 12213
temp = num
reverse = 0
while(temp>0):
    rem = temp%10
    reverse = reverse*10 + rem
    temp = temp//10
print("Reverse :",reverse)
if (num==reverse):
    print("Palindrome")
else:
    print("Not palindrome")