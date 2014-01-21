# -*- coding: utf-8 -*-
import web

import auth
import user
import worker
import admin

from model import db
from web.contrib.template import render_jinja

render = render_jinja(
	 'templates/main', 
	 encoding = 'utf-8',
	)


urls = (
	 #static index page
	 #auth
	 "/",
	 "auth.index",
	 "/dologin",
	 "auth.dologin",
	 "/dologout",
	 "auth.dologout",

	 #user 
	 #fees
	 "/fees", 
	 "user.fees",
	 #trouble
	 "/trouble_post",
	 "user.trouble_post",
	 #message
	 "/message_post",
	 "user.message_post",
	 "/message_list",
	 "user.message_list",
	 
	 #worker
	 "/worker",
	 "worker.trouble_list",
	 
	 #admin
	 "/fees_admin",
	 "admin.fees_admin"
)

app = web.application(urls, globals(), autoreload=True)
store = web.session.DiskStore('sessions')
session = web.session.Session(app, store, initializer={'user_info': None})
def session_hook():
    web.ctx.session = session
app.add_processor(web.loadhook(session_hook))

if __name__ == "__main__":
	 app.run()



