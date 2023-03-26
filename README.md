# paas-dashboard-flask

## Test environment

```
KAFKA_DEFAULT_BOOTSTRAP_SERVERS=localhost:9092
MOGO_DEFAULT_HOST=localhost
MOGO_DEFAULT_PORT=27017
PULSAR_DEFAULT_HOST=localhost
PULSAR_DEFAULT_TCP_PORT=6650
PULSAR_DEFAULT_WEB_PORT=8080
REDIS_DEFAULT_URL=redis://localhost:6379
REDIS_DEFAULT_CLUSTER_URL=redis://localhost:6379
ROCKETMQ_DEFAULT_NAMESRV_ADDR=localhost:9876
ROCKETMQ_DEFAULT_CLUSTER=DefaultCluster
ZOOKEEPER_DEFAULT_ADDR=zookeeper-0.svc-zookeeper:2181
```

## generate requirements.txt
```bash
pip install pipreqs
pipreqs --encoding utf-8 . --force
```
