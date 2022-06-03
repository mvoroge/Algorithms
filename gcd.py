from random import randint


def extendGcd(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q
    return x, y, a


num1 = randint(13, 10000)
num2 = randint(13, 10000)

print(num1, num2)
print(extendGcd(num2, num1) if num1 < num2 else extendGcd(num1, num2))
