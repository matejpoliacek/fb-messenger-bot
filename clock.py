from apscheduler.schedulers.blocking import BlockingScheduler
from msgs import weather_msg
import logging

log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG

fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=14)
def scheduled_job():
	print('This is a morning job')
	weather_msg()

# testing job
#@sched.scheduled_job('interval', minutes=5)
#def timed_job():
#	weather_msg()

sched.start()
