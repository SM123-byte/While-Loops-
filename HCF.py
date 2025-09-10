num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))

while (num2 != 0):
    temp = num2
    num2 = num1 % num2
    num1 = temp
    
HCF = num1

print("The HCF for the numbers are: ", HCF)



