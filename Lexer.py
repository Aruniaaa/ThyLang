import string
from string_with_Arrows import *
digits = string.digits
letters = string.ascii_letters
letters_digits  = letters + digits
import string
from tokens import *
from errors import IllegalCharError, ExpectedCharError
from position import Position






class Lexer:
    def __init__(self, file_name, text):
        self.text = text
        self.file_name = file_name
        self.pos = Position(-1, 1, -1, file_name, text)
        self.current_char = None
        self.advance()



    def advance(self):
        self.pos.advance(self.current_char)

        if self.pos.index < len(self.text):
            self.current_char = self.text[self.pos.index]

        else:
            self.current_char = None


    def makeNumber(self):
        num_str = ''
        dot_count = 0
        pos_st = self.pos.copy()
        while self.current_char != None and self.current_char in digits + ".":
            if self.current_char == ".":
                if dot_count == 1: break
                dot_count += 1
                num_str += "."
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str), pos_st, self.pos)
        else:
            return Token(TT_FLOAT, float(num_str), pos_st, self.pos)

    def make_identifier(self):
        id_str = ''
        pos_st  = self.pos.copy()

        while self.current_char != None and self.current_char in letters_digits + "_":
            id_str += self.current_char
            self.advance()

        tok_type = TT_KEYWORD if id_str in KEYWORDS else TT_IDENTIFIER
        return Token(tok_type, id_str, pos_st, self.pos)

    def make_not_equaLs(self):
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == "=":
            self.advance()
            return Token(TT_NOT_EQUAL, pos_start, pos_end=self.pos), None
        else:
            self.advance()
            return None, ExpectedCharError(pos_start, self.pos, f"Expected ‘{'='}’, but thy script delivereth none.")

    def make_equals(self):
        tok_type = TT_EQUAL_TO
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == "=":
            self.advance()
            tok_type = TT_EQUAL

        return Token(tok_type, pos_start, pos_end=self.pos), None

    def make_less_than(self):
        tok_type = TT_LESSTHAN
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == "=":
            self.advance()
            tok_type = TT_LESSTHAN_EQ

        return Token(tok_type, pos_start, pos_end=self.pos), None

    def make_greater_than(self):
        tok_type = TT_GRTRTHAN
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == "=":
            self.advance()
            tok_type = TT_GRT_EQ

        return Token(tok_type, pos_start, pos_end=self.pos), None

    def make_string(self):
        pos_st = self.pos.copy()
        string = ""
        escape_char = None
        self.advance()

        escape_characeters = {
            'n' : '\n',
            't' : '\t'
        }


        while (self.current_char != '"'  or escape_char )and self.current_char != None:
            if escape_char:
                string += escape_characeters.get(self.current_char, self.current_char)
            else:
             if self.current_char == '\\':
                escape_char = True
             else:
              string += self.current_char
            self.advance()
            escape_char = False

        self.advance()
    

        return Token(TT_STRING, string, pos_st, pos_end=self.pos), None

    def make_tokens(self):
       tokens = []
       while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in digits:
                tokens.append(self.makeNumber())
            elif self.current_char in letters:
                tokens.append(self.make_identifier())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS, pos_st=self.pos))
                self.advance()
            elif self.current_char == '"':
                string_token, error = self.make_string()
                if error: return [], error
                tokens.append(string_token)
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS, pos_st=self.pos))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MULTI, pos_st=self.pos))
                self.advance()
            elif self.current_char == '/':
                pos_start = self.pos.copy()
                self.advance()
                if self.current_char == "/":
                    tokens.append(Token(TT_FLOORDIV, pos_st=pos_start))
                    self.advance()
                else:
                    tokens.append(Token(TT_DIVISION, pos_st=pos_start))
                    self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN, pos_st=self.pos))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN, pos_st=self.pos))
                self.advance()
            elif self.current_char == '[':
                tokens.append(Token(TT_LEFT_SQ, pos_st=self.pos))
                self.advance()
            elif self.current_char == ']':
                tokens.append(Token(TT_RIGHT_SQ, pos_st=self.pos))
                self.advance()
            elif self.current_char == '^':
                tokens.append(Token(TT_POWER, pos_st=self.pos))
                self.advance()
            elif self.current_char == '=':
                pos_start = self.pos.copy()
                self.advance()
                if self.current_char == "=":
                    tokens.append(Token(TT_EQUAL, pos_st=pos_start))
                    self.advance()
                else:
                    tokens.append(Token(TT_EQUAL_TO, pos_st=pos_start))
            elif self.current_char == '>':
                pos_start = self.pos.copy()
                self.advance()
                if self.current_char == "=":
                    tokens.append(Token(TT_GRT_EQ, pos_st=pos_start))
                    self.advance()
                else:
                    tokens.append(Token(TT_GRTRTHAN, pos_st=pos_start))
            elif self.current_char == '<':
                pos_start = self.pos.copy()
                self.advance()
                if self.current_char == "=":
                    tokens.append(Token(TT_LESSTHAN_EQ, pos_st=pos_start))
                    self.advance()
                else:
                    tokens.append(Token(TT_LESSTHAN, pos_st=pos_start))
            elif self.current_char == '!':
                pos_start  = self.pos.copy()
                self.advance()
                if self.current_char == "=":
                  tokens.append(Token(TT_NOT_EQUAL, pos_st=pos_start))
                  self.advance()
                else:
                    pos_start = self.pos.copy()
                    char = self.current_char
                    self.advance()
                    return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")
            elif self.current_char == '#':
                break

            elif self.current_char == ',':
                tokens.append(Token(TT_COMMA, pos_st=self.pos))
                self.advance()

            elif self.current_char == ':':
                tokens.append(Token(TT_COLON, pos_st=self.pos))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")



       tokens.append(Token(TT_EOF, pos_st=self.pos))
       return tokens, None






