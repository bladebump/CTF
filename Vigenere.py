from pycipher import vigenere
from pycipher import autokey
import string


def getAllChar(input, decode):
    ans = ''
    j = 0
    for i in range(len(input)):
        if (input[i] not in string.ascii_letters):
            ans += input[i]
        else:
            ans += decode[j]
            j += 1
    return ans


if __name__ == '__main__':
    key = 'AutomaticKey'
    ccc = 'flag{2028ab39927df1d96e6a12b03e58002e}'
    ciphertext = 'fftu{2028mb39927wn1f96o6e12z03j58002p}'
    v = vigenere.Vigenere(key)
    ans1 = v.decipher(ciphertext).lower()
    print(getAllChar(ciphertext, ans1))
    a = autokey.Autokey(key)
    ans2 = a.decipher(ciphertext).lower()
    print(getAllChar(ciphertext, ans2))
