from enum import Enum


class TokenType(Enum):
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    INTEGER = "INTEGER"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    EQ = "EQ"
    TRUE = "TRUE"
    FALSE = "FALSE"
    DEFINE = "DEFINE"
    ID = "ID"
    PRINT = "PRINT"
    COND = "COND"
    LCOND = "LCOND"
    RCOND = "RCOND"
    ELSE = "ELSE"
