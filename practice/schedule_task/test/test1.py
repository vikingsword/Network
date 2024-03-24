# !usr/bin/env python
# -*- coding:utf-8 _*-

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


# 输出时间
def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# BlockingScheduler
sched = BlockingScheduler()
sched.add_job(job, 'interval', seconds=5, id='my_job_id')
sched.start()
