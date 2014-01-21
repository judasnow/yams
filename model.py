#-*-coding:utf-8-*-
import web
from datetime import datetime

db = web.database(host='172.17.0.46', 
		dbn='mysql', 
		user='test', 
		pw='test', 
		db='yapm', 
		charset='utf8')
