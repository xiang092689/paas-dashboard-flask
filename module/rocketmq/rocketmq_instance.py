from dataclasses import dataclass


@dataclass
class RocketmqInstance:
    name: str = ""
    namesrv_addr: str = ""
    cluster: str = ""

    def __init__(self, name: str):
        self.name = name
