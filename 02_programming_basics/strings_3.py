string = 'Hello:Nick:World'
array = string.split(':')
print(array)
print(type(array))

string_2 = 'My name is ' + array[1]
print(string_2)

string_3 = 'Hello ' + array[2] + "!"
print(string_3)

string_4 = 'My name is Gon and I like Python'
print(string_4.split())
