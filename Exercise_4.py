import colorama
import re

colorama.init()
start = "\033[1;31m"
end = "\033[0;0m"
str = input("Введите предложение на английском. ")
pattern = r'^The .* end$'
if re.match(pattern, str):
    print("1) Начинается ли предложение с The и заканчивается на end - ", start + "True" + end)
else:
    print("1) Начинается ли предложение с The и заканчивается на end - ", start + "False" + end)
print("2) Количество символов в предложении - ", len(str))
count = 0
glasn = ['a', 'e', 'i', 'o', 'u']
stroka = ""
flag = False
for i in range(len(str)):
    for k in range(len(glasn)):
        if glasn[k] == str[i]:
            flag = True
            count += 1
    if flag:
        stroka += start + str[i] + end
        flag = False
    else:
        stroka += str[i]
print("3) Количество гласных [a, e, i, o, u] в предложении - ", count)
print(stroka)
print("4) Все символы в нижнем регистре - ", start + str.lower() + end)
a = str.replace("ugly", start + "beauty" + end)
print("5) Заменяет ugly на beauty в предложении - ", a)
