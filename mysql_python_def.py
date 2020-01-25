import pymysql

conn=pymysql.connect(
    host="192.168.1.23",
    port=3306,
    db='hengxinjin',
    user='root',
    passwd='123456',
    charset='utf8'
)
cursor=conn.cursor()
def select_mysql(id):

    sql='select * from class_1 where id=%s'%id
    cursor=excuse(sql)
    info=cursor.fetchall()

    dict01={}
    for item in info:
        print (item)
        dict01['name']=item[0]
        dict01['age']=item[1]
        dict01['sex'] = item[2]
        dict01['score'] = item[3]

        return dict01


def update_mysql(a,b,c):
    sql = 'update class_1 set %s=%s where id=%s'%(a,b,c)
    cursor = excuse(sql)

    cursor.commit()
    cursor.close()


    return 'you are right add'


def add_mysql():
    sql = 'insert into class_1 (name,age,sex,score)values(%s,%s,%s,%s)'%(a, b, c, d)
    cursor = excuse(sql)

    cursor.commit()
    cursor.close()

    return 'you are right  update'


def delete_mysql(a):
    sql = 'delete from class_1 where id=%s'%(a)
    cursor = excuse(sql)

    cursor.commit()
    cursor.close()

    return 'you are right delete'



























