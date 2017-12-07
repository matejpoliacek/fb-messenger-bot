import os
import urlparse
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

	return conn

def db_close(cur, conn):
	cur.close()
	conn.close()

def check_fbID(in_id):
	conn = db_connect()
	cur = conn.cursor()
	cur.execute('SELECT EXISTS (SELECT 1 FROM userID WHERE fb_id = %s LIMIT 1)', str(in_id))
	if cur.rowcount == 0:
		db_close(cur, conn)
		return false
	else:
		db_close(cur, conn)
		return true

def write_fbID(in_id):
	conn =	db_connect()	
	cur = conn.cursor()
	cur.execute('INSERT INTO userID (fb_id) VALUES (%s)', str(in_id))
	conn.commit()
	db_close(cur, conn)

def get_all_users():
	conn = db.connect()
	cur = conn.cursor()
	cur.execute('SELECT * FROM userID;')
	all_ids = cur.fetchall()
	db.close(cur, conn)
	return all_ids
