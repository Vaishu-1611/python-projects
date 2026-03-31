a = int(input('enter the vale of 1st number: '))
b = int(input("enter the value of second number: "))
op = input("enter the operator(+,-.*,/,%,//,**): ")

if op == '+':
    print(a + b )
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
elif op == '%':
    print(a % b)
elif op == '//':
    print(a // b)
elif op == '**':
    print(a ** b)
else:
    print("invalid operator")
