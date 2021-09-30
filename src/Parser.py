

CLIPPING_DIVIDER = '==========';

def parse_kindle_clippings(file_path: str):
    file = open(file_path):
    all_lines = file.read()
    file.close()

    highlights = all_lines.split(CLIPPING_DIVIDER)

    for highlight in highlights:



def _parse_highlight(highlight: str):
    lines = highlight.split('\n')
    book_line = lines[0]
    highlight_info_line = lines[1]
    highlighted_raw = lines[3]


def _parse_book_line(book_line: str):
    regex = r"\((.*?)\)"
    match = re.search("\((.*)\)", book_line)

    if match:
        title = author_line[: match.start()]
        publisher = match.group(0)
        author = match.group(1)
        return title, publisher, author

    return None, None, None

def _parse_highlight_info_line(highlight_info_line: str):
    return

