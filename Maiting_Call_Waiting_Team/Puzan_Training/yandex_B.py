with open('input.txt', 'r') as fin:
    text = fin.readline().strip()

count = 0
upper = False
for j in range(len(text)):
    if text[j] == ' ':
        count += 1
text = text.replace(' ', '')
for i in range(len(text)):
    symbol = text[i]
    if upper == False and symbol.isupper():
        if i >= len(text) - 3:
            count += 2
        elif text[i:i+4].isupper():
            upper = True
            count += 3
        else:
            count += 2
    elif upper and symbol.isupper():
        count += 1
    elif upper and symbol.islower():
        if i >= len(text) - 3:
            count += 2
        elif text[i:i+4].islower():
            upper = False
            count += 3
        else:
            count += 2
    else:
        count += 1


with open('output.txt', 'w') as fout:
    print(count, file=fout)