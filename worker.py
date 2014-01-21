# -*- coding: utf-8 -*-
import web
import time
from model import db
from web.contrib.template import render_jinja

render = render_jinja(
	 'templates/main', 
	 encoding = 'utf-8',
	)

class trouble_list:
	def GET(self):
	 	 worker_no = 0
	 	 troub_list = db.select("trouble")
	 	 return render.trouble_list(title=u"维护人员页面", troub_list=troub_list, worker_no=worker_no)

	def POST(self):
		return "post"
