from random import randint


def extendGcd(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q
    return x, y, a


def is_prime(num):
    if num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num


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


p = int(input('Введите простое число "p": '))
message = int(input('Введите сообщение: '))

message_parts = []
if message < p:
    message_parts.append(message)
else:
    div = message // p
    while sum(message_parts) < message:
        message_parts.append(randint(1, p))
    message_parts[-1] = message - sum(message_parts[:-1])
    print(f'Сообщение численно больше, чем p, поэтому сообщение будет передано по частям в таком виде:'
          f'\n {message_parts}')

output = 0
for m in message_parts:
    while True:
        C1 = randint(1, int(10000))
        if is_prime(C1):
            break
    d1, y, _ = extendGcd(C1, p - 1)
    if d1 < 0:
        d1 += p - 1
    print('\nА: C = ', C1)
    print('А: d = ', d1)

    while True:
        C2 = randint(1, int(10000))
        if is_prime(C2):
            break
    d2, y, _ = extendGcd(C2, p - 1)
    if d2 < 0:
        d2 += p - 1
    print('Б: C =', C2)
    print('Б: d =', d2)

    x1 = fastMul(m, C1, p)
    print('x1 = ', x1)
    # print('Число x1 передано абоненту Б')

    x2 = fastMul(x1, C2, p)
    print('x2 = ', x2)
    # print('Число x2 передано абоненту А')

    x3 = fastMul(x2, d1, p)
    print('x3 = ', x3)
    # print('Число x3 передано абоненту Б')

    x4 = fastMul(x3, d2, p)
    print('x4 = ', x4)

    output += x4


if output == message:
    print(f'\n\nСообщение дошло успешно: {output}')
else:
    print(f'Что-то пошло не так. Вот что вышло: {output}')
