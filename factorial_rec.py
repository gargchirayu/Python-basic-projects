num = int(input("Enter number:"))


def fac(n):
    if n == 1:
        return n
    else:
        return n*fac(n-1)


factorial_ = fac(num)
if num < 0:
    print("Negative number invalid")
elif num == 0:
    print("Factorial = 1")
else:
    print("Factorial = ", factorial_)
