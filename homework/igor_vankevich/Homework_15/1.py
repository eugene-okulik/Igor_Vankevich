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

cursor.execute(f"INSERT INTO books (title, taken_by_student_id) values ('Necronomicon2', {student_id})")
cursor.execute(f"INSERT INTO books (title, taken_by_student_id) values ('pig Pepe2', {student_id})")
cursor.execute(f"INSERT INTO books (title, taken_by_student_id) values ('anno2', {student_id})")

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) values ('neco_book2', 'fed 1080', 'dec 2024')")
group_id = cursor.lastrowid

cursor.execute(f"UPDATE students set group_id = {group_id} WHERE id = {student_id}")

cursor.execute("INSERT INTO subjets (title) values ('math2')")
cursor.execute("INSERT INTO subjets (title) values ('phys2')")
cursor.execute("SELECT * FROM subjets ORDER BY id DESC LIMIT 2")
subject2, subject1 = cursor.fetchall()

cursor.execute(f"INSERT INTO lessons (title, subject_id) "
               f"values "
               f"('less_math_1.2', {subject1['id']}),"
               f"('less_math_2.2', {subject1['id']}),"
               f"('less_phys_1.2', {subject2['id']}),"
               f"('less_phys_2.2', {subject2['id']})")
cursor.execute("SELECT * FROM lessons ORDER BY id DESC LIMIT 4")
less_phys_2, less_phys_1, less_math_2, less_math_1 = cursor.fetchall()

cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) "
               f"values "
               f"('5', {less_math_1['id']}, {student_id}),"
               f"('3', {less_math_2['id']}, {student_id}),"
               f"('1', {less_phys_1['id']}, {student_id}),"
               f"('4', {less_phys_2['id']}, {student_id})")

db.commit()

cursor.execute(f"SELECT value from marks WHERE student_id = {student_id}")
marks = cursor.fetchall()
for mark in marks:
    print(mark['value'])

cursor.execute(f"SELECT title from books WHERE taken_by_student_id = {student_id}")
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
WHERE st.id = {student_id}
'''

cursor.execute(select_query)
print(cursor.fetchall())

db.close()
