str1 = input(" ")
lil = str1.split()
lenn = 0
for i in lil:
    lenn += 1
lil_naoborot = lil[::-1]
str_answer = ""
for i in range(lenn):
    if i != (lenn - 1):
        str_answer += lil_naoborot[i]
    elif i == (lenn -1):
        str_answer += " " + lil_naoborot[i]
print(str_answer)