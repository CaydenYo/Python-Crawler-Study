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
load_dict = []
f = open('classify.json', 'r', encoding="utf-8")
print(f.encoding)
json_all = json.load(f, encoding='utf-8')

# print(datetime(2016,6,23))

jieba.load_userdict("dict.txt")

statistics = {}
for i in json_all:
    statistics[i] = 0;
print(statistics)

analyse.set_stop_words("stop_words.txt")

def text_filter(text):
    text = text.replace('\n', '')
    text = ''.join(map(lambda x: x if x not in '0123456789' else '', text))
    return text

def run_one_year_each_month(year, month, func):
    posts = POST_INFO_SET.find({
        'date': {
            "$gt": str(datetime(year, month, 1)),
            "$lt": str(
                datetime(
                    (year if month != 12 else year + 1),
                    (month + 1 if month != 12 else 1), 1)
            )}
        })
    return func(posts)


def get_content(posts):
    ids = []
    for post in posts:
        ids.append(post['comments'][0])
    return ids

def func(posts):
    for post in posts:
        first = COMMIT_INFO_SET.find({'comment_id': {"$in": [post['comments'][0]]}})
        str_all = first[0]['content']
        ans = ''.join(map(lambda x: x if x not in '0123456789' else '', str_all))
        keywords = analyse.tfidf(sentence=ans, topK=5)
        for keyword in keywords:
            print(keyword)
        print('----------')
        print(str_all)
        print('==========')


def is_classified(keywords):
    for keyword in keywords:
        for i in json_all:
            dict = json_all[i]
            if keyword[0] in dict:
                print(keyword[0] + ' ' + str(keyword[1]) + ' ' + i)
                statistics[i] += 1
                break

def year(year):
    ids = []
    str_all = ""
    for i in range(1,13):
        ids.extend(run_one_year_each_month(year, i, get_content))
    comments = COMMIT_INFO_SET.find({'comment_id': {"$in": ids}})
    for i in comments:
        str_all += i['content']
    text = text_filter(str_all)
    return text
    # print(text)
    # keywords = analyse.tfidf(sentence=text, topK=100)
    # for keyword in keywords:
    #     print(keyword)



# run_one_year_each_month(2017, 1, func)
str_all = ""
for i in range(0, 4):
    str_all += year(2015 + i)
    str_all += '\n'
print(str_all)

keywords = analyse.tfidf(sentence=str_all, topK=100, withWeight=True)
is_classified(keywords)
print(statistics)
# for keyword in keywords:
#     print(keyword)