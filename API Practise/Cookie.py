from bottle import run,route,response,error,request

@route('/hello')
def hello_again():
    if request.get_cookie("visited"):
        return "Welcome back! Nice to see you again"
    else:
        response.set_cookie("visited", "yes")
        return "Hello there! Nice to meet you"

@error(404)
def error404(error):
    return ('nothing here')

if __name__ == '__main__':
    run(debug=True, reloader=True)