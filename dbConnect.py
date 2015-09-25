#!/usr/bin/python
# -*- coding: utf-8 -*-
import _mysql
import sys
import dbConfig

def execute(query):
	try:
		con = _mysql.connect(dbConfig.server, dbConfig.user, dbConfig.password, dbConfig.database)
		con.query(query)
		
    
	except _mysql.Error, e:
  
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)

	finally:
    
		if con:
			con.close()
