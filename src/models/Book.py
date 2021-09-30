from typing import List
from dataclasses import dataclass
from .Highlights import Highlights

@dataclass(frozen = True)
class Book:
    title: str
    publisher: str
    author: str
    highlights: List[Highlights]
