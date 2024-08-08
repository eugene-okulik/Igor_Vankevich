import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

base_path = os.path.dirname(__file__)
hw_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(hw_path, 'eugene_okulik', 'lesson_16', 'hw_data', 'data.csv')

with open(file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)

select_query = '''
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
WHERE st.name = %s
and st.second_name = %s
and g.title = %s
and b.title = %s
and su.title = %s
and l.title = %s
and m.value = %s
'''

undiscovered_query = []

for row in data:
    empty = []
    cursor.execute(select_query, (
        row['name'],
        row['second_name'],
        row['group_title'],
        row['book_title'],
        row['subject_title'],
        row['lesson_title'],
        row['mark_value']
    )
    )
    if cursor.fetchall() == empty:
        undiscovered_query.append(row)

for row in undiscovered_query:
    print(row)

db.close()
