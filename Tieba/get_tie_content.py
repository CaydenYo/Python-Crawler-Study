# -*- coding:utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup
from value import *
from user_info import TaskPUI
from task import Task
from floorProcess import *
import time

# @author haooon
# Task Get Tie zi Content
# 统计总页数
# 遍历页 爬数据
#   爬帖子人
#

class TaskGTC(Task):

    def run(self, tiezi_id):
        # try:
        url = VALUE['tiezi_url'].format(tiezi_id, '1')
        resp = requests.get(url)
        html = resp.text
        soup = BeautifulSoup(html, 'lxml')
        spans = soup.find_all('li', attrs={'class': 'l_reply_num'})[0].find_all('span')
        page_num = spans[1].text
        post_info = {
            'post_id': tiezi_id,
            'user_id': None,
            'date': None,
            'comment_num': None,
            'activity': 0,
            'comments': [],
            'data': {
                'keyword': []
            }
        }
        # 帖子页数
        page = 1
        # 楼层数
        num = 1
        # 楼层列表
        comment_list = []
        user_info = {}
        floorprocess = TaskFP()
        first_comment_user_info = None
        while page <= int(page_num):
            a = soup.find_all('div', attrs={'class': 'p_postlist'})[0].find_all('div', attrs={'class': 'j_l_post'})
            for i in a:
                data_json = json.loads(i['data-field'])
                user_info = {
                    'user_id': data_json['author']['user_id'],
                    'user_name': data_json['author']['user_name'],
                    'name_u': data_json['author']['name_u'],
                    'gender': data_json['author']['user_sex'],
                    'portrait': data_json['author']['portrait'],
                    'is_like': data_json['author']['is_like'],
                    'level': data_json['author']['level_id'],
                    'level_name': data_json['author']['level_name'],
                    'cur_score': data_json['author']['cur_score'],
                    'bawu': data_json['author']['bawu'],
                    'age':0,
                    'activity': 0,
                    'posts': [],
                    'comments': [],
                    'replies': [],
                    'data': {
                        'week': [],
                        '2week': [],
                        'month': []
                    }
                }
                comment_info = {
                    'tiezi_id': tiezi_id,
                    'comment_id': data_json['content']['post_id'],
                    'user_id': data_json['author']['user_id'],
                    'open_type': data_json['content']['open_type'],
                    'date': data_json['content']['date'],
                    'content': i.find_all('div', attrs={'class': 'd_post_content'})[0].text.strip(),
                    'comment_no': data_json['content']['post_no'],
                    'type': data_json['content']['type'],
                    'reply_num': data_json['content']['comment_num'],
                    'activity': 0,
                    'replies': [],
                    'data': {
                        'keyword': []
                    }
                }
                taskpui = TaskPUI()
                taskpmp = TaskPMP()

                comment_info = floorprocess.trans_comment(comment_info)

                taskpui.deal_user_info(user_info, 'add comment', comment_info)
                taskpmp.deal_p_info('comment', comment_info)

                comment_list.append(data_json['content']['post_id'])
                if num == 1:
                    post_info['user_id'] = data_json['author']['user_id']
                    post_info['date'] = data_json['content']['date']
                    first_comment_user_info = user_info
                # print(comment_info)
                print(num)
                num += 1

                # 处理每一层
                # break
                pass
            page += 1
            url = VALUE['tiezi_url'].format(tiezi_id, page)
            resp = requests.get(url)
            html = resp.text
            soup = BeautifulSoup(html, 'lxml')
        post_info['comment_num'] = num
        post_info['comments'] = comment_list
        floorprocess.save_post(first_comment_user_info, post_info)
        print('finished: ', tiezi_id)

    def __init__(self):
        self.set('TaskGTC', LOG_MESSAGE['TaskGTI'])


# start_time = time.time()
# g = TaskGTC()
# g.run('5197373039')
# end_time = time.time()
# print(end_time - start_time)
