PROGRAM -> int main ( ) { STATEMENT_LANGUAGE }
STATEMENT_LANGUAGE -> STATEMENT
STATEMENT -> DECLARATION_STATEMENT
TYPE -> float
TYPE -> int
TYPE -> char
TYPE -> double
TYPE -> bool
DECLARATION_STATEMENT -> TYPE identifier DECLARATION_STATEMENT2
DECLARATION_STATEMENT2 -> ;
DECLARATION_STATEMENT2 -> , identifier DECLARATION_STATEMENT2
DECLARATION_STATEMENT2 -> = number DECLARATION_STATEMENT2