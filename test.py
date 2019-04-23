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
    s = '$acbedgfihmlonpsrtyx_'
    print(s[17]+s[8]+s[10]+s[4])
    print(s[16]+s[1]+s[13]+s[5]+s[12]+s[10]+s[20]+s[3]+s[18]+s[17]+s[4]+s[15])
    print(s[14]+s[9]+s[14]+s[20]+s[15]+s[1]+s[14]+s[8]+s[20]+s[13]+s[1]+s[10]+s[4])
    print(s[6]+s[4]+s[17]+s[20]+s[11]+s[12]+s[1]+s[5]+s[4]+s[5]+s[20]+s[4]+s[19]+s[17]+s[4]+s[13]+s[15]+s[8]+s[12]+s[13]+s[15])
    print(s[2]+s[9]+s[16])
    print(s[8]+s[13]+s[20]+s[1]+s[16]+s[16]+s[1]+s[18])
    print(s[12]+s[16]+s[5])
    print(s[15]+s[17]+s[16]+s[11]+s[4]+s[13])
    print(s[7]+s[8]+s[11]+s[4]+s[20]+s[6]+s[4]+s[17]+s[20]+s[2]+s[12]+s[13]+s[17]+s[4]+s[13]+s[17]+s[15])

