parser grammar ExprParser;
options { tokenVocab=ExprLexer; }


code: (stat)* EOF
    ;

stat: (expr | query | cond  | func_call |
func | loop_while | loop_for | PASS )
'\n'*
    ;


query: BOOL  
    | query OP_BOOL query
    | NOT query
    | '(' query ')'
    | expr (LESSER | GREATER |
    EQ2  ) expr
    ;
    
cond: IF (query | expr ) ':' BL stat+
    (ELIF (query | expr) ':' BL stat+)* 
    (ELSE ':' BL stat+)?;



expr: ID
    | INT
    | FLOAT
    | COMPLEX
    | expr (MUL | DIVIDE | POT ) expr
    | expr (PLUS | MINUS ) expr
    | ID ( EQ ) expr
    | '(' expr ')' 
    |func_call;
    
        
func : 'def' ID '(' params ')' ':' BL
stat*
(RETURN expr BL?)? ;

params: ( ID ',' ID* | ID |  'None')
  | (expr','expr* | expr | 'None');


func_call: ID '(' expr (','expr)* ')' ; 

loop_for: FOR ID IN RANGE  '(' 
(expr | expr',' expr | expr ',' expr ',' expr ) ')' 
':' BL  
   expr ;
    
        

loop_while: WHILE ( expr* | query* )
COLON
        stat* ;
