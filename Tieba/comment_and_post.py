from value import *
from task import Task


class TaskPMP(Task):
    from pymongo import MongoClient
    MONGO_CONNECT = MongoClient('127.0.0.1', 27017, maxPoolSize=None, connect=False)
    DB = MONGO_CONNECT.tieba
    POST_INFO_SET = DB.post_info
    UNFINISHED_POST_ID = DB.unfinished_post_id
    FINISHED_POST_ID = DB.finished_post_id
    COMMENT_INFO_SET = DB.comment_info
    USER_INFO_SET = DB.user_info
    MISSION_PER_MINUTES_SET = DB.mission_per_minutes


    def post_existed_in_database(self, post_info):
        if self.POST_INFO_SET.find({'post_id': post_info['post_id']}).count() != 0:
            return True
        else:
            return False

    def comment_existed_in_database(self, comment_info):
        if self.COMMENT_INFO_SET.find({'comment_id': comment_info['comment_id']}).count() != 0:
            return True
        else:
            return False

    def __init__(self):
        self.set('TaskPMP', LOG_MESSAGE['TaskPMP'])


    def save_new_post(self, post_info):
        self.POST_INFO_SET.insert(post_info)

    def save_new_comment(self, comment_info):
        self.COMMENT_INFO_SET.insert(comment_info)

    def update_post_info(self, post_info):
        self.POST_INFO_SET.update(
            {'comment_id': post_info['post_id']},
            {'$set':
                {
                    'comment_num': post_info['comment_num'],
                    'comments': post_info['comments'],
                }
            }
        )

    def update_comment_info(self, comment_info):
        self.COMMENT_INFO_SET.update(
            {'comment_id': comment_info['comment_id']},
            {'$set':
                {
                    'reply_num': comment_info['reply_num'],
                    'replies': comment_info['replies'],
                }
            }
        )

    def deal_p_info(self, method, data):
        if method == 'post':
            if self.post_existed_in_database(data):
                self.update_post_info(data)
            else:
                self.save_new_post(data)
        if method == 'comment':
            if self.comment_existed_in_database(data):
                self.update_comment_info(data)
            else:
                self.save_new_comment(data)