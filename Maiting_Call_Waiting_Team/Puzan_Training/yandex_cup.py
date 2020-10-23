with open('input.txt', 'r') as fin:
    b, c = map(int, fin.readline().split(' '))
    r, d = map(int, fin.readline().split(' '))

res = 0
operations = False
million = 10**6
while operations == False:
    operations = True
    while c >= r:
        if c - r == 0:
            d += c
        else:
            d += c - r
        c -= r
        res += 1
        operations = False
    if r // million < 0:
        x = 1
    else:
        x = 1 + r // million
    while x*million - r <= d and b >= x:
        d -= x*million - r
        b -= x
        c += x*million - r
        res += 1
        operations = False
    if (x-1)*million + c >= r and b >= (x-1):
        d += abs((x-1)*million - r)
        c -= abs((x-1)*million - r)
        b -= x-1
        res += 1
        operations = False


with open('output.txt', 'w') as fout:
    print(res, file=fout)