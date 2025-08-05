import re

from simpleeval import simple_eval

print('Calculator')
print('Type \'quit\' to exit\n')

previous = 0
run = True


def perform_math():
    global run
    global previous
    equation = ''

    if previous == 0:
        equation = input('Enter equation: ')
    else:
        equation = input(str(previous))

    if equation.strip().lower() == 'quit':
        print('Goodbye')
        run = False
        return
    else:
        equation = equation.strip()
        equation = re.sub(r'[^0-9+\-*/().]', '', equation)

        try:
            if previous == 0:
                previous = simple_eval(equation)
            else:
                if equation and equation[0] in '+-*/':
                    previous = simple_eval(str(previous) + equation)
                else:
                    previous = simple_eval(equation)
            print("= ", str(previous))
        except Exception as e:
            print("[ERROR]: Invalid input →", e)
            previous = 0


while run:
    perform_math()
