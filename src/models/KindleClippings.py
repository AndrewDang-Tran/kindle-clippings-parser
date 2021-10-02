from typing import List
from dataclasses import dataclass
from .Book import Book

@dataclass(frozen = True)
class KindleClippings:
    books: List[Book]
