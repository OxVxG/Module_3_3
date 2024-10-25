def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

values_list = ['wow', True, 30]
values_dict = {'a': 16, 'b': 'rock', 'c': 22.3}
values_list_2 = [55, False]

print_params()
print_params(a = 3, b = 5)
print_params(b = 5, c = [1, 2, 6])
print_params(c = 1)
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
