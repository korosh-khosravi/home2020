import json
import re
from bottle import run, get, put, post, delete, request, response, template
from Library import SQLconnection as SQL


@get('/person/<person_id>')
def getting(person_id):
    regex = r"^\d+$"
    if re.search(regex, person_id):
        SQL.c.execute('''BEGIN; SELECT * FROM person WHERE person_id = {0}'''.format(person_id))
        visible = SQL.c.fetchall()
        myjson = json.dumps(visible)
        return myjson
    else:
        return "Your Input Incorrect.Try Again"


@post('/person')
def postingjson():
    name = request.json.get('name')
    lastname = request.json.get('lastname')
    age = request.json.get('age')
    credit = request.json.get('credit')
    SQL.c.execute('''BEGIN; INSERT INTO person (name, lastname, age, credit, person_id) 
    values (%s, %s, %s, %s, NEXTVAL('person_person_id_seq'))''', (name, lastname, age, credit))
    SQL.conn.commit()
    return 'Posting Done.'


@put('/person/<person_id>')
def putting(person_id):
    regex = r"^\d+$"
    if re.search(regex, person_id):
        name = request.json.get('name')
        lastname = request.json.get('lastname')
        age = request.json.get('age')
        credit = request.json.get('credit')
        SQL.c.execute('''BEGIN; UPDATE person SET name = '{}', lastname = '{}', age = {}, credit = {}
                         WHERE person_id = {}'''.format(name, lastname, age, credit, person_id))
        SQL.conn.commit()
        return 'Update Done.'
    else:
        return "Your Input Incorrect.Try Again"


@delete('/person/<person_id>')
def deletee(person_id):
    regex = r"^\d+$"
    if re.search(regex, person_id):
        SQL.c.execute('''BEGIN; DELETE FROM person WHERE person_id = {0}'''.format(person_id))
        SQL.conn.commit()
        return 'Delete Done'
    else:
        return "Your Input Incorrect.Try Again"
