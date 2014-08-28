# -*- coding: utf-8 -*-

__author__ = 'luyu'

"""
初始化来自 Sogou 的词频数据库, 写入 SQLite

See: http://www.sogou.com/labs/dl/w.html

N				名词
V				动词
ADJ			形容词
ADV			副词
CLAS		量词
ECHO		拟声词
STRU		结构助词
AUX			助词
COOR		并列连词
CONJ		连词
SUFFIX	前缀
PREFIX	后缀
PREP		介词
PRON		代词
QUES		疑问词
NUM			数词
IDIOM		成语

-- ----------------------------
--  Table structure for pinyin_domains
-- ----------------------------
DROP TABLE IF EXISTS "pinyin_domains";
CREATE TABLE "pinyin_domains" (
	 "word" text NOT NULL,
	 "pinyin" TEXT NOT NULL,
	 "frequency" integer,
	 "available_com" TEXT,
	 "available_cn" TEXT,
	 "expiry_date_com" TEXT,
	 "expiry_date_cn" TEXT,
	 "last_updated" text
);

"""

import sqlite3
import time
from xpinyin import Pinyin

file_object = open('sougouDic.txt')
list_of_all_the_lines = file_object.readlines()

con = sqlite3.connect('data.sqlite')

p = Pinyin()

# TODO: 么->YAO
# TODO: 还->HUAN

for line in list_of_all_the_lines:
    list_of_line = line.split('\t')
    word = list_of_line[0]
    pinyin = p.get_pinyin(word.decode("utf-8"), '')
    frequency = list_of_line[1]

    c = con.cursor()

    try:
        sql = """INSERT INTO "main"."pinyin_domains" ( "word", "pinyin", "frequency", "last_updated") VALUES ('{0}', '{1}', {2}, '{3}')""".format(
            word, pinyin, frequency, time.time())
        c.execute(sql)
    except UnicodeEncodeError:
        pass

c.close()
con.commit()
con.close()

print 'All Right!'