from dataclasses import dataclass


@dataclass
class Result:
    success: bool = False
    data: dict = None
    error: dict = None
