if __name__ == "__main__":
    key = ['000', '01', '00101', '110', '00111', '111', '10', '00100', '00110']
    ans = ['a', 'd', 'g', 'f', 'l', '0', '5', '{', '}']

    s = '11000111000001010010010101100110110101111101110101011110111111100001000110010110101111001101110001000110'
    p = []
    i = 0
    while i < len(s):
        for k in range(len(s)):
            if s[i:i + k] in key:
                p.append(ans[key.index(s[i:i + k])])
                i = i + k
                break
    temp = ''.join(p)[5:-1]
    print(temp)
    p = []
    for i in range(0, len(temp), 2):
        p.append(chr(int('0x' + temp[i:i + 2], 16)))
    print(''.join(p))
