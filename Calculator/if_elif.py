#buiilding a Calculator using if elif function.

a = int(input("Enter a first number: "))
b = input("Enter the operator: ")
c = int(input("Enter a second number: "))

if b == '+':
    print(a+c)
elif b == '-':
    print(a-c)
elif b == '*':
    print(a*c)
elif b == "/":
    print(a/c)
elif b == "%":
    print(a%c)
else:
    print("invalid operator")