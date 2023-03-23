import os

from flask import Flask, send_from_directory

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

app = Flask(__name__, static_url_path='', static_folder=root)


@app.route('/', methods=['GET'])
def redirect_to_index():
    return send_from_directory(root, 'index.html')


if __name__ == '__main__':
    app.run()
