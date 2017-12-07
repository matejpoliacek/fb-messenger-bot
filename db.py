import os
from urlparse
import psycopg2

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

def db_connect():
	try:
		conn = psycopg2.connect(
			database=url.path[1:],
			user=url.username,
			password=url.password,
			host=url.hostname,
			port=url.port
		)
	except:
		print "Cannot connect to DB"

	cur = conn.cursor()

def db_close():
	cur.close()
	conn.close()

def check_fbID(in_id):
	db_connect()
	cur.execute('SELECT EXISTS (SELECT 1 FROM userID WHERE fb_id = %s LIMIT 1)', in_id)
	if cur.rowcount == 0:
		db_close()
		return false
	else:
		db_close()
		return true

def write_fbID(in_id):
	db_connect()	
	cur.execute('INSERT INTO userID (fb_id) VALUES (%s)', in_id)
	conn.commit()
	db_close()

def get_all_users():
	db.connect()
	cur.execute('SELECT * FROM userID;')
	all_ids = cur.fetchall()
	db.close()
	return all_ids
