from flask import Flask, request
from flask_cors import CORS
from ComputeCore.Core import Core

app = Flask(__name__)
CORS(app)
core_list = {}


@app.route('/connect', methods=['POST'])
def connect():
    origin = request.headers['Origin']
    core_list[origin] = Core()
    return 'Hi!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2019)
