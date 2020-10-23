with open('input.txt', 'r') as fin:
    _ = fin.readline()
    numbers = list(map(int, fin.readline().split(' ')))

def binary_search(numbers, index):
    left = 0
    right = index - 1
    m = 0
    while True:
        if left > right:
            return m
        m = left + int((right - left)/2)
        if numbers[m] < index:
            left = m + 1
        elif numbers[m] > index:
            right = m - 1
        else:
            return m



min = len(numbers)
index = binary_search(numbers, min)
to_check = numbers[index + 1:]
max = numbers[len(numbers) - 1] + 1
flag = False
res = -1
for i in range(min, max + 1):
    if flag:
        res = i - 1
        break
    temp_numbers = numbers[:index + 1]
    for elem in to_check:
        if elem % i in temp_numbers:
            flag = False
            break
        else:
            temp_numbers.append(elem % i)
            flag = True
print(res)
