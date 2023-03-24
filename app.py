import os

from flask import Flask, send_from_directory
from flask_cors import CORS

from api.kafka.kafka_route import kafka_route
from api.kubernetes.kubernetes_route import kubernetes_route
from api.pulsar.pulsar_route import pulsar_route

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

app = Flask(__name__, static_url_path='', static_folder=root)
CORS(app)

app.register_blueprint(kafka_route, url_prefix='/api/kafka')
app.register_blueprint(kubernetes_route, url_prefix='/api/kubernetes')
app.register_blueprint(pulsar_route, url_prefix='/api/pulsar')


@app.route('/', methods=['GET'])
def redirect_to_index():
    return send_from_directory(root, 'index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=11111)
