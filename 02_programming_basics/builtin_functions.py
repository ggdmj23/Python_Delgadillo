print('Hi')

string = str(5)
print(string)

string = str(5.6)
print(string)

string = str(True)
print(string)

num = int('5')
print(num)

num = int(5.3)
print(num)

num = float('5.3')
print(num)

num = int(float('5.3'))
print(num)

my_float = float(5)
print(my_float)

my_bool = bool('True')
print(my_bool)
print(type(my_bool))

my_ascii = ord('a')
print(my_ascii)

my_char = chr(97)
print(my_char)

len('hello')
print(len('hello'))

length = len(['hello', 'world'])
print(length)

array = [5, 65, 8, 6, 4, 9, 3, 23, 51, 38, 50, 94, 7, 15]
print(f'Original: {array}')

sorted_array = sorted(array)  # Return a new array, it does not change the original
print(sorted_array)

reversed_array = list(reversed(array))
print(reversed_array)

sorted_reversed_array = sorted(array, reverse=True)
print(sorted_reversed_array)

print(f'Original: {array}')

# array = [5, 65, 8, 6, 4, 9, 3, 23, 51, 38, 50, 94, 7, 15]
array.sort(reverse=True)  # Changes the original array
print(array)

array.sort()  # Changes the original array
print(array)
