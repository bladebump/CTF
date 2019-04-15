import base58


def encode(s: str):
    return base58.b58encode(s.encode('utf-8')).decode('utf-8')


def decode(s: str):
    return base58.b58decode(s.encode('utf-8')).decode('utf-8')


if __name__ == "__main__":
    print(decode('D9cS9N9iHjMLTdA8YSMRMp'))
