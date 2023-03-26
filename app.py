import os

from flask import Flask, send_from_directory
from flask_cors import CORS

from api.kafka_api.kafka_route import kafka_route
from api.kubernetes_api.kubernetes_route import kubernetes_route
from api.mogo_api.mogo_route import mogo_route
from api.pulsar_api.pulsar_route import pulsar_route
from api.redis_api.redis_route import redis_route
from api.rocketmq_api.rocketmq_route import rocketmq_route

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

app = Flask(__name__, static_url_path='', static_folder=root)
CORS(app)

app.register_blueprint(kafka_route, url_prefix='/api/kafka')
app.register_blueprint(kubernetes_route, url_prefix='/api/kubernetes')
app.register_blueprint(mogo_route, url_prefix='/api/mogo')
app.register_blueprint(pulsar_route, url_prefix='/api/pulsar')
app.register_blueprint(redis_route, url_prefix='/api/redis')
app.register_blueprint(rocketmq_route, url_prefix='/api/rocketmq')


@app.route('/', methods=['GET'])
@app.route('/kafka', methods=['GET'])
@app.route('/kubernetes', methods=['GET'])
@app.route('/mongo', methods=['GET'])
@app.route('/pulsar', methods=['GET'])
@app.route('/redis', methods=['GET'])
@app.route('/rocketmq', methods=['GET'])
def redirect_to_index():
    return send_from_directory(root, 'index.html')


@app.route('/kafka/<path>', methods=['GET'])
@app.route('/kubernetes/<path>', methods=['GET'])
@app.route('/mongo/<path>', methods=['GET'])
@app.route('/pulsar/<path>', methods=['GET'])
@app.route('/redis/<path>', methods=['GET'])
@app.route('/rocketmq/<path>', methods=['GET'])
def redirect_to_index_next(path):
    return send_from_directory(root, 'index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=11111)
