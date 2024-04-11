parser grammar Bananguage;

options { tokenVocab=BananguageLexer; }

program
    : statement*
    ;

statement
    : expr END
    | printStatement END
    | readStatement END
    ;

expr
    : assignment
    | arrayGet
    ;

assignment
    : floatAssignment
    | numAssignment
    | stringAssignment
    | booleanAssignment
    | idReassignment
    | arrayAssignment
    | arrayReassignment
    ;

floatAssignment
    : F64_TYPE ID ASSIGN value;

numAssignment
    : (INT_TYPE | LONG_TYPE) ID ASSIGN value;

stringAssignment
    : STRING_TYPE ID ASSIGN STRING_LITERAL;

booleanAssignment
    : BOOL_TYPE ID ASSIGN booleanExpr;

idReassignment
    : floatReassignment
    | intReassignment
    | longReassignment
    | stringReassignment;

floatReassignment
    : F64_TYPE ID ASSIGN ID;

intReassignment
    : INT_TYPE ID ASSIGN ID;

longReassignment
    : LONG_TYPE ID ASSIGN ID;

stringReassignment
    : STRING_TYPE ID ASSIGN ID;

arrayAssignment
    : arrayType ID ASSIGN LBRACK arrayItem* RBRACK;

arrayReassignment
    : (F64_TYPE | INT_TYPE | LONG_TYPE) ID ASSIGN arrayGet;

arrayType
    : ARRAY_TYPE LT type GT;

arrayItem: (numValue | floatValue) COMMA;

arrayGet
    : PEEL LPAREN ID DIGITS RPAREN;

type
    : F64_TYPE
    | LONG_TYPE;

value
    : numbers ( (ADD | SUB | MUL | DIV) numbers )* ;

floatValue: F64_TYPE FLOAT;
numValue: (INT_TYPE | LONG_TYPE) DIGITS;

numbers
    : FLOAT
    | DIGITS;

booleanExpr
    : TRUE
    | FALSE
    | ID
    | booleanExpr AND booleanExpr
    | booleanExpr OR booleanExpr
    | BANG booleanExpr
    | expr GT expr
    | expr LT expr
    | expr EQUAL expr
    | expr NOTEQUAL expr;

printStatement
    : PRINT LPAREN ID RPAREN;

readStatement
    : READ LPAREN ID RPAREN;