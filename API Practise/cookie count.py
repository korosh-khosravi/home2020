from bottle import run, route, response, error, request, template,view,SimpleTemplate

@route('/counter')
def counter():
    count = int(request.cookies.get('counter','0'))
    count +=1
    response.set_cookie('counter', str (count))
    return 'U visit this site %d time'  %count

@error(404)
def error404(error):
    return ('nothing here')

if __name__ == '__main__':
    run(debug=True, reloader=True)