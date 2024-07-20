import datetime
from random import randint, sample, choice

from connect import connection
from faker import Faker

fake = Faker()


def insert_groups(quantity: int):
    c = connection.cursor()
    for n in range(quantity):
        c.execute('INSERT INTO groups (number) values (%s)', (f'Group {n + 1}',))
    connection.commit()


def insert_students(quantity: int):
    c = connection.cursor()
    c.execute('SELECT MIN(id) from groups')
    min_number = c.fetchone()[0]
    c.execute('SELECT MAX(id) from groups')
    max_number = c.fetchone()[0]
    for _ in range(quantity):
        c.execute('INSERT INTO students (name, surname, group_id) values (%s, %s, %s)',
                  (fake.first_name(), fake.last_name(), randint(min_number, max_number)))
    connection.commit()


def insert_lektors(quantity: int):
    c = connection.cursor()
    for n in range(quantity):
        c.execute('INSERT INTO lektors (name, surname) values (%s, %s)', (fake.first_name(), fake.last_name()))
    connection.commit()


def insert_subjects(quantity: int):
    subjects_items = ["Mathematics", "Physics", "Chemistry", "Biology",
                      "Computer Science", "History", "Philosophy",
                      "Linguistics", "Literature", "Economics", "Psychology",
                      "Sport", "Programming", "Theory of Automation", "Nature",
                      "English", "Deutsch", "Geography", "Power plants"]
    c = connection.cursor()
    c.execute('SELECT MIN(id) from lektors')
    min_number = c.fetchone()[0]
    c.execute('SELECT MAX(id) from lektors')
    max_number = c.fetchone()[0]

    subjects = sample(subjects_items, quantity)

    for s in subjects:

        c.execute('INSERT INTO subjects (name, lektor_id) values (%s, %s)', (s, randint(min_number, max_number)))

    connection.commit()


def insert_marks(quantity: int):
    c = connection.cursor()
    c.execute('SELECT id FROM students')
    students = c.fetchall()
    c.execute('SELECT MIN(id) from subjects')
    min_number = c.fetchone()[0]
    c.execute('SELECT MAX(id) from subjects')
    max_number = c.fetchone()[0]
    students_list = [s[0] for s in students]
    for _ in range(quantity):
        date = generate_random_work_day()
        subject_id = randint(min_number, max_number)
        for student in students_list:
            c.execute('INSERT INTO marks (value, test_date, student_id, subject_id) VALUES (%s, %s, %s, %s)',
                      (randint(20, 100), date, student, subject_id))
    connection.commit()


start_day = datetime.date(2024, 1, 2)
end_day = datetime.date(2024, 6, 15)


def generate_random_work_day():
    while True:
        random_date = fake.date_between(start_day, end_day)
        if random_date.weekday() < 5:
            return random_date


if __name__ == '__main__':
    insert_groups(3)
    insert_students(50)
    insert_lektors(5)
    insert_subjects(8)
    insert_marks(20)
