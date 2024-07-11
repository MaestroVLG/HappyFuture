data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

count = 0

def func(param):
    global count
    if isinstance(param, int):
        count += param
    elif isinstance(param, str):
        count +=len(param)
    elif isinstance(param, dict):
        for key, value in param.items():
            func(key)
            func(value)
    elif isinstance(param, (list, tuple, set)):
        for i in param:
            func(i)

for i in data_structure:
    func(i)

print(count)