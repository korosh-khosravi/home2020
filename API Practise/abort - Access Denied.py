from bottle import route, run, abort, error


@route('/restricted')
def restricted():
    abort(402,'sorry, access denied')


@error(404)
def error404(error):
    return 'Nothing here, sorry'


if __name__=='__main__':
    run(reloader=True, debug=True)

