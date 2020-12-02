# Generated from src\DecafLexerer.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing import TextIO
import sys
# test
#homa is bitch


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("F\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\6\2\25\n\2\r\2\16\2\26\3\2\3\2\3")
        buf.write("\2\3\2\7\2\35\n\2\f\2\16\2 \13\2\3\2\5\2#\n\2\3\3\6\3")
        buf.write("&\n\3\r\3\16\3\'\3\3\3\3\3\4\3\4\3\4\3\4\7\4\60\n\4\f")
        buf.write("\4\16\4\63\13\4\3\4\5\4\66\n\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\2\2\n\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\3\2\7\6\2\62;B\\aac|\6\2\f\f\17")
        buf.write("\17$$^^\4\2$$^^\5\2\13\f\17\17\"\"\4\2\f\f\17\17\2L\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\3\"\3\2\2")
        buf.write("\2\5%\3\2\2\2\7+\3\2\2\2\t;\3\2\2\2\13=\3\2\2\2\r?\3\2")
        buf.write("\2\2\17A\3\2\2\2\21C\3\2\2\2\23\25\t\2\2\2\24\23\3\2\2")
        buf.write("\2\25\26\3\2\2\2\26\24\3\2\2\2\26\27\3\2\2\2\27#\3\2\2")
        buf.write("\2\30\36\7$\2\2\31\35\n\3\2\2\32\33\7^\2\2\33\35\t\4\2")
        buf.write("\2\34\31\3\2\2\2\34\32\3\2\2\2\35 \3\2\2\2\36\34\3\2\2")
        buf.write("\2\36\37\3\2\2\2\37!\3\2\2\2 \36\3\2\2\2!#\7$\2\2\"\24")
        buf.write("\3\2\2\2\"\30\3\2\2\2#\4\3\2\2\2$&\t\5\2\2%$\3\2\2\2&")
        buf.write("\'\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2()\3\2\2\2)*\b\3\2\2*")
        buf.write("\6\3\2\2\2+,\7\61\2\2,-\7\61\2\2-\61\3\2\2\2.\60\n\6\2")
        buf.write("\2/.\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62")
        buf.write("\65\3\2\2\2\63\61\3\2\2\2\64\66\7\17\2\2\65\64\3\2\2\2")
        buf.write("\65\66\3\2\2\2\66\67\3\2\2\2\678\7\f\2\289\3\2\2\29:\b")
        buf.write("\4\2\2:\b\3\2\2\2;<\7>\2\2<\n\3\2\2\2=>\7@\2\2>\f\3\2")
        buf.write("\2\2?@\7?\2\2@\16\3\2\2\2AB\7=\2\2B\20\3\2\2\2CD\7<\2")
        buf.write("\2DE\7?\2\2E\22\3\2\2\2\n\2\26\34\36\"\'\61\65\3\b\2\2")
        return buf.getvalue()


class DecafLexerer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    STRING = 1
    WS = 2
    LINE_COMMENT = 3
    LPAREN = 4
    RPAREN = 5
    EQUALS = 6
    SEMICO = 7
    ASSIGN = 8

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>",
                    "'<'", "'>'", "'='", "';'", "':='"]

    symbolicNames = ["<INVALID>",
                     "STRING", "WS", "LINE_COMMENT", "LPAREN", "RPAREN", "EQUALS",
                     "SEMICO", "ASSIGN"]

    ruleNames = ["STRING", "WS", "LINE_COMMENT", "LPAREN", "RPAREN", "EQUALS",
                 "SEMICO", "ASSIGN"]

    grammarFileName = "DecafLexerer.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(
            self, self.atn, self.decisionsToDFA, PredictionContextCache()
        )
        self._actions = None
        self._predicates = None
