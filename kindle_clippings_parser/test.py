from kindle_clippings_parser.KindleClippingsParser import KindleClippingsParser
from models import KindleClippingsParserConfig

if __name__ == '__main__':
    config = KindleClippingsParserConfig(True, 'PST8PDT')
    parser = KindleClippingsParser(config)

    output = parser.parse_kindle_clippings('../example_clippings.txt')

    print()
