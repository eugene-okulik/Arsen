INSERT INTO students (name, second_name, group_id) VALUES ('Oldos', 'Haksli', '1')

INSERT INTO books (title, taken_by_student_id) VALUES ('Nwe world', '22460')

INSERT INTO  `groups` (title, start_date, end_date) VALUES ('Writer', '11.01.2026', '30.05.2026')

-- SELECT * FROM students WHERE name = 'Oldos'

UPDATE students SET group_id = '22136' WHERE  name = 'Oldos'

INSERT INTO subjects (title) VALUE ('History')

INSERT INTO subjects (title) VALUE ('Algebra')

INSERT INTO lessons (title, subject_id) VALUE ('lesson3301', '14177')

INSERT INTO lessons (title, subject_id) VALUE ('lesson3302', '14177')

INSERT INTO lessons (title, subject_id) VALUE ('lesson04', '14178')

INSERT INTO lessons (title, subject_id) VALUE ('lesson03', '14178')

INSERT INTO marks  (value, lesson_id, student_id) VALUE ('4', '75495', '22460')

INSERT INTO marks  (value, lesson_id, student_id) VALUE ('5', '75496', '22460')

INSERT INTO marks  (value, lesson_id, student_id) VALUE ('3', '75497', '22460')

INSERT INTO marks  (value, lesson_id, student_id) VALUE ('4', '75498', '22460')

SELECT * FROM marks WHERE student_id = '22460' 

SELECT * FROM books WHERE taken_by_student_id = '22460' 

SELECT * FROM marks WHERE student_id = '22460'

SELECT 
stud.name,
stud.second_name,
gr.title AS TitleGroups,
b.title AS TitleBooks,
l.title AS TitleLesson,
m.value 
FROM students stud
JOIN `groups` gr ON gr.id = stud.group_id
JOIN marks m ON m.student_id = stud.id 
JOIN lessons l ON m.lesson_id = l.id 
JOIN subjects s ON s.id = l.subject_id
LEFT JOIN books b ON b.taken_by_student_id = stud.id
WHERE stud.id = 22460 
AND s.id IN (14177, 14178)
ORDER BY m.value DESC;
