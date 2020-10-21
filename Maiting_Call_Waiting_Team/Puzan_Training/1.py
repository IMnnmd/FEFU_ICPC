with open('input.txt', 'r') as fin:
    _ = fin.readline()
    arr = []
    for i in fin.readlines():
        if len(i) > 1:
            arr.append(list(map(int, i.strip().split(' '))))


def check_res(sum):
    res = 2
    flag = True
    for i in range(1, int(int(sum) ** 0.5)):
        if int(sum) % i == 0:
            flag = False
            break
    if flag:
        res = 0
    return res


sum = 1
for pair in arr:
    sum *= pair[0] / pair[1]
if sum.is_integer():
    res = check_res(sum)
elif (sum - 0.0000001).is_integer():
    res = check_res(sum)
elif (sum + 0.0000001).is_integer():
    res = check_res(sum)
else:
    res = 2

with open('output.txt', 'w') as fout:
    print(res, file=fout)
