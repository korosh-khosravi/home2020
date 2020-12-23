from bottle import run, get, request, post, delete, put
import psycopg2
import json

connect = psycopg2.connect(database="test1", user="korosh", password="0012652377", host="127.0.0.1", port="5432")
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
                 VALUES (%s,%s,%s,%s)''', (name, lname, age, nationcode))
    connect.commit()
    return 'ok'


@get('/API/<id>')
def get_code(id):
    query = "SELECT * FROM PERSON WHERE NATIONCODE=" + id
    c.execute(query)
    visible = c.fetchall()
    my_j = json.dumps(visible)
    return my_j


@delete('/API/<name>')
def dele(name):
    query = "DELETE FROM PERSON WHERE NAME LIKE '{}' ".format(name)
    del_item = c.execute(query)
    connect.commit()
    return del_item


@put('/API/<name>/<lname>/<age>/<nationcode>/<condition>')
def up(name, lname, age, nationcode, condition):
    query = "UPDATE PERSON SET NAME = '{0}', LNAME = '{1}', AGE = {2}, NATIONCODE = {3} WHERE NAME='{4}' ".format(name, lname, age, nationcode, condition)
    up_item = c.execute(query)
    connect.commit()
    return up_item


if __name__ == '__main__':
    run(reloader=True, debug=True)