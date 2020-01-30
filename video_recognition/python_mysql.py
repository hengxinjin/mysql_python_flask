import pymysql
from flask import Flask,request




def inio_db():
    return   pymysql.connect(
             host='192.168.1.23',
             port=3306,
             database='hengxinjin',
             user='root',
             passwd='123456'
        )


app = Flask(__name__)
@app.route('/')
def test_file():
    return "当你看到这段文字的时候，说明已经找到了我"


@app.route('/api/add',methods=['POST'])
def add_mysql_sql():
    print('11111111111111111111111111111111111111')
    a = request.form.get('a')
    b = request.form.get('b')
    c = request.form.get('c')
    d = request.form.get('d')
    e = request.form.get('e')

    try:
        conn=inio_db()
        cursor=conn.cursor()
        sql='insert into pictures_project( name ,link,user,params,status)values("%s","%s","%s",%s,%s)'%(a,b,c,d,e)
        print('2222222222222222222222222222222222222222222')
        print(sql)
        cursor.execute(sql)
        print(sql)
        print("@@@@@@@@@@@@@@@@@@@@@")
        conn.commit()
        cursor.close()

        return " add sucessful"
    except:
        return "add fail"

@app.route('/api/query',methods=['POST'])
def query_mysql():
    conn=inio_db()
    cursor=conn.cursor()
    id=request.form.get('id')
    try:
        sql = 'select * from class_1 where id= %s' % id
        print(sql)
        cursor.execute(sql)
        print(sql)
        print("@@@@@@@@@@@@@@@@@@@@@")
        info = cursor.fetchall()
        conn.commit()
        dict01 = {}
        for i in info:
            dict01['id'] = i[0]
            dict01['name'] = i[1]
            dict01['link'] = i[2]
            dict01['user'] = i[3]
            dict01['params'] = i[4]
            dict01['status'] = i[5]

        return dict01

    except:
        print("query fail")
        return {}


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

