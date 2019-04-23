#!/usr/bin/env python
# encoding: utf-8

import string

"""
'a': 8167,
'b': 1492,
'c': 2782,
'd': 4253,
'e': 12702,
'f': 2228,
'g': 2015,
'h': 6094,
'i': 6966,
'j': 153,
'k': 772,
'l': 4025,
'm': 2406,
'n': 6749,
'o': 7507,
'p': 1929,
'q': 95,
'r': 5987,
's': 6327,
't': 9056,
'u': 2758,
'v': 978,
'w': 2360,
'x': 150,
'y': 1974,
'z': 74
"""

cton = lambda x: ord(x) - ord('a')
ntoc = lambda x: chr(x + ord('a'))
# ret = ""
# for k, v in enumerate(content):
#     v = string.lower(v)
#     if v in "{}": ret += v
#     if not v in string.ascii_lowercase:
#         continue
#
#     s = secret[k % len(secret)]
#     ret += ntoc((cton(v) + cton(s)) % 26)
#
# open("cipher", "w").write(ret)

if __name__ == "__main__":
    t = 'xtld'
    s = "celj{sufhhhkkpuadfgfxbbe}"
    for j in range(26):
        t = 'xtld' + ntoc(j)
        for i in range(25):
            if s[i] in string.ascii_letters:
                print(ntoc(((cton(s[i]) - cton(t[i%5])) + 26) % 26), end='')
            else:
                print(s[i],end='')
        print()
