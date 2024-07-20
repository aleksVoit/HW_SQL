from sqlite3 import Error
from connect import connection
from faker import Faker
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('data_logger')
logger.setLevel(logging.INFO)

# fake = Faker()
# name = fake.name()
# logger.info(f'{name}')


def create_table(table_name, table_dict):
    columns_query = ', '.join(f'{key} {value}' for key, value in table_dict.items())
    query = (f'DROP TABLE IF EXISTS {table_name} cascade;'
             f'CREATE TABLE if not exists {table_name} ({columns_query});')
    print(query)
    try:
        c = connection.cursor()
        c.execute(query)
        connection.commit()
    except Error as err:
        logger.info(f'Error: {err}')


def create_my_tables():
    create_table('groups', {'id': 'serial primary key', 'number': 'varchar(30)'})
    create_table('students', {'id': 'serial primary key', 'name': 'varchar(30)',
                              'surname': 'varchar(30)', 'group_id': 'integer',
                              'foreign key (group_id)': 'REFERENCES groups (id) on delete cascade'})
    create_table('lektors', {'id': 'serial primary key', 'name': 'varchar(30)', 'surname': 'varchar(30)'})
    create_table('subjects', {'id': 'serial primary key', 'name': 'varchar(30)',
                              'lektor_id': 'integer',
                              'foreign key (lektor_id)': 'REFERENCES lektors (id) on delete cascade'})
    create_table('marks', {'id': 'serial primary key', 'value': 'integer', 'test_date': 'date',
                           'student_id': 'integer', 'subject_id': 'integer',
                           'foreign key (student_id)': 'REFERENCES students (id) on delete cascade',
                           'foreign key (subject_id)': 'REFERENCES subjects (id) on delete cascade'})


if __name__ == '__main__':
    create_my_tables()
