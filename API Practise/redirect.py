from bottle import run, route, redirect, error


@route('/wrong/url')
def wrong():
    redirect('https://translate.google.com/#view=home&op=translate&sl=en&tl=fa&text=ac')


@error(404)
def error404(error):
    return 'Nothing here, sorry'


if __name__ == '__main__':
    run(reloader=True, debug=True)