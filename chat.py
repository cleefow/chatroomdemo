#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bottle
import os
from bottle import jinja2_template as template
import time
import chatDb

app = application = bottle.Bottle()
chatMsgs = chatDb.chatDb()

static_path = os.path.join(os.path.dirname(__file__), 'static/')
template_path = os.path.join(os.path.dirname(__file__), 'templates/')
languages = 'en cn'.split()

bottle.TEMPLATE_PATH.append(template_path)

@app.get('/')
def index():
    bottle.redirect('/chat')

@app.get('/chat')
def chat():
    global chatMsgs
    return template('chat.html', all_msg = chatMsgs.getMsg())

@app.route('/hello')
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name='stranger'):
    return template('home.html', name = name)

@app.post('/submit')
def submit_msg():
    global all_msg
    username = bottle.request.forms.get('username')
    content = bottle.request.forms.get('content')
    curtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    msg_item = {
            'name':username.decode('utf8'), 
            'content': content.decode('utf8'), 
            'time': curtime }
    # print msg_item
    chatMsgs.insertMsg(msg_item)
    # bottle.response.set_cookie('username', username)
    bottle.redirect('/chat')


@app.get('/<filename:path>')
def static(filename):
    return bottle.static_file(filename, root=static_path)

# Start server
if __name__ == '__main__':
    import sys
    bottle.run(app, host ='0.0.0.0', port = 9080, debug='debug' in sys.argv)
