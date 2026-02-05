person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

res1 = 'результат операции: 42'
res2 = 'результат операции: 514'
res3 = 'результат работы программы: 9'
a = int(res3.split()[-1])
b = int(res2.split()[-1])
c = int(res1.split()[-1])
print(a + 10, b + 10, c + 10)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
print('Students', ' '.join(students), 'study these subjects:', ' '.join(subjects))
