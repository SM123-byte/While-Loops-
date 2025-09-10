

num = int(input("Enter a number: "))

rev = 0
temp = num

while temp > 0:
    rem = temp % 10
    rev = rem + (rev*10)
    temp = (temp//10)

if rev == num:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")

