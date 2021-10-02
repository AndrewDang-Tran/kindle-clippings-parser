from dataclasses import dataclass

@dataclass(frozen = True)
class KindleClippingsParserConfig:
    convert_to_utc: bool
    zone_info_key: str