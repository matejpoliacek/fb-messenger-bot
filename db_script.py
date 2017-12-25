import os
import sys
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
	in_id = "\'" + in_id + "\'"
	cur.execute('SELECT COUNT (fb_id) FROM userdb WHERE fb_id = %s;', (in_id,))
	found = cur.fetchall()
	for x in found:
		extract = x[0]
	sys.stdout.write(extract)
	sys.stdout.flush()
	if extract == 0:
		db_close(cur, conn)
		return True
	else:
		db_close(cur, conn)
		return False

def check_post(in_id):
	conn = db_connect()
	cur = conn.cursor()
	cur.execute('SELECT post FROM userdb WHERE fb_id = %s;', (in_id,))
	post_result = cur.fetchall()
	for x in post_result:
		extract = x[0]
	sys.stdout.write(extract)
	sys.stdout.flush()
	if extract == 0:
		return False
	else:
		return True


def write_fbID(in_id):
	conn =	db_connect()	
	cur = conn.cursor()
	cur.execute('INSERT INTO userdb (fb_id, post) VALUES (%s, 1);', (in_id,))
	conn.commit()
	db_close(cur, conn)

def mute_fbID(in_id):
	conn = db_connect()
	cur = conn.cursor()
	cur.execute('UPDATE userdb SET post = 0 WHERE fb_id = %s;', (in_id,))
	conn.commit()
	db_close(cur, conn)

def unmute_fbID(in_id):
	conn = db_connect()
	cur = conn.cursor()
	cur.execute('UPDATE userdb SET post = 1 WHERE fb_id = %s;', (in_id,))
	conn.commit()
	db_close(cur, conn)

def get_all_users():
	conn = db.connect()
	cur = conn.cursor()
	cur.execute('SELECT fb_id FROM userdb WHERE post = 1;')
	all_ids = cur.fetchall()
	db.close(cur, conn)
	return all_ids
