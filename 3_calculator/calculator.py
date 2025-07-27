import re

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

    if equation == 'quit':
        print('Goodbye')
        run = False
    else:
        equation = re.sub(r'[a-zA-Z,.:()" ]', '', equation)
        # equation = re.sub(r'[^0-9+\-*/.]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

        # print('You entered:', previous)


while run:
    perform_math()
