from connect import connection


def truncate_groups():
    c = connection.cursor()
    c.execute('TRUNCATE TABLE groups cascade;')
    connection.commit()


def truncate_students():
    c = connection.cursor()
    c.execute('TRUNCATE TABLE students cascade;')
    connection.commit()


def truncate_subjects():
    c = connection.cursor()
    c.execute('TRUNCATE TABLE subjects cascade;')
    connection.commit()


def truncate_marks():
    c = connection.cursor()
    c.execute('TRUNCATE TABLE marks cascade;')
    connection.commit()


if __name__ == '__main__':
    # truncate_groups()
    # truncate_students()
    # truncate_subjects()
    truncate_marks()
