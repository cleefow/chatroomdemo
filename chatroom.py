from bottle import route, run, template
from bottle import get, post, request

all_content=''

@route('/chatroom')
@route('/chatroom/<roomname>')
def index(roomname='default roomname'):
    return template('''<html><head></head><body>welcome to {{roomname}}<br/>
            {{!all_content}}
            <form action="/postdiag" method="post">
            username: <input name="username" type="text" /> <br/>
            content: <input name="content" type="text" /> <br/>
            <input value="Post" type="submit" />
            </form></body></html>''', 
            all_content = all_content,
            roomname=roomname)

@get('/postdiag')
def do_get():
    return

@post('/postdiag')
def do_post():
    global all_content
    username = request.forms.get('username')
    content = request.forms.get('content')

    if username == '':
        username = 'anonymous'
    this_content = '<p>' + username + ' : ' + content + '</p>'
    all_content = all_content + this_content
    return '<a href="chatroom">post ok, return</a>'

run(host='localhost', port=8080)

