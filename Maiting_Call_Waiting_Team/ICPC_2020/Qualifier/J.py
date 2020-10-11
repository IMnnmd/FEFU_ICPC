text = 'jUst DO it!'

def to_str(a):
    return ''.join([str(i) for i in a])

just = [1]*4
do = [1]*2
it = [1]*2

end = []
result = ''
for i in range(0,256):
    result = ''
    str_bin = (8 - len(bin(i)[2:]))*'0' +  bin(i)[2:]
    result += ['j', 'J'][int(str_bin[0])]
    result += ['u', 'U'][int(str_bin[1])]
    result += ['s', 'S'][int(str_bin[2])]
    result += ['t', 'T'][int(str_bin[3])]
    result += ' '
    result += ['d', 'D'][int(str_bin[4])]
    result += ['o', 'O'][int(str_bin[5])]
    result += ' '
    result += ['i', 'I'][int(str_bin[6])]
    result += ['t', 'T'][int(str_bin[7])]
    result += '!'
    
    end.append(result)

with open('output.txt', 'w') as file:
    file.write('\n'.join(end))
