#ЗАДАНИЕ 1 
m = [ 'круг' , 0.25 , 'квадрат' , 'треугольник' , 15 , 'круг' , 'овал' , '10']
m.remove(0.25)
m.remove(15)
m.remove('10')
print (m)
#ЗАДАНИЕ 2
abc = ["A" , "B" , "C" , "D" , "E" , "F" , "G"]
del abc[1:5]
print (abc)
#ЗАДАНИЕ 3
numbers = [1, 4]
numbers.insert(1, 2)
numbers.insert(2,3)
print (numbers)
#ЗАДАНИЕ 4
mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]
mass.sort()
print (mass)
del mass[0:4]
print (mass)
mass.sort(reverse=True)
print (mass)
#ЗАДАНИЕ 5
bolshe_0 = []
nol_0 = []
menshe_0 = []
spusok = int(input("Введите количество чисел: "))
for i in range(spusok):
    i += 1
    num = int(input(f"Введите {i} число: "))
    if num < 0:
        menshe_0.append(num)
    elif num == 0:
        nol_0.append(num)   
    elif num > 0:
        bolshe_0.append(num)
summ_mal = 0
while True:
    if num < 0 in menshe_0:
        summ_mal += num
    else:
        print (summ_mal)
        break
print (bolshe_0)
o = 0
while True:
    if 0 in nol_0:
        o += 1
        nol_0.remove(0)
        nol_0.append("*")
    else:   
        print (f"Количество звёзд: {o} {nol_0}")
        break
