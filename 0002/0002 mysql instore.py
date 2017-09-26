#-*-coding:utf-8 -*-
'''
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
'''
import pymysql
import uuid
def createcode(num):
    codelist=[]
    for i in xrange(num):
        code=str(uuid.uuid4()).replace('-','').upper()
        while code in codelist:
            code=str(uuid.uuid4()).replace('-','').upper()
        codelist.append(code)
    return codelist
def storecode(codelist):
    try:
        conn=pymysql.connect(host='127.0.0.1',user='root',passwd='228600',db='mysql')
        cur=conn.cursor()
    except BaseException as e:
        print (e)
    else:
        try:
            cur.execute('CREATE DATABASE act_code_in_py')
            cur.execute('USE act_code_in_py')
            cur.execute('''CREATE TABLE IF NOT EXISTS code_table(
                            id INT NOT NULL AUTO_INCREMENT,
                            code VARCHAR(32) NOT NULL,
                            PRIMARY KEY(id))
                        ''')
            for code in codelist:
                cur.execute('INSERT INTO code_table(code) VALUES(%s)',(code))
                cur.connection.commit()
        except BaseException as e:
            print (e)
    finally:
        cur.close()
        conn.close()

storecode(createcode(200))
print "OK"
