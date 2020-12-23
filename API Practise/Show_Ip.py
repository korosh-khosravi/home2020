from bottle import  run,route,response,error,request,template

@route('/myip')
def show_ip():
    ip = request ['REMOTE_ADDR']
    return template('ur ip is {{ip}}', ip =ip)



@error(404)
def error404(error):
    return ('nothing here')

if __name__ == '__main__':
    run(debug=True, reloader=True)