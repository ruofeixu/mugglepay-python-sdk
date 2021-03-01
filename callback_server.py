'''
Author: ruofei
Date: 2021-03-01 16:15:58
LastEditTime: 2021-03-01 16:45:17
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /mugglepay-python-sdk/example_callback_server.py
'''

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/muggle_callback_api', methods=['POST'])
def muggle_call_back():
    callback_info = request.json
    # 检查callback_info中的token字段来判断回调有效性，判断是否与创建时商户的token相同
    return callback_info

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)