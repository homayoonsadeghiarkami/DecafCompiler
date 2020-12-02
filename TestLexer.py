from antlr4 import *
from DecafLexerer import DecafLexerer

_FILENAME = '''// What to do in the morning
func morning <
  name := "Jay";
  greet morning=true input=@name;
  eat cereals;
  attend class="CS101";
>

// What to do at night
func night <
  brush_teeth;
  sleep hours=8;
>'''


def main():
    input_stream = InputStream(_FILENAME)
    lexer = DecafLexerer(input_stream)
    toks = CommonTokenStream(lexer)
    toks.fetch(500)
    for token in toks.tokens:
        print(token)


if __name__ == '__main__':
    main()