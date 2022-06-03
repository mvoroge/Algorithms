from random import randint


def isPrime(num):
    d = 2
    while d * d <= num and num % d != 0:
        d += 1
    return d * d > num


def extendGcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        div, x, y = extendGcd(b % a, a)
    return div, y - (b // a) * x, x


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


def generateKey(p, q):
    n = p * q
    fn = (p - 1) * (q - 1)
    d = 65537
    _, x, y = extendGcd(d, fn)
    if x < 0:
        x += fn
    C = x
    return (n, d), (n, C)


def encrypt(m, publicKey):
    return fastMul(m, publicKey[1], publicKey[0])


def decrypt(c, privateKey):
    return fastMul(c, privateKey[1], privateKey[0])


p = 953
q = 733
publicKey, privateKey = generateKey(p, q)
m = randint(1, p*q)
print(f"Сообщение: {m}")
c = encrypt(m, publicKey)
print(f"Зашифрованное сообщение: {c}")
d = decrypt(c, privateKey)
print(f"Сообщение после расшифровки: {d}")
