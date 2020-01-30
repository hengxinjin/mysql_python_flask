import requests

add_mysql={"a":"xiaohong","b":"16","c":"w","d":"92"}


res=requests.post('127.0.0.1',add_mysql)
print (res)