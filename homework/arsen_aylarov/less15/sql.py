import mysql.connector as mysql

bd = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = bd.cursor(dictionary=True)
cursor.execute("INSERT INTO students (name, second_name, group_id) "
               "VALUES ('Sergio', 'Ramos', NULL)")
cursor.execute("INSERt INTO books  (title, taken_by_student_id) "
               "VALUES ('football', 23086)")
cursor.execute("INSERt INTO books  (title, taken_by_student_id) "
               "VALUES ('spanish', 23086)")
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) "
               "VALUES ('RM', 'Aug 2012', 'may 2020')")
cursor.execute("UPDATE students  SET group_id = 23080 WHERE  id = 23086")
cursor.execute("INSERT INTO subjects (title) VALUES ('fizra')")
cursor.execute("INSERT INTO subjects (title) VALUES ('obj')")
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('less001', 23123)")
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('less002', 23123)")
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (7, 76454, 23086)")
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (8, 76455, 23086)")
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('les_101', 23122)")
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('les_102', 23122)")
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (11, 76456, 23086)")
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (9, 76457, 23086)")
bd.commit()

cursor.execute("SELECT * FROM  marks WHERE  student_id  = 23086")
print(cursor.fetchall())
cursor.execute("SELECT * FROM  books   WHERE  taken_by_student_id  = 23086")
print(cursor.fetchall())

qery = """
SELECT s.name, s.second_name, b.title, m.value, l.title, su.title AS subject_title
FROM students s
JOIN books b on s.id = b.taken_by_student_id
JOIN `groups` g on s.group_id = g.id
JOIN marks m on s.id = m.student_id
JOIN lessons l on m.lesson_id = l.id
JOIN subjects su on l.subject_id = su.id
WHERE s.id = 23086
"""

cursor.execute(qery)
print(cursor.fetchall())

# data = cursor.fetchall()
# print(data)
# for student in data:
#     print(student['name'])

bd.close()
