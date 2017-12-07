from apscheduler.schedulers.blocking import BlockingScheduler
import msgs.py

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=7)
def scheduled_job():
	print('This is a morning job')
	weather_msg()

sched.start()
