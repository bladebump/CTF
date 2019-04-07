import hashlib


def sha1(string):
    return hashlib.sha1(string).hexdigest()


def calc(strSHA1):
    r = 0
    for i in strSHA1:
        r += int('0x%s' % i, 16)

    return r


def encrypt(plain, key):
    keySHA1 = sha1(key)
    intSHA1 = calc(keySHA1)
    r = []
    for i in range(len(plain)):
        r.append(ord(plain[i]) + int('0x%s' % keySHA1[i % 40], 16) - intSHA1)
        intSHA1 = calc(sha1(plain[:i + 1])[:20] + sha1(str(intSHA1))[:20])

    return ''.join(map(lambda x: str(x), r))


def get_key():
    with open(r"C:\Users\yfq61\Documents\work\jarvisoj\msic\you_need_python\key", "r", encoding='utf-8') as f:
        a = f.read()
        print(a)


if __name__ == '__main__':
    cipherText = '-185-147-211-221-164-217-188-169-205-174-211-225-191-234-148-199-198-253-175-157-222-135-240-229-201-154-178-187-244-183-212-222-164'
    get_key()
