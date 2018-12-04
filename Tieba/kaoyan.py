dict = [
    "食堂"
]


# -*- coding:utf-8 -*-
from pymongo import MongoClient
import time
import json
import jieba
from jieba import analyse

from snownlp import SnowNLP
MONGO_CONNECT = MongoClient('127.0.0.1', 27017, maxPoolSize=None)
DB = MONGO_CONNECT.tieba
UNFINISHED_POST_ID = DB.unfinished_post_id
POST_INFO_SET = DB.post_info
COMMIT_INFO_SET = DB.comment_info
FINISHED_POST_ID = DB.finished_post_id

from datetime import datetime
from datetime import timedelta
load_dict = []
jieba.load_userdict("dict.txt")
analyse.set_stop_words("stop_words.txt")

f = open('classify.json', 'r', encoding="utf-8")
json_all = json.load(f, encoding='utf-8')


statistics = {}
for i in json_all:
    statistics[i] = 0;
print(statistics)






def text_filter(text):
    text = text.replace('\n', '')
    text = ''.join(map(lambda x: x if x not in '0123456789' else '', text))
    return text

def is_classified(keywords):
    all_keyword = ""
    for keyword in keywords:
        for i in json_all:
            dict = json_all[i]
            if keyword in dict:
                all_keyword += keyword + ' '
                statistics[i] += 1
                break
    print(all_keyword)

final = []
def func(posts):
    all = ""
    for post in posts:
        first = COMMIT_INFO_SET.find({'comment_id': {"$in": [post['comments'][0]]}})
        str_all = first[0]['content']
        ans = ''.join(map(lambda x: x if x not in '0123456789' else '', str_all))
        # keywords = analyse.tfidf(sentence=ans, topK=10)
        num = 0
        for keyword in dict:
            if keyword in ans:
                num += 1
        if num != 0:
            print({
                'id': first[0]['tiezi_id'],
                'num': num,
                'content': first[0]['content']
            })
            final.append({
                'id': first[0]['tiezi_id'],
                'num': num
            })
            comment_num = 0;
            comment_emotion = 0;
            all_comments = COMMIT_INFO_SET.find({'comment_id': {"$in": post['comments']}})
            for com in all_comments:
                reply_and_comments = []
                reply_and_comments.append(com['content'])
                for c in reply_and_comments:
                    ans = ''.join(map(lambda x: x if x not in '0123456789' else '', c))
                    if ans == '':
                        continue
                    s = SnowNLP(ans)
                    COMMIT_INFO_SET.update({"comment_id": com['comment_id']}, {"$set": {"emotion": s.sentiments}})
                    comment_emotion += s.sentiments
                    comment_num += 1
                reply_and_comments = []
                for reply in com['replies']:
                    reply_and_comments.append(reply['content'])
                for r in reply_and_comments:
                    ans = ''.join(map(lambda x: x if x not in '0123456789' else '', r))
                    if ans == '':
                        continue
                    s = SnowNLP(ans)
                    comment_emotion += s.sentiments
                    comment_num += 1
            POST_INFO_SET.update({'post_id': post['post_id']}, {"$set": {
                'emotion': comment_emotion/comment_num,
                'classify': '小吃摊',
                'relevancy': num
            }})
            POST_INFO_SET.update({'post_id': post['post_id']}, {"$set": {'classify': '小吃摊'}})

def run():
    for i in range(300):
        now = (datetime.now() - timedelta(days=i)).date()
        last_week = (datetime.now() - timedelta(days=i+1)).date()
        posts = POST_INFO_SET.find({
            'date': {
                "$gt": str(last_week),
                "$lt": str(now)
            }
        })
        func(posts)


run()

for i in final:
    print(i)
#
# for i in run():
#     print(i)


def get_content(posts):
    ids = []
    for post in posts:
        ids.append(post['comments'][0])
    return ids



def get_last_week():
    ids = []
    str_all = ""
    for i in range(1,13):
        ids.extend(run_one_year_each_month(year, i, get_content))
    comments = COMMIT_INFO_SET.find({'comment_id': {"$in": ids}})
    return text
    # print(text)
    # keywords = analyse.tfidf(sentence=text, topK=100)
    # for keyword in keywords:
    #     print(keyword)



# run_one_year_each_month(2017, 1, func)
# str_all = ""
# for i in range(0, 4):
#     str_all += year(2015 + i)
#     str_all += '\n'
# print(str_all)
#
# keywords = analyse.tfidf(sentence=str_all, topK=100, withWeight=True)
# is_classified(keywords)
# print(statistics)

