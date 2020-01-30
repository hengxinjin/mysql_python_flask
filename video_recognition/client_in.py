import requests

res={'a':'zdslgiu23','b':'http://192.168.1.23:1234/webwxgetvideo.mp4','c':'sorry','d':'{}','e':'0'}

#ress=requests.post('http://127.0.0.1:5000/api/delete',res_d)
res_query={'id':'11'}
res_delete={'id':"6"}


res_select = requests.post('http://192.168.1.23:8005/api/add', res)
print(res_select.text)

