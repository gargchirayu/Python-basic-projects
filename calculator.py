print("Mini Calculator\n===============\n")
op1 = float(input("Enter operand 1: "))
op = input("Enter operation: ")
op2 = float(input("Enter operand 2: "))
flag = 0

if op == '+':
    result = op1 + op2
elif op == '-':
    result = op1 - op2
elif op == '*':
    result = op1 * op2
elif op == '/':
    result = op1 / op2
elif op == '^':
    result = op1 ** op2
elif op == '%':
    result = op1 % op2
else:
    flag = 1
    print("Invalid operation")

if flag == 0:
    print("\nResult: ", result)