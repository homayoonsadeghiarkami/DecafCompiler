from antlr4 import *
from DecafLexerer import DecafLexerer

_FILENAME = 'sample.script'

# # Function to convert number into string
# # Switcher is dictionary data type here
# def numbers_to_strings(argument):
# 	switcher = {
# 		0: "zero",
# 		1: "one",
# 		2: "two",
# 	}
#
# 	# get() method of dictionary data type returns
# 	# value of passed argument if it is present
# 	# in dictionary otherwise second argument will
# 	# be assigned as default value of passed argument
# 	return switcher.get(argument, "nothing")
#
# # Driver program
# if __name__ == "__main__":
# 	argument=0
# 	print (numbers_to_strings(argument))


def get_Token_Type(token_type):
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
                i, get_Token_Type(token.type), token.text)
            )
            token = lexer.nextToken()
            i += 1


if __name__ == '__main__':
    main()