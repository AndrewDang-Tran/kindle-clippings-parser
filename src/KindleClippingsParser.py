import re
import zoneinfo

from datetime import datetime, timezone

from src.models import KindleClippings, Book, Highlight, KindleClippingsParserConfig

CLIPPING_DIVIDER = '==========';

class KindleClippingsParser:
    def __init__(self, config: KindleClippingsParserConfig):
        if config is None:
            raise AttributeError('Config is required')

        if config.convert_to_utc and (config.zone_info_key is None or config.zone_info_key == ''):
            zone_info_documentation = 'https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo.key'
            error_message = f'''Kindle Clippings default to local timezone when highlight is added.\n
                These are the available timezone configurations {zone_info_documentation}\n
                {zoneinfo.available_timezones()}
                '''
            raise AttributeError(error_message)

        self.config = config
        self.zone_info = zoneinfo.ZoneInfo(config.zone_info_key)

    def parse_kindle_clippings(self, file_path: str) -> KindleClippings:
        file = open(file_path)
        all_lines = file.read()
        file.close()

        highlights = all_lines.split(CLIPPING_DIVIDER)

        books = {}

        for highlight in highlights:
            lines = highlight.split('\n')
            lines = [l for l in lines if l]
            if len(lines) >= 3:
                book_line = lines[0]
                highlight_info_line = lines[1]
                highlighted_raw = lines[2].strip()
                title, publisher, author = self._parse_book_line(book_line)
                relative_page_number, location, created_date = self._parse_highlight_info_line(highlight_info_line)
                new_highlight = Highlight(highlighted_raw, location, relative_page_number, created_date)
                book_hash = hash(hash(title) + hash(publisher) + hash(author))

                book = None
                if book_hash in books:
                    book = books[book_hash]
                else:
                    book = Book(title, publisher, author, [])
                    books[book_hash] = book

                book.highlights.append(new_highlight)

        return KindleClippings(list(books.values()))


    def _parse_book_line(self, book_line: str):
        regex = r"\((.*?)\)"
        match = re.findall(regex, book_line)

        if len(match) == 2:
            publisher = match[0]
            title = book_line[: book_line.find(f'({publisher}')].strip()
            author = match[1]
            return title, publisher, author

        return None, None, None

    def _parse_highlight_info_line(self, highlight_info_line: str):
        regex = r"page (.*?) \| Location (.*?) \| Added on (.*)"
        match = re.search(regex, highlight_info_line)

        if match:
            relative_page_number = match.group(1)
            location = match.group(2)
            added_on_date = match.group(3)
            created_date = datetime.strptime(added_on_date, '%A, %B %d, %Y %I:%M:%S %p')
            something_else = created_date
            if self.config.convert_to_utc:
                created_date = created_date.replace(tzinfo=self.zone_info).astimezone(zoneinfo.ZoneInfo('UTC'))

            return relative_page_number, location, created_date

        return None, None, None
