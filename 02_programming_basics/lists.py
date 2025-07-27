my_list = [1, 2, 3]
print(my_list)

my_list.append(4)
print(my_list)

my_list.remove(4)
print(my_list)

my_list.pop()
print(my_list)

my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list_2 = ['Movies', 23, 'Games', 'Python']
print(my_list_2)

print(['Movies', 'Games', 'Python'][0])
print(my_list_2[1])

string = 'I like ' + my_list_2[0]
print(string)

string = 'I like ' + str(my_list_2[1])
print(string)

my_list_3 = ['Movies', 23, 'Games', 'Python']

for i, item in enumerate(my_list_3):
    print(i, item, type(item))

for i, item in enumerate(my_list_3):
    print(f'index {i}, item {item}, type {type(item)}')
