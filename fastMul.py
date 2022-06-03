from random import randint


def fastMul(a, b, n):
    res = 1
    while b != 0:
        if b % 2 == 0:
            b = b / 2
            a = (a * a) % n
        elif b % 2 != 0:
            b = b - 1
            res = (res * a) % n
    return res


num1, num2, m = randint(1, 100000), randint(1, 100000), randint(1, 100000)
print('\n', num1, num2, m)
print(f'Умножение по алгоритму: {fastMul(num1, num2, m)}')
print(f'Проверка: {(num1 ** num2) % m}')
