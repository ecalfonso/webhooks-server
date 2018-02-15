from flask import Flask, request
import json
import subprocess

app = Flask(__name__)

#@app.route('/home/ecalfonso/webhooks-srv/working-dir/', methods=['GET'])
@app.route('/test', methods=['POST'])
def test():
    data = json.loads(request.data.decode('utf-8'))
    print(data['content'])
    subprocess.call("./test.sh", shell=True)
    return "OK"

@app.route('/test2', methods=['POST'])
def test2():
    data = json.loads(request.data.decode('utf-8'))
    print(data)
    return "OK"

if __name__ == '__main__':
    app.run()
