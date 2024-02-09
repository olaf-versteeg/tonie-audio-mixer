from dataclasses import dataclass


@dataclass
class Song:
    name: str
    path: str
    length: float
