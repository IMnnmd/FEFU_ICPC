with open('input.txt', 'r') as fin:
    _ = fin.readline()
    ord = list(map(int, fin.readline().split(' ')))

ans = '0 '
mass = 0
for k in range(1, len(ord)):
    temp_ord = ord[0:k+1]
    operations = 0
    not_sorted = True
    while not_sorted:
        for j in range(len(temp_ord) - 1):
            if temp_ord[j] > temp_ord[j + 1]:
                temp_ord[j+1], temp_ord[j] = temp_ord[j], temp_ord[j+1]
                mass += temp_ord[j + 1]
                ord[j+1], ord[j] = ord[j], ord[j+1]
            elif j == len(temp_ord) - 2:
                not_sorted = False
            else:
                continue
    ans += str(mass) + ' '

ans = ans.strip()



with open('output.txt', 'w') as fout:
    print(ans, file=fout)



