from bottle import run, get, request, post, delete, put
import sqlite3
import json

connect = sqlite3.connect('Employee')
c = connect.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS PERSON 
             (NAME varchar(10), LNAME varchar(10), AGE int, NATIONCODE int)''')


@post('/API')
def posting():
    name = request.json.get('name')
    lname = request.json.get('lname')
    age = request.json.get('age')
    nationcode = request.json.get('nationcode')
    c.execute('''INSERT INTO PERSON (NAME, LNAME, AGE, NATIONCODE)
                 VALUES (?,?,?,?)''', (name, lname, age, nationcode))
    connect.commit()
    return 'ok'


@get('/API/<id>')
def get_code(id):
    query = "SELECT * FROM PERSON WHERE NATIONCODE= {}".format(id)
    visible = c.execute(query).fetchall()
    connect.commit()
    my_j = json.dumps(visible)
    return my_j


@delete('/API/<name>')
def dele(name):
    query = "DELETE FROM PERSON WHERE NAME LIKE '{}' ".format(name)
    del_item = c.execute(query).fetchall()
    connect.commit()
    return del_item


@put('/API/<name>/<lname>/<age>/<nationcode>/<condition>')
def up(name, lname, age, nationcode, condition):
    query = "UPDATE PERSON SET NAME = '{0}', LNAME = '{1}', AGE = {2}, NATIONCODE = {3} WHERE NAME='{4}' ".format(name, lname, age, nationcode, condition)
    up_item = c.execute(query).fetchall()
    connect.commit()
    return up_item


if __name__ == '__main__':
    run(reloader=True, debug=True)