import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

cursor.execute(
    "INSERT INTO students (name, second_name) VALUES (%s, %s)",
    ('Sergio', 'Ramos'))

student_id = cursor.lastrowid
print(f'Студент ID: {student_id}')

books = [("spanish", student_id),
         ("english", student_id)]
add_books = "INSERt INTO books  (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(add_books, books)
print(f'Студент ID: {student_id}')

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) "
               "VALUES ('RM', 'Aug 2012', 'may 2020')")
goup_id = cursor.lastrowid
print(f'ID группы: {goup_id}')

group_query = "UPDATE students  SET group_id = %s WHERE  id = %s"
cursor.execute(group_query, (goup_id, student_id))


def add_subject(subject_name, cursor):
    insert_subj = "INSERT INTO subjects (title) VALUES (%s)"
    cursor.execute(insert_subj, (subject_name,))
    return cursor.lastrowid


subject1 = add_subject('france', cursor)
subject2 = add_subject('spain', cursor)


def add_lessens(title, subject_id, cursor):
    less1 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", (title, subject_id)
    cursor.execute(less1, (title, subject_id))
    return cursor.lastrowid



lesson_id_1 = add_lessens('Geography lesson 1', subject1, cursor)
lesson_id_2 = add_lessens('Geography lesson 2', subject1, cursor)
lesson_id_3 = add_lessens('World History lesson 1', subject2, cursor)
lesson_id_4 = add_lessens('World History lesson 2', subject2, cursor)

marks1 = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values_marks = [(4, lesson_id_1, student_id),
                (5, lesson_id_2, student_id),
                (3, lesson_id_3, student_id),
                (1, lesson_id_4, student_id)]
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

db.commit()
db.close()
