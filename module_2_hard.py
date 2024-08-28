import random
def divisors(the_num):
    d = []
    for i in range(3, the_num + 1):
        if the_num % i == 0:
            d.append(i)
    return d


def pairs(d):
    p = ''
    for i in d:
        for j in range(1, i // 2 + 1):
            if j != i - j:
                p += str(j) + str(i - j)
    return p


the_range = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
the_number = random.choice(the_range)
print(the_number)
the_password = pairs(divisors(the_number))
print(the_password)
