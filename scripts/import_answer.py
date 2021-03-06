# -*- coding: utf-8 -*-
__author__ = 'shn7798'

from pymongo import MongoClient

from flask import Flask

from FlaskZhihu.settings import IPythonSettings
from FlaskZhihu.models import *
from FlaskZhihu.extensions import db
import datetime
def enc(s):
    if isinstance(s, unicode):
        return s.encode('UTF-8')
    else:
        return s

app = Flask(__name__)
app.config.from_object(IPythonSettings())
db.init_app(app)

ctx = app.app_context()

ctx.push()
mysql = db.session()

mg = MongoClient('192.168.5.202').zhihu

print Answer.query.delete()
mysql.commit()
#exit(1)

cur = mg.answers.find() #.limit(100000)

i = 0
for item in cur:
    try:
        d = item['data']
        o = Answer()
        o.id = d['id']
        o.content = enc(d['content'])
        o.excerpt = enc(d.get('excerpt', ''))
        create_time = d.get('created_time', None)
        if create_time:
            o.create_time = datetime.datetime.fromtimestamp(create_time)
        update_time = d.get('updated_time', None)
        if update_time:
            o.update_time = datetime.datetime.fromtimestamp(update_time)

        o.user_hashid = enc(d['author']['id'])
        u = User.get_user_by_hashid(o.user_hashid)
        if u:
            o.user = u

        o.question_id = int(d['question']['id'])

        mysql.add(o)
    except:
        pass

    i += 1
    if i % 100 == 0:
        mysql.commit()

mysql.commit()