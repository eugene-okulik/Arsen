import mysql.connector as mysql

bd = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = bd.cursor(dictionary=True)
cursor.execute("INSERT INTO students (name, second_name) "
               "VALUES ('Sergio', 'Ramos'")
student_id = cursor.lastrowid
qery = "INSERt INTO books  (title, taken_by_student_id) VALUES (%s, %s)"
value = [("spanish", student_id),
         ("english", student_id)]
cursor.executemany(qery, value)

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) "
               "VALUES ('RM', 'Aug 2012', 'may 2020')")
goup_id = cursor.lastrowid
group_query = "UPDATE students  SET group_id = %s WHERE  id = %s"
cursor.execute(group_query, (goup_id, student_id))

subj = "INSERT INTO subjects (title) VALUES (%s)"
subj_qery = ["футбол", "разминка"]
cursor.executemany(subj, subj_qery)
subj_id = cursor.lastrowid

less1 = "INSERT INTO lessons (title, subject_id) VALUES ('less001', %s)"
cursor.execute(less1, subj_id)
less1_id = cursor.lastrowid

less2 = "INSERT INTO lessons (title, subject_id) VALUES ('less002', %s)"
cursor.execute(less2, subj_id)
less2_id = cursor.lastrowid

less3 = "INSERT INTO lessons (title, subject_id) VALUES ('less002', %s)"
cursor.execute(less3, subj_id + 1)
less3_id = cursor.lastrowid

less4 = "INSERT INTO lessons (title, subject_id) VALUES ('less002', %s)"
cursor.execute(less4, subj_id + 1)
less4_id = cursor.lastrowid

marks1 = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values_marks = [(4, less1_id, student_id),
                (5, less1_id, student_id),
                (3, less1_id, student_id),
                (1, less1_id, student_id)]
cursor.executemany(marks1, values_marks)
marks_id = cursor.lastrowid

sel_marks = "SELECT * FROM  marks WHERE  student_id  = %s"
cursor.execute(sel_marks, student_id)
marks_1 = cursor.fetchall()
print(marks_1)

books_1 = "SELECT * FROM  books   WHERE  taken_by_student_id  = %s"
cursor.execute(books_1, student_id)
books = cursor.fetchall()
print(books)

qery = """
SELECT s.name, s.second_name, b.title, m.value, l.title, su.title AS subject_title
FROM students s
JOIN books b on s.id = b.taken_by_student_id
JOIN `groups` g on s.group_id = g.id
JOIN marks m on s.id = m.student_id
JOIN lessons l on m.lesson_id = l.id
JOIN subjects su on l.subject_id = su.id
WHERE s.id = %s
"""

cursor.execute(qery, student_id)

data = cursor.fetchall()
print(data)
for student in data:
    print(student)

bd.commit()
bd.close()
