num = int(input("Enter num:"))

add = 0
temp = num
while temp > 0:
    digit = temp % 10
    add += digit ** 3
    temp //= 10

if add == num:
    print("Armstrong Num")
else:
    print("Not")
