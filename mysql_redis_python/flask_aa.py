from flask import Flask,request

app=Flask(__name__)



def to_id(id):
    if id == None:
       return "用户名不对或者密码错误"
    if id=="1":
       return "北京欢迎您"
    if id=="2":
       return  "济南欢迎您"
    if id=="3":
       return "郑州欢迎您:"
    
    return "不在服务区"

@app.route('/api/login')
def hello_world():

    id=request.args.get("id")
    aaa=to_id(id)
    return  aaa


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)

