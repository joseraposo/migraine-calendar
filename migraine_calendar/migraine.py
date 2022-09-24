from dataclasses import dataclass


@dataclass
class Migraine:
    start: str
    stop: str
    intensity: int
    medication: str
    reason: int
    notes: str
