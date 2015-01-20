#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import MySQLdb.cursors

createTableCmd='''CREATE TEBLE if not exists message ( \
    id  int(6) NOT NULL AUTO_INCREASEMENT, \
    name char(50) NOT NULL, \
    time char(50) NOT NULL, \
    content char(255), \
    PRIMARY KEY(id) \
)'''
'''CREATE TABLE `messages` (\
        `id`  int(6) NOT NULL AUTO_INCREMENT, \
        `name` varchar(50) NOT NULL, \
        `time` varchar(50) NOT NULL, \
        `content` varchar(255), \
        PRIMARY KEY(`id`) \
        ) CHARSET=utf8;'''

insertCmd='''insert into messages(name, time, content) \
        values('%s', '%s', '%s')'''
testMsgItem = {'name':'testUserName',
        'content': 'testContent',
        'time': 'testTime'}

class chatDb():
    conn = None
    cur = None
    def __init__(self):
        self.conn=MySQLdb.Connect(
                host='localhost',
                user = 'test',
                passwd = 'test',
                port = 3306,
                cursorclass = MySQLdb.cursors.DictCursor)
        print self.conn
        self.cur = self.conn.cursor()

        self.cur.execute('create database if not exists testDb')
        self.conn.select_db('testDb')
        #self.cur.execute(tableChatMsg)

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def getMsg(self):
        self.cur.execute('select * from messages order by -1*id')
        # for data in self.cur.fetchall():
        #    print data
        return self.cur.fetchall()

    def insertMsg(self, item=testMsgItem):
        self.cur.execute(insertCmd % (
            item['name'], 
            item['time'], 
            item['content']))
        self.conn.commit()


if __name__ == '__main__':
    db=chatDb()
    print db.getMsg()

