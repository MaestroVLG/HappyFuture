def print_params(a=1, b="mom", c=True):
   print(a, b, c)

print(print_params(b=[1, 2, 3]))



def print_params(a, b, c):
    print(a, b, c)


values_list = [10, "mom", True]
values_dict = {'a': 5, 'b': "dad", 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [2, "matushka"]
print(values_list_2)

print_params(a)
print_params()

