str1 = input("Напишите список чисел через запятую: ")
lil = str1.split(",")
lenn = 0
for i in lil:
    lenn += 1
summ = 0
n = 0
while n != lenn:
    summ += int(lil[n])
    n += 1
print(summ)
print(summ/lenn)
max1 = 0
n = 0
while n != lenn:
    if int(max1) < int(lil[n]):
        max1 = lil[n]
    n += 1
print(max1)