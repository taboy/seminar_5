#3Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

data=("12W1B12W3B24W1B")
number=''
code=''
for y in range(len(data)):
    if data[y].isdigit():
        number+=data[y]
    else:
        code+=data[y]*int(number)
        number=""

print(code)


