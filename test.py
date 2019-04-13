from pycipher import Autokey
import string
from random import choice
from pyDes import *
import codecs


def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    k = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
    print(k)
    a = k.copy()
    a.reverse()
    for i in range(len(k) - 1):
        a[i] = a[i] + a[-1]
    print(a)
    print(k)
    for i in range(len(k)-1):
        k[i] = k[i] - k[-1]
    k.reverse()
    print(k)

