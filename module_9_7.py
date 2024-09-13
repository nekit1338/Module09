def is_prime(func):
    def wrapper(*args):
        result_01 = func(*args)
        if result_01 < 2:
            print("Число должно быть больше 1")
            return
        if all(result_01 % i != 0 for i in range(2, int(result_01**0.5) + 1)):
            print("Простое")
        else:
            print("Составное")
        return result_01
    return wrapper


@is_prime
def sum_three(*args):
    a = sum(args)
    return a


result = sum_three(2, 3, 6)
print(result)
