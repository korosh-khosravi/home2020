from bottle import run, route, response, error, request, template
import os


@route('/upload', method='POST')
def do_upload():
    category = request.forms.get('category')
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'
    save_path = './API Practise'
    upload.save(save_path)
    return 'OK'


@error(404)
def error404(error):
    return('nothing here')


if __name__ == '__main__':
    run(reloader=True,debug=True)
