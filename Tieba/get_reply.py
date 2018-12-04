from snownlp import SnowNLP
from pymongo import MongoClient
from datetime import datetime


MONGO_CONNECT = MongoClient('127.0.0.1', 27017, maxPoolSize=None)
DB = MONGO_CONNECT.tieba
UNFINISHED_POST_ID = DB.unfinished_post_id
POST_INFO_SET = DB.post_info
COMMIT_INFO_SET = DB.comment_info
FINISHED_POST_ID = DB.finished_post_id

key_dict = {
    "挂科": [],
    "公选课": [],
    "校医院": [],
    "超市": [],
    "外卖": [],
    "驾校": [],
    "实习": [],
    "考研": [],
    "图书馆": []
}

def get_replies_by_post_id(post_id):
    str_all = []
    post = POST_INFO_SET.find_one({'post_id': post_id})
    comments = []
    for comment in post['comments']:
        comments.append(
            COMMIT_INFO_SET.find_one({'comment_id': comment})
        )
    for comment in comments:
        str_all.append(comment['content'])
        for reply in comment['replies']:
            str_all.append(reply['content'])
    return str_all

def get_post_by_keyword(year):
    post_all = []
    posts = POST_INFO_SET.find({
        'date': {
            "$gt": str(datetime(year, 1, 1)),
            "$lt": str(datetime(year + 1, 1, 1))
        }
    })
    for i in posts:
        comment = COMMIT_INFO_SET.find_one({'comment_id': i['comments'][0]})
        print(comment['content'])
        print(comment['date'], comment['user_id'])
        for i in key_dict.keys():
            if i in comment['content']:
                key_dict[i].append(comment['tiezi_id']);
                # post_all.append(comment['tiezi_id'])
        # print(key_dict)
    return post_all

replies = get_replies_by_post_id('5286275095')
for i in replies:
    s = SnowNLP(i)
    print(i, s.sentiments)
# key_dict = {
#     "挂科": 0,
#     "公选课": 0,
#     "校医院": 0,
#     "超市": 0,
#     "外卖": 0,
#     "驾校": 0,
#     "实习": 0,
#     "考研": 0,
#     "图书馆": 0
# }



# print(get_post_by_keyword(2017))
# for i in key_dict:
#     print(key_dict[i])
# print(get_post_by_keyword('公选课', 2017))
# print(get_post_by_keyword('校医院', 2017))
# print(get_post_by_keyword('超市', 2017))
# print(get_post_by_keyword('图书馆', 2017))
# print(get_post_by_keyword('考研', 2017))

