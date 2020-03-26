from flask import Flask
from flask import request
from flask import Response
import json
import jieba
 
app = Flask(__name__)

@app.route('/participle', methods=['POST'])
def participle():
    try:
        data = json.loads(request.get_data(as_text=True))
        text = data['text']
        after_participle = list(jieba.cut(text))
        returndata = {
            'text': after_participle,
            'error': ''
        }
    except Exception as e:
        returndata = {
            'text': [],
            'error': format(e)
        }
    js = json.dumps(returndata)
    resp = Response(js, mimetype='application/json')
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
