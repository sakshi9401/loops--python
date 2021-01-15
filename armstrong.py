num1 = int(input("enter number"))
sum = 0
n1 = num1

while num1 > 0:
    rem = num1 % 10
    sum = sum + rem ** 3
    num1 = num1 // 10


if sum == n1 :
        print("number is armstrong")

else :
        print("number is not armstrong")
