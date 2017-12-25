from apscheduler.schedulers.blocking import BlockingScheduler
from msgs import weather_msg

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=7)
def scheduled_job():
	print('This is a morning job')
	weather_msg()

@sched.scheduled_job('interval', minutes=5)
def timed_job():
	weather_msg()

sched.start()
