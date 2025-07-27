def print_something(name='Someone', age='Unknown'):
    print(f'My name is {name} and my age is {age}')


print_something('John')
print_something()
print_something(None, 27)
print_something(age=27)
print_something(age=27, name='John')
