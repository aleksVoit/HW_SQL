from connect import connection

if __name__ == '__main__':
    c = connection.cursor()
    c.execute('SELECT * FROM students')
    row = c.fetchall()
    print(row)
    connection.commit()
