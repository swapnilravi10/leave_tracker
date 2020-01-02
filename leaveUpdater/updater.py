from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from leaveUpdater import leavecrediter


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(leavecrediter.credit_leave, 'interval', minutes=5)
    scheduler.start()