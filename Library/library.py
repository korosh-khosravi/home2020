import json
import re
from bottle import run, get, put, post, delete, request
from Library import SQLconnection as SQL


@get('/library/<member_id>')
def get_lib(member_id):
    regex = r"^\d+$"
    if re.search(regex, member_id):
        SQL.execute('''BEGIN; SELECT person.name, person.lastname, book.name, book.author, book.category
                                 FROM ((library INNER JOIN book on book.book_id = library.book_id)
                                 INNER JOIN person on person.person_id = library.person_id)
                                 WHERE library.member_id = {0};'''.format(member_id))
        final = SQL.c.fetchall()
        myjson = json.dumps(final)
        SQL.conn.commit()
        return myjson
    else:
        return "Your Input Incorrect.Try Again"


@post('/library')
def post_lib():
    person_id = request.json.get('person_id')
    book_id = request.json.get('book_id')
    password = request.json.get('pass_word')
    SQL.c.execute('''BEGIN; INSERT INTO library(person_id, book_id, pass_word) 
                 VALUES (%s, %s, %s); END;''', (person_id, book_id, password))
    SQL.conn.commit()
    SQL.c.execute('''BEGIN; SELECT member_id FROM library WHERE person_id = {0};'''.format(person_id))
    pid = SQL.c.fetchall()
    return "Successfully Add.Your member_id Is:{0}".format(pid)


@put('/library/<person_id>')
def updating_lib(person_id):
    regex = r"^\d+$"
    if re.search(regex, person_id):
        password = request.json.get('password')
        SQL.c.execute('''BEGIN; UPDATE library SET pass_word = {0} WHERE person_id = {1};'''.format(password, person_id))
        SQL.conn.commit()
        return 'Password Update.'
    else:
        return "Your Input Incorrect.Try Again"


@delete('/library/<member_id>')
def delete_id(member_id):
    regex = r"^\d+$"
    if re.search(regex, member_id):
        SQL.c.execute('''BEGIN; DELETE FROM library WHERE member_id = {0}'''.format(member_id))
        SQL.conn.commit()
        return 'Successfully Delete.'
    else:
        return "Your Input Incorrect.Try Again"


run(reloader=True, debug=True)
