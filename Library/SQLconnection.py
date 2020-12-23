import psycopg2
from bottle import run
from Library import book, person, Login, library
from Library.book import get, post, delete, put

conn = psycopg2.connect(database='library', host='127.0.0.1', port='5432', user='korosh', password='0012652377')
c = conn.cursor()


def create_table():
    c.execute('''BEGIN; CREATE SEQUENCE IF NOT EXISTS book_book_id_seq START 1000;
                 CREATE TABLE IF NOT EXISTS book(
                 name VARCHAR, author VARCHAR, category VARCHAR,
                 price FLOAT, number INT, book_id INT NOT NULL PRIMARY KEY); END;''')

    c.execute('''BEGIN; CREATE SEQUENCE IF NOT EXISTS person_person_id_seq START 2000;
                 CREATE TABLE IF NOT EXISTS person(
                 name VARCHAR, lastname VARCHAR, age INT, credit FLOAT,
                 person_id INT NOT NULL PRIMARY KEY); END;''')

    c.execute('''BEGIN; CREATE SEQUENCE IF NOT EXISTS library_member_id_seq START 3000;
                 CREATE TABLE IF NOT EXISTS Library(
                 member_id INT NOT NULL PRIMARY KEY, 
                 person_id INT, book_id INT, pass_word INT, 
                 FOREIGN KEY (person_id) REFERENCES person(person_id),
                 FOREIGN KEY (book_id) REFERENCES book(book_id),
                 UNIQUE(member_id, person_id, book_id)); END;''')

    conn.commit()


create_table()


run(reloader=True, debug=True)


