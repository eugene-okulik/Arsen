INSERT INTO students (name, second_name, group_id) VALUES ('Sergio', 'Ramos', 1)

INSERt INTO books  (title, taken_by_student_id) VALUES ('futball', 23020)

INSERt INTO books  (title, taken_by_student_id) VALUES ('spanish', 23020)

INSERT INTO `groups` (title, start_date, end_date) VALUES ('RM', 'Aug 2012', 'may 2020')

INSERT INTO `groups` (title, start_date, end_date) VALUES ('psg', 'nov 2025', 'oct 2026')

UPDATE students  SET group_id = 22840 WHERE  id = 23020 

INSERT INTO subjects (title) VALUES ('fizra')

INSERT INTO subjects (title) VALUES ('obj')

INSERT INTO lessons (title, subject_id) VALUES ('less_28', 23043)

INSERT INTO lessons (title, subject_id) VALUES ('less_15', 23043)

INSERT INTO marks (value, lesson_id, student_id) VALUES (4, 76396, 23020)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('five', 76397, 23020)

INSERT INTO lessons (title, subject_id) VALUES ('les_1_obj', 23048)	

INSERT INTO lessons (title, subject_id) VALUES ('les_2_obj', 23048)	

INSERT INTO marks (value, lesson_id, student_id) VALUES (10, 76409, 23020)

INSERT INTO marks (value, lesson_id, student_id) VALUES (4, 76408, 23020)

SELECT * FROM  marks WHERE  student_id  = 23020

SELECT * FROM  books   WHERE  taken_by_student_id  = 23020

SELECT s.name, s.second_name, b.title, m.value, l.title, su.title AS subject_title 
FROM students s 
JOIN books b on s.id = b.taken_by_student_id   
JOIN `groups` g on s.group_id = g.id
JOIN marks m on s.id = m.student_id 
JOIN lessons l on m.lesson_id = l.id 
JOIN subjects su on l.subject_id = su.id
WHERE s.id = 23020 

			  









