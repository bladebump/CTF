from pycipher import Autokey

if __name__ == "__main__":
    d = Autokey('AutomaticKey')
    s = 'fftu{2028mb39927wn1f96o6e12z03j58002p}'
    ans = d.decipher(s)
    print(ans)
