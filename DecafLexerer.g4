// Name our lexer (the name must match the filename)
lexer grammar DecafLexerer;

// Skip all spaces, tabs, newlines
WS : [ \t\r\n]+ -> skip ;

// Skip comments
LINE_COMMENT : '//' ~[\r\n]* '\r'? '\n' -> skip ;
MULTIPLE_COMMENTS : '/*' .*? '*/' '\r'? '\n' -> skip ;

// KeyWords
T_KEY_WORDS : 'if'|'void'|'int'|'double'|'bool'|'string'|'null'|'this'|'for'|'while'|'else'|'return'|'break'|'new'|'NewArray'|'Print'|'ReadInteger'|'ReadLine';

// T_STRING
T_STRING : '"' ( ESC | .)*? '"' ;
fragment ESC : '\\' [btnr"\\] ;

// T_INT
T_INT : [1-9]+ [0-9]* ;

// T_DOUBLE
T_DOUBLE: [0-9]+ [0-9]* '.' [0-9]* | ([0-9]+ '.' [0-9] [0-9]* ('e' | 'E') ('-' | '+')? [0-9]+);

// T_BOOLEAN
T_BOOLEAN : ('true'|'false');

// T_ID
T_ID : [a-zA-Z] [a-zA-Z0-9]* [_]?;

// Define PUNCTUATION
T_PUNCTUATION : '+' | '-' | '[' | '{' | ']' | '}' | '!=' | '>=' | '>' | '*' | '<' | '<=' | '=' | '==' | '&&' | '||' | '!' | '.' | '(' | ')' | ';' | ',';

