from datetime import datetime
from dataclasses import dataclass

@dataclass(frozen = True)
class Highlight:
    text: str
    location: str
    relative_page_number: int
    highlight_date: datetime
