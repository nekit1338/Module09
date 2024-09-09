def apply_all_func(int_list: list, *functions):
    result = {}
    for func in functions:
        result[func.__name__] = func(int_list)
    return result


list_ = [6, 20, 15, 9]

print(apply_all_func(list_, max, min))
print(apply_all_func(list_, len, sum, sorted))
