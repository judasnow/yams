# -*- coding: utf-8 -*-
import web
from model import db
from hashlib import md5
from web.contrib.template import render_jinja

render = render_jinja(
	 'templates/main',
	 encoding = 'utf-8',
	)

class index:
	 def GET(self):
		 #is user login ?
	 	 user_info = web.ctx.session.user_info
		 if user_info is not None:
	 	 #there is one user/admin/worker login 
		 	 role = user_info["role"]
			 user_id = user_info["id"]

			 if role == "user":
				 web.seeother("/fees")
			 if role == "admin":
				 web.seeotrher("/admin")
			 if role == "worker":
				 web.seeother("/worder")
	 
	 	 return render.index(title="yet anthor")

	 def POST(self):
		 return "WTF ! you get this pager by post?"

class dologin:
	def GET(self):
    	 	raise web.seeother('/')

	def POST(self):
	 	input = web.input(id=None, passwd=None, role=None)
		if input.id is not None and input.passwd is not None and input.role is not None:
	 	 	role = input.role
	    		id = input.id
	    		passwd = input.passwd
		else:
	 	 	#invaild input
		    	return render.index(auth_fail_code=3)

	 	try:
			 id_from_db = db.select(role, {"id":id}, where="id=$id")[0]
		except Exception, e:
			 #there isn`t username ,code 2
		    	 return render.index(auth_fail_code=1)
		
		if id_from_db is not None:
			hash = md5()
	    		hash.update(passwd)
	    		if id_from_db["passwd"] == hash.hexdigest():
				 #login ok
				 #insert userinfo into session
				 user_info = {"id":id, "role":role}
				 web.ctx.session.user_info = user_info
				 #is common user or admin or worker?
				 if role == "user":
	 	 	 	 	 web.seeother("/fees")
				 
				 if role == "admin":
					 web.seeother("/fees_admin")
				 
				 if role == "worker":
					 web.seeother("/worker")

	    		else:	 
		     		 #username or passwd error ,code 1
		    		 return render.index(auth_fail_code=1)
	 	else:
			 #there isn`t username ,code 2
		    	 return render.index(auth_fail_code=2)
