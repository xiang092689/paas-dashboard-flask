from kafka import KafkaAdminClient

bootstrap_servers = "localhost:9092"
admin_client = KafkaAdminClient(
    bootstrap_servers=bootstrap_servers,
    client_id='flask-kafka_api-admin-client'
)
topic_names = admin_client.list_topics()
print(topic_names)
