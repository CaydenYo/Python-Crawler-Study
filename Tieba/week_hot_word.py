# -*- coding:utf-8 -*-
from pymongo import MongoClient
import time
import json
import jieba
from jieba import analyse


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



now = datetime.now().date()
last_week = (datetime.now() - timedelta(days=7)).date()

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

def func(posts):
    all = ""
    for post in posts:
        first = COMMIT_INFO_SET.find({'comment_id': {"$in": [post['comments'][0]]}})
        str_all = first[0]['content']
        ans = ''.join(map(lambda x: x if x not in '0123456789' else '', str_all))
        keywords = analyse.tfidf(sentence=ans, topK=10)
        # is_classified(keywords)
        for keyword in keywords:
            all += keyword + ' '
        # print(keywords)
        # print(str_all)
        # print('------------------------------------------')
    keywords = analyse.tfidf(sentence=all, topK=100, withWeight=True)
    for keyword in keywords:
        print('{name:' + '\"' + keyword[0] + '\",' + 'value:' + str(int(keyword[1]*1000)) + '},')
    # print(keywords)

def run():
    posts = POST_INFO_SET.find({
        'date': {
            "$gt": str(last_week),
            "$lt": str(now)
        }
    })
    func(posts)


run()
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

