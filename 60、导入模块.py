# 项目时间：2022/3/10 14:35
import time

import schedule


def job():
    print('哈哈')


schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
