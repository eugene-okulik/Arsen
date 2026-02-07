txt1 = 'результат операции: 42, результат: 2, результат работы программы: 209, результат операции: 54 '
txt = txt1.split(' ')

for txt2 in txt:
    if txt2.strip(',').isnumeric():
        txt2 = int(txt2.strip(','))
        print(txt2 + 10)
    else:
        continue
