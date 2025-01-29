# 1 - написать ф-цию, которая возвращает ф-цию покторения перых двух символов n раз
# 2 - создать массив ф-ций и применить все ф-ции поочередно к аргументу
# 3 - применить все ф-ции поочередно к массиву аргументов


animal = 'мишка'
animals = ['зайка', 'мишка', 'бегемотик']

#1

def gen_repeat(n):
    def repeater(animal):
        return (animal[:2] + '-') * n + animal
    return repeater


test_1 = gen_repeat(1)
test_2 = gen_repeat(2)

print(test_1(animal))
print(test_2(animal))

#2

funcs = [gen_repeat(n) for n in (1, 2, 3)]
print([func(animal) for func in funcs])

#3


print([func(x) for x in animals for func in funcs])
