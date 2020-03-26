import requests
import json
data = json.dumps({'text' : '测试算法服务打包'})
url = 'http://10.0.3.168:5000/participle'
res = requests.post(url, data=data)
print(res.json())
