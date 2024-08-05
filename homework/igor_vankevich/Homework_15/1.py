import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

cursor.execute("INSERT INTO students (name, second_name, group_id) values ('Ryan2', 'Gosling2', NULL)")
student_id = cursor.lastrowid
cursor.execute(f"SELECT * FROM students where id = {student_id}")
student = cursor.fetchone()

cursor.execute(f"INSERT INTO books (title, taken_by_student_id) values ('Necronomicon2', {student_id})")
cursor.execute(f"INSERT INTO books (title, taken_by_student_id) values ('pig Pepe2', {student_id})")
cursor.execute(f"INSERT INTO books (title, taken_by_student_id) values ('anno2', {student_id})")

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) values ('neco_book2', 'fed 1080', 'dec 2024')")
group_id = cursor.lastrowid

cursor.execute(f"UPDATE students set group_id = {group_id} WHERE id = {student_id}")

cursor.execute("INSERT INTO subjets (title) values ('math2')")
subject1 = cursor.lastrowid
cursor.execute("INSERT INTO subjets (title) values ('phys2')")
subject2 = cursor.lastrowid

cursor.execute(f"INSERT INTO lessons (title, subject_id) values ('less_math_1.2', {subject1})")
less_phys_1 = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) values ('less_math_2.2', {subject1})")
less_phys_2 = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) values ('less_phys_1.2', {subject2})")
less_math_1 = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) values ('less_phys_2.2', {subject2})")
less_math_2 = cursor.lastrowid

cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) values "
               f"('5', {less_math_1}, {student_id}),"
               f"('3', {less_math_2}, {student_id}),"
               f"('1', {less_phys_1}, {student_id}),"
               f"('4', {less_phys_2}, {student_id})")

db.commit()

mask_query = "SELECT value from marks WHERE student_id = %s"
cursor.execute(mask_query, [student['id']])
marks = cursor.fetchall()
for mark in marks:
    print(mark['value'])

book_query = "SELECT title from books WHERE taken_by_student_id = %s"
cursor.execute(book_query, [student['id']])
books = cursor.fetchall()
for book in books:
    print(book['title'])

select_query = f'''
SELECT st.name, st.second_name, g.title, b.title, m.value, l.title, su.title
FROM students st
join `groups` g
on st.group_id = g.id
join books b
on st.id = b.taken_by_student_id
JOIN marks m
on st.id = m.student_id
JOIN lessons l
on m.lesson_id = l.id
JOIN subjets su
on l.subject_id = su.id
WHERE st.id = %s
and st.name = %s
and st.second_name = %s

'''

cursor.execute(select_query, (student_id, student['name'], student['second_name']))
print(cursor.fetchall())

db.close()
