def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        c = 0
        for i in range(1, res):
            if res % i == 0:
                c += 1
        if c > 1:
            print('Составное')
        else:
            print('Простое')
        return res
    return wrapper

@ is_prime
def sum_three(*args):
    res = 0
    for i in args:
        res += i
    return res


result = sum_three(2, 3, 6)
print(result)
