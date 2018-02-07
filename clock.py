from apscheduler.schedulers.blocking import BlockingScheduler
from msgs import weather_msg
import logging
import sys

log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG

fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=6)
def scheduled_job():
	print('This is a morning job')
	sys.stdout.flush()
	weather_msg()

# dummy job to keep awake 
@sched.scheduled_job('interval', minutes=60)
def scheduled_job():
	print('This is a regular job, keeping the app awake')
	sys.stdout.flush()
	# do nothing


sched.start()
