from dataclasses import dataclass


@dataclass
class MogoInstance:
    name: str = ""
    host: str = ""
    port: str = ""

    def __init__(self, name: str):
        self.name = name
