# -*- coding: utf-8 -*-

__author__ = 'luyu'

"""
基于中文词频的域名 Whois 查询工具
Copyright 2014 Luyu Zhang <luyu.zhang@autotiming.com>
"""

import sqlite3
import pythonwhois
import time

conn = sqlite3.connect('data.sqlite')


def is_available(domain_whois):
    '''判断域名 Whois 的注册状态'''
    available = ''
    if domain_whois:
        # 已被注册确认有效期
        if domain_whois.get('raw'):
            raw = domain_whois.get('raw').pop()
            if 'No match for' in raw or 'no matching record.' in raw:
                available = domain_whois
                print 'The Domain is AVAILABLE!'
        if domain_whois.get('status'):
            print(domain_whois.get('status'));
        if domain_whois.get('updated_date'):
            pass
    if available:
        return available
    else:
        return ''


def get_expiry_date(domain_whois):
    if domain_whois:
        if domain_whois.get('expiration_date'):
            expiration_date = domain_whois.get('expiration_date').pop().strftime('%Y-%m-%d')
            return expiration_date
        else:
            return None


def query_pinyin_domains(limit=10000):
    '''获取词频前 10000 的拼音词'''
    c = conn.cursor()

    c.execute(
        'SELECT rowid, pinyin, frequency, last_updated FROM pinyin_domains WHERE expiry_date_com IS NULL ORDER BY frequency DESC LIMIT 10000')

    for row in c.fetchall():

        available_com = ''
        available_cn = ''

        # 打印 ID
        print row[0]

        if not row[1]:
            break

        # 拼合 COM 域名和 CN 域名
        pinyin = row[1]
        domain_com = pinyin + '.com'
        domain_cn = pinyin + '.cn'

        # 查询 Whois
        print domain_com
        try:
            w_com = pythonwhois.get_whois(domain_com, True)
        except:
            w_com = None

        if is_available(w_com):
            available_com = domain_com
        else:
            expiry_date_com = get_expiry_date(w_com)

        # 查询 Whois
        print domain_cn
        try:
            w_cn = pythonwhois.get_whois(domain_cn, True)
        except:
            w_cn = None

        if is_available(w_cn):
            available_cn = domain_cn
        else:
            expiry_date_cn = get_expiry_date(w_cn)

        # 更新数据库记录, 状态、有效期
        sql = 'UPDATE "main"."pinyin_domains" SET "available_com"="{1}", "expiry_date_com"="{2}", "available_cn"="{3}", "expiry_date_cn"="{4}", "last_updated"="{5}" WHERE rowid={0}'.format(
            row[0], available_com, expiry_date_com, available_cn, expiry_date_cn, time.time())
        c.execute(sql)
        conn.commit()


def query_number_domains(limit=10000):
    '''获取 10000 前的数字'''
    pass


if __name__ == '__main__':
    query_pinyin_domains()

    # TODO: 确认可被注册域名的状态列表...

    # w_cn = pythonwhois.get_whois('adfafds2424.com', True)
    # print 'No match for' in w_cn.get('raw').pop()
    conn.close()