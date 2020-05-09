from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    content = request.get_json()
    with open('bot-response.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=4)
    f.close()
    return 'JSON posted'
  
app.run(host='0.0.0.0', port= 8080)
