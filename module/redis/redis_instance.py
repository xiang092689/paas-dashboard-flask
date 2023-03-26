from dataclasses import dataclass


@dataclass
class RedisInstance:
    name: str = ""
    url: str = ""
    cluster_url: str = ""

    def __init__(self, name: str):
        self.name = name
