import time
from value import *
from multiprocessing import Pool, Manager
import os
from get_tie_content import TaskGTC


def one_process(lock):
    i = 0
    from pymongo import MongoClient
    MONGO_CONNECT = MongoClient('127.0.0.1', 27017, maxPoolSize=None)
    DB = MONGO_CONNECT.tieba
    UNFINISHED_POST_ID = DB.unfinished_post_id
    FINISHED_POST_ID = DB.finished_post_id
    while(i < 10):
        lock.acquire()
        if UNFINISHED_POST_ID.find_one() == None:
            lock.release()
            return
        print(UNFINISHED_POST_ID.find_one())
        #.count() != 0:
        id = UNFINISHED_POST_ID.find_one()
        UNFINISHED_POST_ID.remove(id)
        lock.release()

        tiezi_task = TaskGTC()
        tiezi_task.run(str(id['id']))
        print(str(i) + ' : ' + str(id['id']))

        lock.acquire()
        FINISHED_POST_ID.insert(id)
        lock.release()
        i += 1



if __name__ == '__main__':
    s = time.time()
    i = 0
    while i < 20:
        pool = Pool(15)
        manager = Manager()
        lock = manager.Lock()
        for j in range(15):
            pool.apply_async(func=one_process, args=(lock,))
        pool.close()
        pool.join()
        i += 1
    e = time.time()
    print(e - s)