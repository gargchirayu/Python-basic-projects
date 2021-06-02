num = int(input("Enter number: "))

flag = False
if num > 1:
    for i in range(2, num):
        # mathematically here, should use num/2, but can leave for now
        if num % 2:
            flag = True
            break

if flag:
    print("Not prime")
else:
    print("Prime")