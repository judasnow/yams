# -*- coding: utf-8 -*-
import web
import time
from model import db
from web.contrib.template import render_jinja

render = render_jinja(
	 'templates/main', 
	 encoding = 'utf-8',
	)

class fees:
	 def GET(self):
		 #get year & month
	 	 years = time.strftime("%Y")
		 month = time.strftime("%m")
		 #user hasn`t login 
	 	 if web.ctx.session.user_info is None:
			 raise web.seeother("/")

	 	 user_info = web.ctx.session.user_info
	 	 #：-（
		 fees_list = db.select(
				 "fees",
				 {"id":user_info["id"], "years":years, "month":month},
				 what="name, sum, status", 
				 where="user_id=$id and years=$years and month=$month"
				 )
		 return render.fees(title=u"缴费信息", id=id, years=years, month=month, fees_list=fees_list)
	
	 def POST(self):
	 	 raise web.seeother("/fees")

class trouble_post:
	 def GET(self):
	 	 #user hasn`t login 
	 	 if web.ctx.session.user_info is None:
			 raise web.seeother("/")
	
		 user_indo = web.ctx.session.user_info 
	 	 return render.trouble_post(title=u"故障报修", user_id=user_info["id"])
	
	 def POST(self):
	 	 #user hasn`t login 
	 	 if web.ctx.session.user_info is None:
			 raise web.seeother("/")

		 user_info = web.ctx.session.user_info
		 input = web.input(address=None, tel=None, des=None)
	 	 
		 if input.tel is not None or input.address is not None or input.des is not None:
	 	 	 tel = input.tel
			 des = input.des
			 address = input.address
		 else:
			 return render.trouble_post(title=u"故障报修", user_id=user_info["user_id"], message_code=-1)

	 	 try:
		 	 db.insert("trouble", address=address, reporter=user_id, des=des, tel=tel)
		 except Exception, e:
	 	 	 return render.trouble_post(title=u"故障报修", user_id=user_id, message_code=-2)

		 return render.trouble_post(title=u"故障报修", user_id=user_id, message_code=0)
	 	 
class message_post:
	def GET(self):
	 	 #user hasn`t login 
	 	 if web.ctx.session.user_info is None:
			 raise web.seeother("/")
	
		 user_info = web.ctx.session.user_info
	 	 return render.message_post(title=u"给物业留言", user_id=user_info["user_id"])
	def POST(self):
		 #user hasn`t login 
	 	 if web.ctx.session.user_info is None:
			 raise web.seeother("/")
	 	 user_info = web.ctx.session.user_info

		 input = web.input(title=None, content=None)
	 	 
		 if input.title is not None or input.content is not None:
	 	 	 title = input.title
			 content = input.content

		 else:
			 return render.message_post(title=u"给物业留言", user_id=user_info["id"], message_code=-1)

	 	 try:
		 	 db.insert("message", content=content, title=title, poster=user_info["id"])
		 except Exception, e:
	 	 	 return render.message_post(title=u"给物业留言", user_id=user_info["id"], message_code=-2)

		 return render.message_post(title=u"给物业留言", user_id=user_info["id"], message_code=0)

class message_list:
	 def GET(self):
	 	 message_list = db.select("message")
	 	 return render.message_list(title=u" 留言列表", message_list=message_list) 
	 
	 def POST(self):
		 raise web.seeother("/message_list")
