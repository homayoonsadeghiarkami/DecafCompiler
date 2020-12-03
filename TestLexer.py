from antlr4 import *
from DecafLexerer import DecafLexerer

_FILENAME = 'sample.script'


def main():
    with open(_FILENAME, 'r') as reader:
        input_stream = InputStream(reader.read())
        lexer = DecafLexerer(input_stream)
        token = lexer.nextToken()
        while token.type != Token.EOF:
            print(token.text)
            token = lexer.nextToken()


if __name__ == '__main__':
    main()