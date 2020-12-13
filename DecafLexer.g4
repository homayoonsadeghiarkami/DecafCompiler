// Name our lexer (the name must match the filename)
lexer grammar DecafLexer;
// The upper means more priority
// Skip all spaces, tabs, newlines
WS : [ \t\r\n]+ -> skip ;

// Skip comments
LINE_COMMENT : '//' ~[\r\n]* '\r'? '\n' -> skip ;
MULTIPLE_COMMENTS : '/*' .*? '*/' '\r'? '\n' -> skip ;

// KeyWords
T_KEY_WORDS : (DATA_TYPE | LOOP | IF_CLAUSE | FOUNCTION | OTHER) ;
fragment DATA_TYPE : 'int'|'double'|'bool'|'string' |'void';
fragment LOOP : 'for'|'while'|'break' ;
fragment IF_CLAUSE : 'if'|'else' ;
fragment FOUNCTION: 'new'|'NewArray'|'Print'|'ReadInteger'|'ReadLine'| 'return' ;
fragment OTHER: 'null'|'this' ;

// T_STRING
T_STRING : ('"' (~[\r\n"])+ '"') | EMPTY_STRING ;
fragment EMPTY_STRING: '""' ;

// T_INT
T_INT : ([1-9]+ [0-9]*) | ([0][xX][0-9a-fA-F]+) ;

// T_DOUBLE
T_DOUBLE: ([0-9]+ [0-9]* '.' [0-9]*) | ([0-9]+ '.' [0-9] [0-9]* [eE][-+]?[0-9]+);

// T_BOOLEAN
T_BOOLEAN : ('true'|'false');

// T_ID
T_ID : ([a-zA-Z]('_' | [a-zA-Z0-9])*) ;

// Define PUNCTUATION
T_OPERATORS : (RELATIONAL | ARITHMETIC | LOGICAL | ASSIGNMENT | MISCELLANEOUS) ;
fragment RELATIONAL: '!=' | '>=' | '>' | '<' | '<='  | '==' ;
fragment ARITHMETIC: '+' | '-' | '*' | '/' | '%' ;
fragment LOGICAL: '&&' | '||' | '!' ;
fragment ASSIGNMENT: '=' ;
fragment MISCELLANEOUS: '[]' | '[' | ']' | '{'  | '}' |  '.' | '(' | ')' | ';' | ',';