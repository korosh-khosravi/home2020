from bottle import run, route, response, error, request, template,view,SimpleTemplate

@route('/hello')
@route('/hello/<name>')
def hello(name='World'):
    return template('hello_template', name=name)



if __name__ == '__main__':
    run(debug=True, reloader=True)