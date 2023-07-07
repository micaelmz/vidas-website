# from flask import Flask, send_from_directory
# import os
#
# app = Flask(__name__)
#
# # Obtém o caminho absoluto para a pasta raiz do projeto
# root_dir = os.path.dirname(os.path.abspath(__file__))
#
# @app.route('/')
# def index():
#     return send_from_directory(root_dir, 'index.html')
#
# @app.route('/<path:path>')
# def serve_static(path):
#     return send_from_directory(root_dir, path)
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8002, debug=True)

from flask import Flask, send_from_directory, make_response
import os

app = Flask(__name__)

# Obtém o caminho absoluto para a pasta raiz do projeto
root_dir = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    response = make_response(send_from_directory(root_dir, 'index.html'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response

@app.route('/<path:path>')
def serve_static(path):
    response = make_response(send_from_directory(root_dir, path))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002, debug=True)
