from dataclasses import dataclass


@dataclass
class KafkaInstance:
    name: str = ""
    bootstrapServers: str = ""

    def __init__(self, name: str):
        self.name = name
