import os
import datetime

base_path = os.path.dirname(__file__)
hw_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(hw_path, 'eugene_okulik', 'hw_13', 'data.txt')


with open(file_path, 'r') as d_file:
    lines = d_file.readlines()
    line1 = lines[0]
    line2 = lines[1]
    line3 = lines[2]
    l1 = str(line1[3:line1.index(' -')])
    l2 = str(line2[3:line1.index(' -')])
    l3 = str(line3[3:line1.index(' -')])
    date1 = datetime.datetime.strptime(l1, '%Y-%m-%d %H:%M:%S.%f')
    date2 = datetime.datetime.strptime(l2, '%Y-%m-%d %H:%M:%S.%f')
    date3 = datetime.datetime.strptime(l3, '%Y-%m-%d %H:%M:%S.%f')
    date_now = datetime.datetime.now()
    now = date_now - date3
    print(date1 + datetime.timedelta(weeks=1))
    print(datetime.datetime.strftime(date2, '%A'))
    print(now.days)
