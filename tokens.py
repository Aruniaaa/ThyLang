TT_INT = "INT"
TT_FLOAT = "FLOAT"
TT_STRING = "STRING"
TT_PLUS = "PLUS"
TT_MINUS = "MINUS"
TT_MULTI = "MULTI"
TT_DIVISION = "DIVISION"
TT_MODULUS = "MODULUS"
TT_FLOORDIV = "FLOORDIV"
TT_GRTRTHAN = "GRTRTHAN"
TT_LESSTHAN = "LESSTHAN"
TT_RPAREN = "RPAREN"
TT_LPAREN = "LPAREN"
TT_EOF = 'EOF'
TT_POWER = "POWER"
TT_IDENTIFIER  =  "IDENTIFIER"
TT_KEYWORD = "KEYWORD"
TT_EQUAL_TO = "EQUAL_TO"
TT_COMMA = "TT_COMMA"
TT_COLON = "TT_COLON"
TT_LEFT_SQ = "LEFT_SQUARE_BRACKET"
TT_RIGHT_SQ = "RIGHT_SQUARE_BRACKET"
TT_EQUAL = "DOUBLE_EQUAL_TO"
TT_NOT_EQUAL = "NOT_EQUAL_TO"
TT_GRT_EQ = "GREATER_THAN_OR_EQUALS"
TT_LESSTHAN_EQ = "LESS_THAN_OR_EQUALS"
KEYWORDS = ["hath", "and", "not", "or", "shouldst", "mayhaps", "so", "naughtwise", "whilst", "each", "amongst", "do", "to", "craft"]



class Token:
    def __init__(self, type, value=None, pos_st=None, pos_end=None):

        self.value = value
        self.type = type

        if pos_st:
            self.pos_st = pos_st.copy()
            self.pos_end = pos_st.copy()
            self.pos_end.advance()

        if pos_end:
         self.pos_end = pos_end

    def matches(self, type, value):
        return self.type == type and self.value == value

    def __repr__(self):
        if self.value: return f"{self.type} : {self.value}"
        return f"{self.type}"