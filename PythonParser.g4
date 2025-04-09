// DELETE THIS CONTENT IF YOU PUT COMBINED GRAMMAR IN Parser TAB
lexer grammar ExprLexer;

BL: '\n' ; 
OTHER: 'or' ;
EQ : '=' ;
SEMI : ';' ;
PLUS : '+' ;
DOT : '.' ; 
J : 'J' ; 
MINUS : '-' ;
DEF : 'def' ;
IF : 'if' ;
ELSE : 'else' ; 
WHILE : 'while' ; 
BOOL : 'True' | 'False' ;
GREATER : '>' ;
LESSER : '<' ;
DIVIDE : '/';
COMPLEX: (INT | FLOAT )'+' (INT | FLOAT)  ('j'|'J');
INT : [0-9]+  ;
FLOAT : INT'.'INT | INT '.' | '.' INT ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
WS: [ \t\r\f]+ -> skip ;
