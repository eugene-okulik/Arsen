person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

text1 = 'результат операции: 42'
text2 = 'результат операции: 514'
text3 = 'результат работы программы: 9'
txt1_ind = text1.index(':')
txt1 = int(text1[txt1_ind + 1:])
txt2_ind = text2.index(':')
txt2 = int(text2[txt2_ind + 1:])
txt3_ind = text3.index(':')
txt3 = int(text3[txt3_ind + 1:])
print(txt1 + 10, txt2 + 10, txt3 + 10)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
print('Students', ' '.join(students), 'study these subjects:', ' '.join(subjects))
