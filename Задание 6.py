# задание 1
ne_chet = []
chet = []
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for lol in matrix:
    for el in row:
        if el % 2 != 0:
            ne_chet.append(el)
        elif el % 2 == 0:
            chet.append(el)
        print(lol, end = '\n')
    print (f'Не чётные числа: {ne_chet}')
    print (f'Кол-во чётных: {len(chet)}')
# задание 2
matrix_1 = [[2, 4, 3, 6], [5, 7, 1, 5]]
matrix_2 = [[2, 9, 0, 2], [3, 4, 7, 6]]
answer_matrix = [[0] * len(matrix_1[0]) for _ in range(len(matrix_1))]
print(answer_matrix)
for lol in range(len(matrix_1)):
    for el in range(len(matrix_1[0])):
        answer_matrix[lol][el] = matrix_1[lol][el] * matrix_2[lol][el]
print (answer_matrix)
for lol2 in answer_matrix:
    print(f'сумма чисел в списке: {sum(lol2)}')
# задание 3
fruits = [['Banana', 'apple'], ['apricot', 'Avocado'],
['lime', 'lemon'], ['Mango', 'grapes']]
fruits_big = []
for lol in fruits:
    for el in lol:
        if el[0].isupper():
            fruits_big.append(el):
print(fruits_big)
# задание 4
random_elements = [['toy', 'bee', 'cheese', 'ear'],
 [False, 'word', '0110110', 10],
 ['happiness', '(」°ロ°)」', 'luck', None],
 ['car', '<- code ->', 4.7, True]]
for spusok_element in random_elements:
    for element in spusok_element:
        for index, element in enumerate(spusok_element, start = 1):
            if index == 2:
                print(f"индекс: {index}, элемент: {element}")
        break 

