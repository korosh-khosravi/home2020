from bottle import run, route, static_file,error

@route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root='./API Practise', download=filename)

@error(404)
def error404(error):
    return 'Nothing here, sorry'

if __name__ == '__main__':
    run (reloader=True, debug=True)
