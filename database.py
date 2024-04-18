import sqlite3 
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def connect_db():
	#create and connect to the database
	my_conn = sqlite3.connect(dir_path+'/cbt_app.db', check_same_thread=False) 
	return my_conn