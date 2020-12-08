from antlr4 import *
from DecafLexer import DecafLexer

_FILENAME = 'sample.script'


def getTokenType(token_type):
    switcher = {
        DecafLexer.T_INT: "T_INT",
        DecafLexer.T_DOUBLE: "T_DOUBLE",
        DecafLexer.T_BOOLEAN: "T_BOOLEAN",
        DecafLexer.T_ID: "T_ID",
        DecafLexer.T_HEX: "T_HEX",
        DecafLexer.T_STRING: "T_STRING",
        DecafLexer.T_KEY_WORDS: "T_KEY_WORDS",
        DecafLexer.T_PUNCTUATION: "T_PUNCTUATION"
    }
    return switcher.get(token_type, "UNDEFINED_TOKEN")


def main():
    with open(_FILENAME, 'r') as reader:
        input_stream = InputStream(reader.read())
        lexer = DecafLexer(input_stream)
        token = lexer.nextToken()
        valid_token = ["T_ID", "T_STRING", "T_BOOLEAN", "T_DOUBLE", "T_INT"]
        i = 0
        while token.type != Token.EOF:
            # print("[{}] {}   {}".format(
            #     i, getTokenType(token.type), token.text)
            # )
            if getTokenType(token.type) in valid_token:
                print(getTokenType(token.type), token.text)
            else:
                print(token.text)
            token = lexer.nextToken()
            i += 1


if __name__ == '__main__':
    main()