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


def GenPassword(length=8, chars=string.ascii_letters):
    return ''.join([choice(chars) for i in range(length)])


Des_Key = GenPassword().upper()

def DesEncrypt(str):
    k = des(Des_Key, ECB, pad=None, padmode=PAD_PKCS5)
    EncryptStr = k.decrypt(str)
    return EncryptStr.encode('hex')


if __name__ == "__main__":
    f1 = open('123.txt', 'wb')
    f2 = open('enc.txt', 'rb')
    content = f2.readlines()
    res = content
    for i in range(len(res)):
        f1.write(DesEncrypt(res[i].decode('hex')) + '\n')
    f1.close()
    f2.close()
