first_number = 0
second_number = 1
terms = int(input("enter range"))
i=0

if terms <= 1:
        print(0)
else :
    while i < terms:
        next_num = first_number + second_number
        print(int(next_num))
        first_number = second_number
        second_number = next_num
        i += 1
