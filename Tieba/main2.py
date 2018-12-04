import requests
import json
from bs4 import BeautifulSoup
from value import *
from task import Task


# @author haooon
# main process
# TaskGTI 1/min
#
class TaskMP(Task):

    pass

import platform
import os

import time
from apscheduler.schedulers.blocking import BlockingScheduler

def per1s():
    print('1s')

def per5s():
    print('5s')
    # sched.shutdown()

def per1m():
    manager = Manager()
    q = manager.Queue()
    q.put(1)

#
#

from multiprocessing import Process, Queue, Manager
import os

# 子进程要执行的代码
def run_proc(name):
    sched = BlockingScheduler()
    sched.add_job(per1m, 'interval', seconds=5)
    sched.start()

if __name__=='__main__':
    print('aaaParent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('aaaProcess will start.')
    p.start()
    p.join()
    print('aaaProcess end.')