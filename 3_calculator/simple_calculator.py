def sum(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


print('Select operation')
print('1. Addition\n2. Subtraction\n3. Multiplication\n4. Division')

choice = int(input('Enter your choice: '))

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if choice == 1:
    print(num1, '+', num2, '=', sum(num1, num2))
elif choice == 2:
    print(num1, '-', num2, '=', sub(num1, num2))
elif choice == 3:
    print(num1, '*', num2, '=', mul(num1, num2))
elif choice == 4:
    print(num1, '/', num2, '=', div(num1, num2))
else:
    print('Invalid input')
