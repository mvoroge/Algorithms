import random
from time import time

from bitarray import bitarray
from bitarray.util import int2ba, ba2int


def rand_int(start, end, seed=None):
    a = 32310901
    b = 1729
    if seed is None:
        seed = int(str(time()).replace('.', ''))
    m = end - start
    return (a * seed + b) % m


class BlumBlumShub(object):
    def __init__(self, length):
        self.length = length

        # self.primes = e(1000)

    def gcd(self, num1, num2):
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 %= num2
            else:
                num2 %= num1
        return num1 or num2

    def is_prime(self, num):
        if num % 2 == 0:
            return num == 2
        d = 3
        while d * d <= num and num % d != 0:
            d += 2
        return d * d > num

    def fast_mul(self, a, b, n):
        res = 1
        while b != 0:
            if b % 2 == 0:
                b = b / 2
                a = (a * a) % n
            elif b % 2 != 0:
                b = b - 1
                res = (res * a) % n
        return res

    def gen_primes(self):
        out_primes = []
        while len(out_primes) < 2:
            curr_prime = rand_int(1, 100000)
            if curr_prime % 4 == 3:
                if self.is_prime(curr_prime):
                    out_primes.append(curr_prime)
        return out_primes

    def coprime(self, n):
        while True:
            ans = random.randint(1, n - 1)
            if self.gcd(ans, n) == 1:
                return ans

    def random_generator(self):
        ps = bitarray('')
        p, q = self.gen_primes()
        n = p * q
        s = self.coprime(n)
        x_now = self.fast_mul(s, 2, n)
        ps += str(x_now % 2)
        for i in range(1, self.length):
            x_now = self.fast_mul(x_now, 2, n)
            ps += str(x_now % 2)
        return ps

    def get_random_bits(self):
        return self.random_generator()

    def get_random_int(self):
        bit_arr = self.random_generator()
        return bit_arr, ba2int(bit_arr)


if __name__ == '__main__':
    bbs_generator = BlumBlumShub(10)
    # for _ in range(5):
    print(bbs_generator.get_random_int())

    # for _ in range(5):
    #     print(bbs_generator.get_random_bits())

