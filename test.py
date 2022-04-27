import pymysql
from pprint import pprint

sbsjdb = pymysql.connect(
    user='admin',
    passwd='*******',
    host='sbsjdb.c73e6da4mxzg.ap-northeast-2.rds.amazonaws.com',
    db='sbsjdb',
    charset='utf8'
)

corp_code = '034730'
cur = sbsjdb.cursor()

code1 = (corp_code, '2020년 1분기')
code2 = (corp_code, '2020년 2분기')
code3 = (corp_code, '2020년 3분기')
code4 = (corp_code, '2020년 4분기')

query = 'SELECT * FROM searchtable_corporation WHERE corp_code=%s AND quarter=%s;'
cur.execute(query, code1)
sbsjdb.commit()

datas = cur.fetchall()
for data1 in datas:
    print(data1)

query = 'SELECT * FROM searchtable_corporation WHERE corp_code=%s AND quarter=%s;'
cur.execute(query, code2)
sbsjdb.commit()

datas = cur.fetchall()
for data2 in datas:
    print(data2)

query = 'SELECT * FROM searchtable_corporation WHERE corp_code=%s AND quarter=%s;'
cur.execute(query, code3)
sbsjdb.commit()

datas = cur.fetchall()
for data3 in datas:
    print(data3)

query = 'SELECT * FROM searchtable_corporation WHERE corp_code=%s AND quarter=%s;'
cur.execute(query, code4)
sbsjdb.commit()

datas = cur.fetchall()
for data4 in datas:
    print(data4)



# query = 'SELECT * FROM searchtable_corporation WHERE corp_code=%s;'
# cur.execute(query, corp_code)
# sbsjdb.commit()
#
# datas = cur.fetchall()
# print(datas)
# # for data in datas:
# #     print(data)
#
# # for i in datas:
# #     print(datas.index(i), i)
#
# print(datas[0][2])

from django.db.models import Q
from detail.models import *

def corporation_detail(request, corp_code):
    # name = Corporation.objects.filter(corp_code=corp_code)
    name = Corporation.objects.filter(Q(corp_code=corp_code) & Q(quarter="2020년 1분기"))


    print(name)


