letter_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # 字母表


# 根据输入的key生成key列表
def Get_KeyList(key):
    key_list = []
    for ch in key:
        key_list.append(ord(ch.upper()) - 65)
    return key_list


# 加密函数
def Encrypt(plaintext, key_list):
    ciphertext = ""

    i = 0
    for ch in plaintext:
        if 0 == i % len(key_list):
            i = 0
        if ch.isalpha():
            if ch.isupper():
                ciphertext += letter_list[(ord(ch) - 65 + key_list[i]) % 26]
                i += 1
            else:
                ciphertext += letter_list[(ord(ch) - 97 + key_list[i]) % 26].lower()
                i += 1
        else:
            ciphertext += ch
    return ciphertext


# 解密函数
def Decrypt(ciphertext, key_list):
    plaintext = ""
    i = 0
    for ch in ciphertext:  # 遍历密文
        if 0 == i % len(key_list):
            i = 0
        if ch.isalpha():  # 密文为否为字母,如果是,则判断大小写,分别进行解密
            if ch.isupper():
                plaintext += letter_list[(ord(ch) - 65 - key_list[i]) % 26]
                i += 1
            else:
                plaintext += letter_list[(ord(ch) - 97 - key_list[i]) % 26].lower()
                i += 1
        else:  # 如果密文不为字母,直接添加到明文字符串里
            plaintext += ch
    return plaintext


if __name__ == '__main__':
    key = 'AutomaticKey'
    ccc =        'flag{2028ab39927df1d96e6a12b03e58002e}'
    ciphertext = 'fftu{2028mb39927wn1f96o6e12z03j58002p}'
    key_list = Get_KeyList(key)
    plaintext = Decrypt(ccc, key_list)
    print("明文为:\n%s" % plaintext)
