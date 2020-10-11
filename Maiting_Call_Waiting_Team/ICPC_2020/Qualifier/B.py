with open('input.txt', 'r') as file:
    a, b, target_year = file.readline().strip().split()
    a = int(a)
    b = int(b)
    target_year = int(target_year)

def first_life(age, target_year, start = 1970, end = 1982):
    if target_year > start and target_year <= end:
        age += target_year - start
        return None, age, True
    else:
        return end, age + (end - start), False

def end_life(age, target_year, start = 1970):
    if target_year > start:
        return None, age + target_year - start, True
    else:
        return None, age, False
    
try:
    age = 0
    year, age, result = first_life(age, target_year, start = 1970, end = 1982)
    if result:
        raise ValueError('True')
    year, age, result = first_life(age, target_year, start = year + 100, end = year + 100 + a)
    if result:
        raise ValueError('True')
    year, age, result = first_life(age, target_year, start = year - 100, end = year - 100 + b)
    if result:
        raise ValueError('True')
    year, age, result = end_life(age, target_year, start = year + 100)
    if result:
        raise ValueError('True')
    age = -1
except Exception as e:
# =============================================================================
#     print(e)
# =============================================================================
    pass

with open('output.txt', 'w') as file:
    file.write(str(age))
