# paas-dashboard-flask

## Test environment

```
KAFKA_DEFAULT_BOOTSTRAP_SERVERS=localhost:9092
PULSAR_DEFAULT_HOST=localhost
PULSAR_DEFAULT_TCP_PORT=6650
PULSAR_DEFAULT_WEB_PORT=8080
ZOOKEEPER_DEFAULT_ADDR=zookeeper-0.svc-zookeeper:2181
```

## generate requirements.txt
```bash
pip install pipreqs
pipreqs --encoding utf-8 . --force
```
