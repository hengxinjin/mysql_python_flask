import pymysql

conn=pymysql.connect(
    host='192.168.1.23',
    port=3306,
    user='root',
    db='hengxinjin',
    passwd='123456'
)

cursor=conn.cursor()

def mysql_delete(id):
    try:
        sql = "delete from class_1 where id = %s"%id
        # 执行SQL语句
        cursor.execute(sql)
        print(sql)
        # 在执行增删改操作时，需要向数据库提交操作，否则操作不成功
        #cursor.fetchall()
        conn.commit()
        # 关闭游标
        print('1111111111111111111112222222222222222222')
        cursor.close()
        return  "delete right"
    except:
        return "you are fail delete"

def mysql_update(a,b,c):
    try:
        sql = "update class_1 set %s ='%s' where id= %s "%(a,b,c)
        # 执行SQL语句
        cursor.execute(sql)
        print(sql)
        # 在执行增删改操作时，需要向数据库提交操作，否则操作不成功
        #cursor.fetchall()
        conn.commit()
        # 关闭游标
        print('1111111111111111111112222222222222222222')
        cursor.close()
        return  "update right"
    except:
        return "you are fail update"




def mysql_select(id):
    try:
        sql="select * from class_1 where id = %s"%id
        print(id)
        cursor.execute(sql)
        info=cursor.fetchall()
        dict01={}
        for i in info:
            dict01['id']   = i[0]
            dict01['name'] = i[1]
            dict01['age']  = i[2]
            dict01['score'] = i[3]

        print("id= %s, dict01= %s" % (id, dict01))
        return dict01
    except:
        return  "select fail"



def mysql_add(a,b,c,d):
    try:
        print('0000000000000000')
        sql=" insert into class_1 (name,age,sex,score) values ('%s',%s,'%s',%s)"%(a,b,c,d)
        print(sql)

        cursor.execute(sql)
        print("111111111111111111")
        conn.commit()
        print("22222222222222222")
        cursor.close()

        return "add success"

    except:
        return "add fail"
