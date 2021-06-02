n = int(input("Enter number:"))

a1 = 0
a2 = 1

if n <= 0:
    print("Invalid range")
elif n == 1:
    print("Fibonacci sequence: ", a1)
else:
    for i in range(0, n):
        print(a1)
        a2 = a1 + a2
        a1 = a2 - a1
