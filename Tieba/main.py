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

from multiprocessing import Process, Queue, Manager
import os
manager = Manager()
q = manager.Queue()

def per1m():
    print(q.qsize())

#
#




def per1m1():

    print('123123')
    q.put(1)

# 子进程要执行的代码
def run_proc1(name):
    sched = BlockingScheduler()
    sched.add_job(per1m1, 'interval', seconds=5)
    sched.start()
# 子进程要执行的代码
def run_proc(name):
    sched = BlockingScheduler()
    sched.add_job(per1m, 'interval', seconds=1)
    sched.start()

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    p1 = Process(target=run_proc1, args=('test',))
    print('Process will start.')
    p.start()
    p1.start()
    p.join()
    p1.join()
    print('Process end.')