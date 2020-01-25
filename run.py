from flask import Flask,request

from project_mysql import mysql_select, mysql_add, mysql_update, mysql_delete

app=Flask(__name__)


@app.route('/api/delete',methods=['POST','GET'])
def update_mysql_flask():

        id = request.args.get('id')

        print(id)
        delete_result=mysql_delete(id)

        return delete_result


@app.route('/api/update',methods=['POST','GET'])
def delete_mysql_flask():

        a = request.args.get('a')
        b = request.args.get('b')
        c = request.args.get('c')
        print(a,b,c)
        update_result=mysql_update(a,b,c)

        return update_result


@app.route('/api/select',methods=['POST','GET'])
def select_mysql_flask():

        id=request.args.get('id')
        print(id)
        id_resu=mysql_select(id)
        print(id_resu)
        return id_resu




@app.route('/api/insert',methods=['POST','GET'])
def insert_mysql_flash():

        a = request.args.get('a')
        b = request.args.get('b')
        c = request.args.get('c')
        d = request.args.get('d')

        insert_res=mysql_add(a,b,c,d)
        print(insert_res)
        return insert_res

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
