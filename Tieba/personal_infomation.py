# -*- coding:utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup
from value import *
from task import Task


# @author haooon
# Task get tie zi id
class TaskGTI(Task):

    def id_existed_in_database(self, username):
        if SAVED_TIEZI_ID_SET.find({'id': username}).count() != 0:
            return True
        else:
            return False

    def run(self, name):
        try:
            done = False
            page = 1
            while page <= 5:
                url = VALUE['main_url'].format(name, str((page - 1) * 50))
                resp = requests.get(url, verify=False)
                html = resp.text
                soup = BeautifulSoup(html, 'lxml')
                a = soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})
                for i in a:
                    i = json.loads(i['data-field'])
                    if self.id_existed_in_database((i['id'])):
                        self.write_log('warning', 'find tiezi ' + str(i['id']) + ' already existed in database')
                        done = True
                        break
                    SAVED_TIEZI_ID_SET.insert(
                        {
                            "id": i['id'],
                            "reply_num": i['reply_num'],
                        }
                    )
                    self.write_log('complete', 'saved tiezi ' + str(i['id']) + ' to database')
                if done:
                    break
                page += 1
        except Exception as e:
            print(e)
            self.write_log('error', 'get tiezi id error')

    def __init__(self):
        self.set('TaskGTI', LOG_MESSAGE['TaskGTI'])


g = TaskGTI()
g.run('合肥工业大学')
