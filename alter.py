from connect import connection


def alter_groups():
    c = connection.cursor()
    c.execute('ALTER TABLE if exists groups;')
    connection.commit()


def alter_students():
    c = connection.cursor()
    c.execute('ALTER TABLE students rename column surmane to surname;')
    connection.commit()


def alter_lektors():
    c = connection.cursor()
    c.execute('ALTER TABLE lektors add column surname varchar(30);')
    connection.commit()


def alter_marks():
    c = connection.cursor()
    c.execute('ALTER TABLE marks ALTER COLUMN test_date TYPE date USING test_date::date;')
    # c.execute('UPDATE marks SET test_date = test_date::date;')

    connection.commit()


if __name__ == '__main__':
    # alter_groups()
    # alter_students()
    # alter_lektors()
    alter_marks()