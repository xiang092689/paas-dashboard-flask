from dataclasses import dataclass


@dataclass
class PulsarInstance:
    name: str = ""
    host: str = ""
    web_port: str = ""
    tcp_port: str = ""

    def __init__(self, name: str):
        self.name = name
