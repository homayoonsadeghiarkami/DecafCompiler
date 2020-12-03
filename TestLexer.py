from antlr4 import *
from DecafLexerer import DecafLexerer

_FILENAME = 'sample.script'


def getTokenType(token_type):
    switcher = {
        DecafLexerer.STRING: "STRING",
        DecafLexerer.LPAREN: "LPAREN",
        DecafLexerer.RPAREN: "RPAREN",
        DecafLexerer.EQUALS: "EQUALS",
        DecafLexerer.SEMICO: "SEMICO",
        DecafLexerer.ASSIGN: "ASSIGN"
    }
    return switcher.get(token_type, "OTHER")


def main():
    with open(_FILENAME, 'r') as reader:
        input_stream = InputStream(reader.read())
        lexer = DecafLexerer(input_stream)
        token = lexer.nextToken()
        i = 0
        while token.type != Token.EOF:
            print("[{}] {}   {}".format(
                i, getTokenType(token.type), token.text)
            )
            token = lexer.nextToken()
            i += 1


if __name__ == '__main__':
    main()