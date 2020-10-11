with open('input.txt', 'r') as file:
    a, b, n = file.readline().strip().split(' ')
    a = int(a)
    b = int(b)
    n = int(n)

c = int((a**2 + b**2) ** 0.5)

start = 0
end = 1 + b

full_cicle = (1 + b) + (1) + (c) + (1) + (1 + a)

cicles = n // full_cicle

n = n - full_cicle*cicles

# =============================================================================
# print(n, cicles)
# =============================================================================

if n >= 0 and n <= 1 + b:
    result = 'metal'
elif n == b + 2:
    result = 'metal'
elif n > b + 2 and n < b + 2 + c:
    result = 'empty'
elif n == b + 2 + c:
    result = 'wood'
elif n > b + 2 + c:
    result = 'wood'

with open('output.txt', 'w') as file:
    file.write(result)
