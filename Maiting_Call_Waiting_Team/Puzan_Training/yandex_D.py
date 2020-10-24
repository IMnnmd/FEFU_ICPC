with open('input.txt', 'r') as fin:
    n, k, r = map(int, fin.readline().split(' '))
    numbas = list(map(int, fin.readline().split(' ')))

def binary_search(numbers, index):
    left = 0
    right = index - 1
    m = 0
    while True:
        if left > right:
            return m + 1
        m = left + int((right - left)/2)
        if numbers[m] < index:
            left = m + 1
        elif numbers[m] > index:
            right = m - 1
        else:
            return m
#MYASO
for i in range(r):
    sum = 0
    for k_r in range(k):
        sum += numbas[k_r]
    for i in range(len(numbas) - 1):
        numbas[i] = numbas[i+1]
    ind = binary_search(numbas, sum)
    numbas.pop(-1)
    if ind == len(numbas):
        numbas.append(sum)
    else:
        numbas.insert(ind, sum)

ans = ''
for i in range(len(numbas)):
    ans += str(numbas[i]) + ' '
with open('output.txt', 'w') as fout:
    print(ans, file=fout)
