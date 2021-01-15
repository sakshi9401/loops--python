
for i in range(100 , 200):

    n = i

    sum = 0

    while i > 0:

        rem = i % 10

        sum = sum + rem ** 3

        i = i // 10

    if sum == n:

        print("number is armstrong" , int(sum))




