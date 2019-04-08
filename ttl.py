if __name__ == "__main__":
    with open(r"D:\ctf\match\xihulunjian\ttl\ttl.txt", 'r') as f:
        lines = f.readlines()
        temp = []
        for line in lines:
            n = int(line.split('=')[1])
            if n == 63:
                temp.append(0)
            elif n == 127:
                temp.append(1)
            elif n == 191:
                temp.append(2)
            elif n == 255:
                temp.append(3)
            else:
                print(n)
    print(temp[:100])
    ans = []
    for i in range(0, len(temp), 4):
        ans.append((temp[i] << 6) + (temp[i + 1] << 4) + (temp[i + 2] << 2) + (temp[i + 3]))
    print(ans)
    with open(r'D:\ctf\match\xihulunjian\ttl\test','wb') as f:
        for i in ans:
            f.write(chr(i).encode('utf-8'))
    print(len(ans))