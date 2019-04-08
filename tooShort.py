v = {}
vist = {}


def build(g):
    for i in g:
        if i[0] not in v:
            v[i[0]] = set([i[1]])
        else:
            v[i[0]].add(i[1])
        if i[1] not in v:
            v[i[1]] = set([i[0]])
        else:
            v[i[1]].add(i[0])


if __name__ == "__main__":
    g = [('FloraPrice', 'E11'), ('FloraPrice', 'E9'), ('FloraPrice', '75D}'), ('NoraFayette', 'E11'),
         ('NoraFayette', 'E10'), ('NoraFayette', 'E13'), ('NoraFayette', 'E12'), ('NoraFayette', 'E14'),
         ('NoraFayette', 'E9'), ('NoraFayette', 'E7'), ('NoraFayette', 'E6'), ('E10', 'SylviaAvondale'),
         ('E10', 'MyraLiddel'), ('E10', 'HelenLloyd'), ('E10', 'KatherinaRogers'), ('VerneSanderson', 'E7'),
         ('VerneSanderson', 'E12'), ('VerneSanderson', 'E9'), ('VerneSanderson', 'E8'), ('E12', 'HelenLloyd'),
         ('E12', 'KatherinaRogers'), ('E12', 'SylviaAvondale'), ('E12', 'MyraLiddel'), ('E14', 'SylviaAvondale'),
         ('E14', '75D}'), ('E14', 'KatherinaRogers'), ('FrancesAnderson', 'E5'), ('FrancesAnderson', 'E6'),
         ('FrancesAnderson', 'E8'), ('FrancesAnderson', 'E3'), ('DorothyMurchison', 'E9'), ('DorothyMurchison', 'E8'),
         ('EvelynJefferson', 'E9'), ('EvelynJefferson', 'E8'), ('EvelynJefferson', 'E5'), ('EvelynJefferson', 'E4'),
         ('EvelynJefferson', 'E6'), ('EvelynJefferson', 'E1'), ('EvelynJefferson', 'E3'), ('EvelynJefferson', 'E2'),
         ('RuthDeSand', 'E5'), ('RuthDeSand', 'E7'), ('RuthDeSand', 'E9'), ('RuthDeSand', 'E8'), ('HelenLloyd', 'E11'),
         ('HelenLloyd', 'E7'), ('HelenLloyd', 'E8'), ('OliviaCarleton', 'E11'), ('OliviaCarleton', 'E9'),
         ('EleanorNye', 'E5'), ('EleanorNye', 'E7'), ('EleanorNye', 'E6'), ('EleanorNye', 'E8'),
         ('E9', 'TheresaAnderson'), ('E9', 'PearlOglethorpe'), ('E9', 'KatherinaRogers'), ('E9', 'SylviaAvondale'),
         ('E9', 'MyraLiddel'), ('E8', 'TheresaAnderson'), ('E8', 'PearlOglethorpe'), ('E8', 'KatherinaRogers'),
         ('E8', 'SylviaAvondale'), ('E8', 'BrendaRogers'), ('E8', 'LauraMandeville'), ('E8', 'MyraLiddel'),
         ('E5', 'TheresaAnderson'), ('E5', 'BrendaRogers'), ('E5', 'LauraMandeville'), ('E5', 'CharlotteMcDowd'),
         ('E4', 'CharlotteMcDowd'), ('E4', 'TheresaAnderson'), ('E4', 'BrendaRogers'), ('E7', 'TheresaAnderson'),
         ('E7', 'SylviaAvondale'), ('E7', 'BrendaRogers'), ('E7', 'LauraMandeville'), ('E7', 'CharlotteMcDowd'),
         ('E6', 'TheresaAnderson'), ('E6', 'PearlOglethorpe'), ('E6', 'BrendaRogers'), ('E6', 'LauraMandeville'),
         ('E1', 'LauraMandeville'), ('E1', 'BrendaRogers'), ('E3', 'TheresaAnderson'), ('E3', 'BrendaRogers'),
         ('E3', 'LauraMandeville'), ('E3', 'CharlotteMcDowd'), ('E3', 'flag{'), ('E2', 'LauraMandeville'),
         ('E2', 'TheresaAnderson'), ('KatherinaRogers', 'E13'), ('E13', 'SylviaAvondale')]
    build(g)
    start = 'flag{'
    end = '75D}'
    q = [start]
    vist[start] = 0
    while (len(q) != 0):
        p = q[0]
        q.remove(p)
        for i in v[p]:
            if i not in vist:
                vist[i] = p
                q.append(i)
    p = end
    q = start
    ans = []
    while(p != q):
        ans.append(p)
        p = vist[p]
    ans.append(start)
    ans.reverse()
    print(''.join(ans))