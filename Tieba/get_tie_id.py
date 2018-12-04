# -*- coding:utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup
from value import *
from task import Task


# @author haooon
# Task get tie zi id
class TaskGTI(Task):
    from pymongo import MongoClient
    MONGO_CONNECT = MongoClient('127.0.0.1', 27017, maxPoolSize=None, connect=False)
    DB = MONGO_CONNECT.tieba
    POST_INFO_SET = DB.post_info
    UNFINISHED_POST_ID = DB.unfinished_post_id
    FINISHED_POST_ID = DB.finished_post_id
    COMMENT_INFO_SET = DB.comment_info
    USER_INFO_SET = DB.user_info
    MISSION_PER_MINUTES_SET = DB.mission_per_minutes
    def id_existed_in_database(self, tiezi_id):
        if self.UNFINISHED_POST_ID.find({'id': tiezi_id}).count() != 0:
            return True
        else:
            return False

    def run(self, name):
        try:
            done = False
            page = 1
            while page <= 5:
                url = VALUE['main_url'].format(name, str((page - 1) * 50))
                print(url)
                resp = requests.get(url, verify=False)
                html = resp.text
                soup = BeautifulSoup(html, 'lxml')
                a = soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})
                for i in a:
                    i = json.loads(i['data-field'])
                    if self.id_existed_in_database((i['id'])):
                        self.write_log('warning', 'find tiezi ' + str(i['id']) + ' already existed in database')
                        done = True
                        continue
                    self.UNFINISHED_POST_ID.insert(
                        {
                            "id": i['id'],
                        }
                    )
                    self.write_log('complete', 'saved tiezi ' + str(i['id']) + ' to database')
                # if done:
                #     break
                page += 1
        except Exception as e:
            print(e)
            self.write_log('error', 'get tiezi id error')

    def __init__(self):
        self.set('TaskGTI', LOG_MESSAGE['TaskGTI'])


g = TaskGTI()
g.run('达内')
