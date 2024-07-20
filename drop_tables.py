from connect import connection


def drop_students():
    c = connection.cursor()
    c.execute('DROP TABLE if exists students cascade')
    connection.commit()


def drop_marks():
    c = connection.cursor()
    c.execute('DROP TABLE if exists marks cascade')
    connection.commit()


def drop_subjects():
    c = connection.cursor()
    c.execute('DROP TABLE if exists subjects cascade')
    connection.commit()


def drop_lektors():
    c = connection.cursor()
    c.execute('DROP TABLE if exists lektors cascade')
    connection.commit()


def drop_groups():
    c = connection.cursor()
    c.execute('DROP TABLE if exists groups cascade')
    connection.commit()


if __name__ == '__main__':
    drop_groups()
    drop_marks()
    drop_lektors()
    drop_students()
    drop_subjects()
