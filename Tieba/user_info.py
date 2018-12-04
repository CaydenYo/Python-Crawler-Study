from value import *
from task import Task


class TaskPUI(Task):
    from pymongo import MongoClient
    MONGO_CONNECT = MongoClient('127.0.0.1', 27017, maxPoolSize=None, connect=False)
    DB = MONGO_CONNECT.tieba
    POST_INFO_SET = DB.post_info
    UNFINISHED_POST_ID = DB.unfinished_post_id
    FINISHED_POST_ID = DB.finished_post_id
    COMMENT_INFO_SET = DB.comment_info
    USER_INFO_SET = DB.user_info
    MISSION_PER_MINUTES_SET = DB.mission_per_minutes
    def user_existed_in_database(self, user_info):
        name = user_info['user_name']
        if self.USER_INFO_SET.find({'user_name': name}).count() != 0:
            return True
        else:
            return False

    def __init__(self):
        self.set('TaskPUI', LOG_MESSAGE['TaskPUI'])

    def save_user_info(self, user_info):
        self.USER_INFO_SET.insert(user_info)


    def update_user_info(self, user_info):
        name = user_info['user_name']
        user = self.USER_INFO_SET.find_one({'user_name': name})
        if user['user_id'] == '':
            self.USER_INFO_SET.update(
                {'user_name': name},
                {'$set':
                     {
                        'user_id': user_info['user_id'],
                        'name_u': user_info['name_u'],
                        'gender': user_info['gender'],
                        'portrait': user_info['portrait'],
                        'is_like': user_info['is_like'],
                        'level': user_info['level'],
                        'level_name': user_info['level_name'],
                        'cur_score': user_info['cur_score'],
                        'bawu': user_info['bawu'],
                        'age': user_info['age'],
                        'activity': user_info['activity'],
                    }
                }
            )
        elif user_info['user_id'] != '':
            self.USER_INFO_SET.update(
                {'user_name': name},
                {'$set':
                     {
                         'level': user_info['level'],
                     }
                }
            )

    def add_post(self, user_info, post_info):
        self.update_user_info(user_info)
        post_list = self.USER_INFO_SET.find_one({'user_name': user_info['user_name']})['posts']
        for i in post_list:
            if i== post_info['post_id']:
                return
        post_list.append(post_info['post_id'])
        self.USER_INFO_SET.update(
            {'user_name': user_info['user_name']},
            {'$set':
                {
                    'posts': post_list
                }
            }
        )

    def add_comment(self, user_info, comment_info):
        self.update_user_info(user_info)
        comment_list = self.USER_INFO_SET.find_one({'user_name': user_info['user_name']})['comments']
        for i in comment_list:
            if i[0] == comment_info['tiezi_id'] and i[1] == comment_info['comment_id']:
                return
        comment_list.append([comment_info['tiezi_id'], comment_info['comment_id']])
        self.USER_INFO_SET.update(
            {'user_name': user_info['user_name']},
            {'$set':
                {
                    'comments': comment_list
                }
            }
        )

    def add_reply(self, user_info, comment_info):
        self.update_user_info(user_info)
        comment_list = self.USER_INFO_SET.find_one({'user_name': user_info['user_name']})['replies']
        for i in comment_list:
            if i[0] == comment_info['tiezi_id'] and i[1] == comment_info['comment_id']:
                return
        exist = False
        for i in comment_list:
            if i[0] == [comment_info['tiezi_id'] and i[1] == comment_info['comment_id']]:
                exist = True
                break
        if not exist:
            comment_list.append([comment_info['tiezi_id'], comment_info['comment_id']])
        self.USER_INFO_SET.update(
            {'user_name': user_info['user_name']},
            {'$set':
                {
                    'replies': comment_list
                }
            }
        )

    def deal_user_info(self, user_info, method, data):
        if method == 'add post':
            if self.user_existed_in_database(user_info):
                self.add_post(user_info, data)
            else:
                self.save_user_info(user_info)
                self.add_post(user_info, data)
        if method == 'add comment':
            if self.user_existed_in_database(user_info):
                self.add_comment(user_info, data)
            else:
                self.save_user_info(user_info)
                self.add_comment(user_info, data)
        if method == 'add replies':
            if self.user_existed_in_database(user_info):
                self.add_reply(user_info, data)
            else:
                self.save_user_info(user_info)
                self.add_reply(user_info, data)
