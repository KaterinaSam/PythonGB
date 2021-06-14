print ("Введите строку>")
strUser = input()
strNew = strUser.split(' ')

i = 0
for el in strNew:
    i += 1
    print(f"{i} - {el[:10]}")