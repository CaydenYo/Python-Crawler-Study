from comment_and_post import TaskPMP
from user_info import TaskPUI
from bs4 import BeautifulSoup
import requests
from task import Task
import json
from value import *

class TaskFP(Task):
    def trans_comment(self, comment_info):

        taskpui = TaskPUI()
        i = 1
        reply_list = []
        while True:
            url = VALUE['reply'].format(comment_info['tiezi_id'], comment_info['comment_id'], str(i))
            # print(url)
            resp = requests.get(url)
            resp.encoding = 'utf-8'
            html = resp.text
            soup = BeautifulSoup(html, 'lxml')
            # is_over = soup.find_all('p', attrs={'class': 'j_pager l_pager pager_theme_2'})

            replys = soup.find_all('li', attrs={'class': 'lzl_single_post'})
            if replys.__len__() == 0:
                break
            for reply in replys:
                data_json = json.loads(reply['data-field'])

                user_info = {
                    'user_id': '',
                    'user_name': data_json['user_name'],
                    'name_u': '',
                    'gender': '',
                    'portrait': '',
                    'is_like': '',
                    'level': '',
                    'level_name': '',
                    'cur_score': '',
                    'bawu': '',
                    'age': 0,
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
                taskpui.deal_user_info(user_info, 'add replies', comment_info)

                time = reply.find_all('span')[3].text
                content = reply.find_all('span', attrs={'class': 'lzl_content_main'})
                contenttext = reply.find_all('span')[0].text.strip()
                start = 2
                if contenttext[0:2] == '回复':
                    while contenttext[start] != ':':
                        start += 1
                        if start >= contenttext.__len__():
                            start = 2
                            break
                    contenttext = contenttext[start + 1:]
                reply_info = {
                    'spid': data_json['spid'],
                    'user_name': data_json['user_name'],
                    'content': contenttext,
                    'date': time
                }
                reply_list.append(reply_info)
            i += 1
        comment_info['replies'] = reply_list
        return comment_info


    def save_post(self, user_info, post_info):
        taskpui = TaskPUI()
        taskpmp = TaskPMP()
        taskpui.deal_user_info(user_info, 'add post', post_info)
        taskpmp.deal_p_info('post', post_info)
