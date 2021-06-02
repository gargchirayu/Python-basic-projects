num = int(input("Enter number:"))
fac = 1

if num<0:
    print("Negative number invalid")
elif num == 0:
    print("Factorial = 1")
else:
    for i in range(1, num+1):
        fac = fac*i
    print("Factorial = ",fac)