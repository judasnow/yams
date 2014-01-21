# -*- coding: utf-8 -*-
import web
import time
from model import db
from web.contrib.template import render_jinja

render = render_jinja(
	 'templates/admin', 
	 encoding = 'utf-8'
	)

class fees_admin:
	 def GET(self):
	 	 return render.fees_admin()
	
	 def POST(self):
		 return "post"
	 	 
		 
