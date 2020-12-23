import json
import datetime
import re
from bottle import run, get, put, post, delete, request, response, template
from Library import SQLconnection as SQL


@post('/login/<username>/<password>')
def login(username, password):
    # username = request.json.get('member_id')
    # password = request.json.get('password')     #how use regex with json!
    regex = r"^\d+$"
    if re.search(regex, username) and re.search(regex, password):
        if check_login(username, password):
            deathtime = datetime.datetime.now() + datetime.timedelta(days=1)
            response.set_cookie('account', username, secret="4321", path='/', expires=deathtime)
            return template('Successful Login {{name}}', name=username)
        else:
            return 'Faild.'
    else:
        return False, "Your Password or Username Incorrect"


def check_login(username, password):
    SQL.c.execute('''SELECT EXISTS
                    (SELECT * FROM library WHERE member_id = {} and pass_word = {})'''.format(username, password))
    query_result = SQL.c.fetchall()
    tuple_result = query_result[0][0]
    SQL.conn.commit()
    return tuple_result


