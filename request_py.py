from flask import Flask,request

app=Flask(__name__)


@app.route('/',methods=['POST','GET'])
def request_select():

    id=request.form.get('id')
    select_my=select_mysql(id)

    return select_my


@app.route('/add',methods=['POST','GET'])
def request_select():

    a = request.form.get('a')
    b = request.form.get('b')
    c = request.form.get('c')
    d = request.form.get('d')

    add_sql=add_mysql(a,b,c,d)

    return add_sql



@app.route('/update',methods=['POST','GET'])
def request_select():

    a = request.form.get('a')
    b = request.form.get('b')
    c = request.form.get('c')

    insert_sql=insert_mysql(a,b,c)

    return insert_sql


@app.route('/delete', methods=['POST', 'GET'])
def request_select():
    a = request.form.get('a')


    delete_sql = delete_mysql(a)

    return delete_sql

if __name__ == '__main__':
    app.run()

































