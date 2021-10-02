from typing import List
from dataclasses import dataclass
from .Highlight import Highlight

@dataclass
class Book:
    title: str
    publisher: str
    author: str
    highlights: List[Highlight]
