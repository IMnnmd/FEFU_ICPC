import unittest

#### temp ####
class TestStringMethods(unittest.TestCase):
    def test1(self, res):
        self.assertEqual(res, "0 3 6")

    def test2(self, res):
        self.assertEqual(res, "0 0 4 11 11")
############

"""
ВХОД:
В первой строке дано целое число n (2≤n≤200000) — количество серверов.
Во второй строке через пробел записаны n целых чисел w_i (1 ≤ w_i ≤ 100000000) — вес i-го сервера.

ВЫХОД:
В единственной строке выведите через пробел n целых чисел res_i — суммарное количество энергии, необходимое для упорядочивания первых i серверов.
"""

"""
with open("input.txt") as file:
    pass

examples = ["3\n3 1 2", "5\n1 4 3 2 5"] # temp
"""
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



testing = TestStringMethods()   # temp
# testing.test1(ans)          # temp
testing.test2(ans)    # temp

with open('output.txt', 'w') as fout:
    print(ans, file=fout)


"""
res = ""

with open("output.txt", "w") as file:
    file.write(res)
"""
