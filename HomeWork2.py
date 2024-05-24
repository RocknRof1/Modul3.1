def print_params(a=1, b='string', c=True):
    print(a, b, c)

print_params(a=2, b='strong', c=False)
print_params(b=25)
print_params(c=[1, 2, 3])

value_list = ['Hello', 24, False]
value_dict = {'1': 1990, 'string': 55.5, 'True': False}
print_params(*value_list)
print_params(*value_dict)
value_list2 = ['World', False]
print_params(*value_list2, 42)
