person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

res1 = 'результат операции: 42'
res2 = 'результат операции: 514'
res3 = 'результат работы программы: 9'
a = res3.split()
b = res2.split()
c = res1.split()
d = int((a[-1]))
e = int((b[-1]))
f = int((c[-1]))
print(d + 10, e + 10, f + 10)


students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
st1, st2, st3 = students
sub1, sub2, sub3 = subjects
print(f'Students {st1}, {st2}, {st3} study these subjects: {sub1}, {sub2}, {sub3}')
