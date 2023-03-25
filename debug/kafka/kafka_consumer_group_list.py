from kafka import KafkaAdminClient

bootstrap_servers = "localhost:9092"
admin_client = KafkaAdminClient(
    bootstrap_servers=bootstrap_servers,
    client_id='flask-kafka_api-admin-client'
)
groups = admin_client.list_consumer_groups()
print(groups)
