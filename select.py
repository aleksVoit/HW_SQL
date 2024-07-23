import logging

import connect
from connect import connection


def task_1():
    """
    to find 5 students with the highest average note at all subjects
    """
    c = connection.cursor()
    c.execute(f'SELECT s.id, s.name, s.surname, AVG(m.value) AS average_note '
              f'FROM students s '
              f'JOIN marks m ON s.id = m.student_id '
              f'GROUP BY s.id, s.name '
              f'ORDER BY average_note DESC '
              f'LIMIT 5')
    result = c.fetchall()
    print(result)


def task_2(subject: str):
    """
    find a student with the highest note at specific subject
    """
    query = """
    SELECT sts.id, sts.name, sts.surname, ROUND(AVG(m.value), 2) as avg_note, s.name
    from marks m
	    join subjects s on s.id = m.subject_id 
	    join students sts on sts.id = m.student_id  
    where s.name = %s
    group by sts.id, s.name  
    order by avg_note desc
    limit 1
    """
    conn = connection.cursor()
    conn.execute(query, (subject,))
    student = conn.fetchall()
    if student:
        print(student)
    else:
        print(f'Students don\'t study {subject}')


def task_3(subject: str):
    """
    to find the average note in groups in specific subject(groups, marks, subjects)
    """
    query = """
    SELECT g.id, g.number, s.name, ROUND(AVG(m.value), 2) as group_avg_note
    FROM marks m
        JOIN students sts on sts.id = m.student_id
        join groups g on g.id = sts.group_id
        join subjects s on s.id = m.subject_id
    where s.name = %s
    group by g.id, s.name
    order by group_avg_note desc
    """
    conn = connection.cursor()
    conn.execute(query, (subject,))
    result = conn.fetchall()
    if result:
        print(result)
    else:
        print(f'Groups don\'t study {subject}')


def task_4():
    """
    to find the average note in all groups at all subjects
    """
    query = """
    SELECT ROUND(AVG(m.value), 2) as avg_note
    FROM marks m
    """
    conn = connection.cursor()
    conn.execute(query)
    result = conn.fetchall()
    if result:
        print(result)
    else:
        print(f'There are no any notes')


def task_5(lektor_first_name: str, lektor_last_name: str, ):
    """
    to find list of subjects which specific lektor (subjects, lektors)
    """
    query = """
    SELECT l.name, l.surname, s.name
    FROM subjects s
        JOIN lektors l on l.id = s.lektor_id
    WHERE l.name = %s AND l.surname = %s
    """
    conn = connection.cursor()
    conn.execute(query, (lektor_first_name, lektor_last_name))
    result = conn.fetchall()
    if result:
        print(result)
    else:
        print(f'There is no such lektor')


def task_6(group: str):
    """
    to find list of students in specific group
    """
    query = """
    SELECT g.id, s.name, s.surname
    FROM students s
        JOIN groups g on g.id = s.group_id
    WHERE g.number = %s
    ORDER BY s.surname
    """
    conn = connection.cursor()
    conn.execute(query, (group,))
    result = conn.fetchall()
    if result:
        print(result)
    else:
        print(f'There is no such group')


def task_7(subject: str, group: str):
    """
    to find student's marks of specific subject in specific group
    """
    query = """
    SELECT m.value, sts.name, sts.surname, s.name, g.number
    FROM marks m
        JOIN students sts ON sts.id = m.student_id
        JOIN groups g ON sts.group_id = g.id
        JOIN subjects s ON m.subject_id = s.id
    WHERE s.name = %s AND g.number = %s
    GROUP BY m.id, sts.id, s.id, g.id
    ORDER BY sts.name
    """
    conn = connection.cursor()
    conn.execute(query, (subject, group))
    result = conn.fetchall()
    if result:
        print(result)
    else:
        print(f'There is no such group or such subject')


def task_8(lektor: str):
    """
    to find an average note which gives specified lektor at his subjects
    """
    query = """
    select l.surname, s.name, ROUND(AVG(m.value), 2) as average_note
        from subjects s
            join marks m on s.id = m.subject_id 
            join lektors l on l.id = s.lektor_id 
        where l.surname  = %s 
        group by s.id, l.id
    """
    conn = connection.cursor()
    conn.execute(query, (lektor,))
    result = conn.fetchall()
    if result:
        print(result)
    else:
        print(f'There is no such teacher')


def task_9(student: str):
    """
    to find the list of subjects which attend a specific student
    """
    query = """
    SELECT s.name, ROW_NUMBER() OVER (ORDER BY s.name) AS subject_number
        FROM students sts
            JOIN marks m ON m.student_id = sts.id
            JOIN subjects s ON s.id = m.subject_id
        WHERE sts.surname = %s
        GROUP BY s.id
    """
    conn = connection.cursor()
    conn.execute(query, (student,))
    result = conn.fetchall()
    if result:
        print(result)
    else:
        print(f'There is no such teacher')


def task_10(student: str, lektor: str):
    """
    to find the list of subjects which specific lektor teach specific student
    """
    query = """
    SELECT ROW_NUMBER() OVER (ORDER BY s.name) AS subject_number, s.name
        FROM subjects s
            JOIN lektors l ON l.id = s.lektor_id
            JOIN marks m ON m.subject_id = s.id
            JOIN students sts ON sts.id = m.student_id
        WHERE sts.surname = %s and l.surname = %s
        GROUP BY s.id
    """
    conn = connection.cursor()
    conn.execute(query, (student, lektor))
    result = conn.fetchall()
    if result:
        print(result)
    else:
        print(f'There is no such teacher')


def add_task_1(student: str, lektor: str):
    """
    to find the average note which specific teacher gives to the specific student
    """
    query = """
    SELECT ROUND(AVG(m.value), 2) as average_note, sts.surname as student, l.surname as lektor
        FROM marks m
            JOIN students sts ON sts.id = m.student_id
            JOIN subjects s ON s.id = m.subject_id
            JOIN lektors l ON l.id = s.lektor_id
        WHERE sts.surname = %s and l.surname = %s
        GROUP BY sts.id, l.id
    """
    conn = connection.cursor()
    conn.execute(query, (student, lektor))
    result = conn.fetchall()
    columns = conn.description
    if result:
        print([col.name for col in columns])
        print(result)
    else:
        print(f'There is no such teacher')


def add_task_2(group: str, subject: str):
    """
    to find the marks of students of specific group at specific subject on last lecture
    """
    query = """
    SELECT m.value, sts.surname, s.name, m.test_date, g.number
    FROM marks m
    JOIN students sts ON sts.id = m.student_id
    JOIN groups g ON g.id = sts.group_id
    JOIN subjects s ON s.id = m.subject_id
    join (
        SELECT MAX(m.test_date) as last_date, s.id as subject
        from marks m
        join subjects s on s.id = m.subject_id
        where s.name = %s
        group by s.id
    )latest_lecture on m.test_date = latest_lecture.last_date and m.subject_id  = latest_lecture.subject
    WHERE g.number = %s AND s.name = %s
    GROUP BY m.id, sts.id, s.name, g.id
    """
    conn = connection.cursor()
    conn.execute(query, (subject, group, subject))
    result = conn.fetchall()
    columns = conn.description
    if result:
        print([col.name for col in columns])
        print(result)
    else:
        print(f'There is no such teacher')


if __name__ == '__main__':
    task_1()
    task_2('English')
    task_3('Nature')
    task_4()
    task_5('Ashley', 'Williamson')
    task_6('Group 3')
    task_7('English', 'Group 2')
    task_8('Edwards')
    task_9('Moran')
    task_10('Thomas', 'Washington')
    add_task_1('Moran', 'Washington')
    add_task_2('Group 2', 'Biology')

