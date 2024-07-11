def apply_all_func(int_list, *functions):

    # Args:
    # int_list: список цифр(int, float)
    # *functions: функции которые можно применить к списку(sorted, len, max, min, sum  и.т.д)
    #
    # Returns:
    #         Словарь где выводится ключ(название функции), а значением является результат работы функции

    result = {}
    for function in functions:
        result[function.__name__] = function(int_list)

    return result

int_list = [1, 2, 3, 4, 5]
functions = [min, max, len, sum, sorted]

results = apply_all_func(int_list, *functions)

print(results)


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))






