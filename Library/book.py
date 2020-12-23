import json
import re
from bottle import run, get, put, post, delete, request, Bottle
from Library import SQLconnection as SQL

app = Bottle()


@app.get('/book/<book_id>')
def get(book_id):
    regex = r"^\d+$"
    if re.search(regex, book_id):
        SQL.c.execute('''BEGIN; SELECT * FROM book WHERE book_id = {0};'''.format(book_id))
        visible = SQL.c.fetchall()
        myjson = json.dumps(visible)
        return myjson
    else:
        return "Your Input Incorrect.Try Again"


@app.put('/book/<book_id>')
def updating(book_id):
    regex = r"^\d+$"
    if re.search(regex, book_id):
        name = request.json.get('name')
        author = request.json.get('author')
        category = request.json.get('category')
        price = request.json.get('price')
        number = request.json.get('number')
        SQL.c.execute('''BEGIN; UPDATE book SET name='{0}', author='{1}', category='{2}',price='{3}',number='{4}'
        WHERE book_id ={5}'''.format(name, author, category, price, number, book_id))
        SQL.conn.commit()
        return 'Update Done.'
    else:
        return "Your Input Incorrect.Try Again"


@app.post('/book')
def post():
    name = request.json.get('name')
    author = request.json.get('author')
    category = request.json.get('category')
    price = request.json.get('price')
    number = request.json.get('number')
    SQL.c.execute('''BEGIN; INSERT INTO book(name, author, category, price, number, book_id)  
                    VALUES(%s, %s, %s, %s, %s, NEXTVAL('book_book_id_seq'))''', (name, author, category, price, number))
    SQL.conn.commit()
    return 'Insert Done.'


@app.delete('/book/<book_id>')
def delete(book_id):
    regex = r"^\d+$"
    if re.search(regex, book_id):
        query = "BEGIN; DELETE FROM book WHERE book_id = {}".format(book_id)
        SQL.c.execute(query)
        SQL.conn.commit()
        return 'Delete ', book_id
    else:
        return "Your Input Incorrect.Try Again"

application = app