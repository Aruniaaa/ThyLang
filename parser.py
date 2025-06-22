from nodes import *
from tokens import *
from errors import InvalidSyntaxError
from values import Strings




class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()

    def if_expr(self):
        res = ParserResult()
        cases = []
        else_case = None

        if not self.current_token.matches(TT_KEYWORD, "shouldst"):
            return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must declare a judgment, but where is thy 'shouldst'?"))

        res.register_advancements()
        self.advance()

        condition = res.register(self.expression())
        if res.error:
            return res
        

        if not self.current_token.matches(TT_KEYWORD, "so"):
            return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must declare a judgment, but where is thy 'so'?"))

        res.register_advancements()
        self.advance()

        expression = res.register(self.expression())
        if res.error:
            return res
        cases.append((condition, expression))

        while self.current_token.matches(TT_KEYWORD, "mayhaps"):
            res.register_advancements()
            self.advance()

            condition = res.register(self.expression())
            if res.error:
               return res
            
            
            if not self.current_token.matches(TT_KEYWORD, "so"):
               return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must declare a judgment, but where is thy 'so'?"))

            res.register_advancements()
            self.advance()

            expression = res.register(self.expression())
            if res.error:
                return res
            cases.append((condition, expression))

        if self.current_token.matches(TT_KEYWORD, "naughtwise"):
               res.register_advancements()
               self.advance()

               else_case  = res.register(self.expression())
               if res.error:
                   return res
        
        return res.success(IfNode(cases, else_case))




    def while_expr(self):
        res = ParserResult()
        expressions = []


        if not self.current_token.matches(TT_KEYWORD, "whilst"):
            return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must declare a loop, but where is thy 'whilst'?"))

        res.register_advancements()
        self.advance()

        condition = res.register(self.expression())
        
        
        if res.error:
            return res
        

        if not self.current_token.matches(TT_KEYWORD, "do"):
            return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must declare a loop, but where is thy 'do'?"))

        res.register_advancements()
        self.advance()

    
    
        if self.current_token.type != TT_LPAREN:
              return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must declare a loop, but where is thy '('?"))

        res.register_advancements()
        self.advance()

        expression = res.register(self.expression())
        if res.error:
            return res
        expressions.append(expression)

        while self.current_token.type == TT_COMMA:
                res.register_advancements()
                self.advance()
                expression = res.register(self.expression())
                if res.error:
                 return res
                expressions.append(expression)


        if self.current_token.type != TT_RPAREN:
              return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must declare a loop, but where is thy ')'?"))

        res.register_advancements()
        self.advance()

        return res.success(WhileNode(condition, expressions))


    def for_expr(self):
        res = ParserResult()
        expressions = []


        if not self.current_token.matches(TT_KEYWORD, "each"):
            return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must declare a judgment, but where is thy 'each'?"))

        res.register_advancements()
        self.advance()

        if self.current_token.type != TT_IDENTIFIER:
            return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must declare a judgment, but where is thy iterator?"))


        iterator = self.current_token
        if res.error:
            return res
        res.register_advancements()
        self.advance()   
        

        if not self.current_token.matches(TT_KEYWORD, "amongst"):
            return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must declare a judgment, but where is thy 'amongst'?"))

        res.register_advancements()
        self.advance()

        start_value = res.register(self.expression())
        if res.error: return res
    
        
        if not self.current_token.matches(TT_KEYWORD, "to"):
            return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must declare a judgment, but where is thy 'to'?"))

        res.register_advancements()
        self.advance()

        end_value = res.register(self.expression())
        if res.error: return res
      

        if not self.current_token.matches(TT_KEYWORD, "do"):
            return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must declare a judgment, but where is thy 'do'?"))

        res.register_advancements()
        self.advance()

         
        if self.current_token.type != TT_LPAREN:
              return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must declare a loop, but where is thy '('?"))
        
        res.register_advancements()
        self.advance()
        
        expression = res.register(self.expression())
        if res.error:
            return res
        expressions.append(expression)

        while self.current_token.type == TT_COMMA:
                res.register_advancements()
                self.advance()
                expression = res.register(self.expression())
                if res.error:
                 return res
                expressions.append(expression)


        if self.current_token.type != TT_RPAREN:
              return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must declare a loop, but where is thy ')'?"))

        res.register_advancements()
        self.advance()

        return res.success(ForNode(iterator, start_value, end_value, expressions))
       

    def func_def(self):
        res = ParserResult()

        if not self.current_token.matches(TT_KEYWORD, "craft"):
            return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must craft a function, but where is thy 'craft'?"))
        
        res.register_advancements()
        self.advance()

        if self.current_token.type != TT_IDENTIFIER:
              return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must craft a function, but where is thy name?"))
 
        
        elif self.current_token.type == TT_IDENTIFIER:
            name = self.current_token

        res.register_advancements()
        self.advance()
        
       

        if self.current_token.type != TT_LPAREN:
              return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must craft a function, but where is thy '('?"))

        res.register_advancements()
        self.advance()

        arguements = []

        if self.current_token.type == TT_IDENTIFIER:
            arguements.append(self.current_token)
                     
            res.register_advancements()
            self.advance()

            while self.current_token.type == TT_COMMA:
                res.register_advancements()
                self.advance()
                if self.current_token.type != TT_IDENTIFIER:
                 return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must craft a function, but where is thy name?"))
                else:
                      arguements.append(self.current_token)
                     
                      res.register_advancements()
                      self.advance()
              

        
        if self.current_token.type != TT_RPAREN:
              return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must craft a function, but where is thy ')'?"))

        res.register_advancements()
        self.advance()

        if self.current_token.type != TT_COLON:
              return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must craft a function, but where is thy ':'?"))

        res.register_advancements()
        self.advance()

        body = res.register(self.expression())
        if res.error:
            return res
        
        return res.success(FuncDefNode(name, arguements, body))






    def advance(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_token = self.tokens[self.tok_idx]
        return self.current_token

    def parse(self):
        res = self.expression()
        if not res.error and self.current_token.type != TT_EOF:
            return res.failure(InvalidSyntaxError(
                self.current_token.pos_st,
                self.current_token.pos_end,
                "The scroll thirsted for aught of +, −, /, ^, or *, yet thou didst deliver none. A grievous lapse in logic!"
            ))
        return res

    def call(self):
        res = ParserResult()
        atom = res.register(self.atom())
        if res.error: return res

        if self.current_token.type == TT_LPAREN:
            res.register_advancements()
            self.advance()
            arguements = []

            if self.current_token.type == TT_RPAREN:
             res.register_advancements()
             self.advance()
             return res.success(FuncCallNode(atom, arguements))
            else:
                arguements.append(res.register(self.expression()))
                if res.error:
                    
                  return res.failure(InvalidSyntaxError(
                     self.current_token.pos_st,
                     self.current_token.pos_end,
                    "Thou wast to bring forth a ), identifier, keyword, or a numeral, integer or float, yet thy offering was but naught." ))      
    
                else: 
                  while self.current_token.type == TT_COMMA:
                     res.register_advancements()
                     self.advance()
                     arguements.append(res.register(self.expression()))
                     if res.error: return res
                     
                  if self.current_token.type != TT_RPAREN:
                     return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must call a function, but where is thy ')'?"))
                  res.register_advancements()
                  self.advance()

                return res.success(FuncCallNode(atom, arguements))
        return res.success(atom)
                   

    def make_list(self):
        res = ParserResult()
        list_expr = []
       
        pos_st = self.current_token.pos_st.copy()

        if self.current_token.type != TT_LEFT_SQ:
             return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must declare a list, but where is thy '['?"))
        res.register_advancements()
        self.advance()

        
        element = res.register(self.expression())
        if element is not None:
                 list_expr.append(element)
    
        if res.error:           
            return res.failure(InvalidSyntaxError(
                     self.current_token.pos_st,
                     self.current_token.pos_end,
                    "Thou wast to bring forth a identifier, string, or a numeral, integer or float, yet thy offering was but naught." ))      
    
        else: 
            while self.current_token.type == TT_COMMA:
                res.register_advancements()
                self.advance()
                element = res.register(self.expression())
                if element is not None:
                    list_expr.append(element)
                  
            
                if res.error: return res
                 
                     
            if self.current_token.type != TT_RIGHT_SQ:
            
                return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, f"Thou must declare a list, but where is thy ']'?"))
            res.register_advancements()
            self.advance()
        
        return res.success(ListNode(list_expr, pos_st, self.current_token.pos_end.copy()))




    def atom(self):
        res = ParserResult()
        tok = self.current_token

        if tok.type in (TT_INT, TT_FLOAT):
            res.register_advancements()
            self.advance()
            return res.success(NumberNode(tok))
        
        elif tok.type == TT_STRING:
            res.register_advancements()
            self.advance()
            return res.success(StringNode(tok))

        elif tok.type == TT_IDENTIFIER:
            res.register_advancements()
            self.advance()
            return res.success(VarAccessNode(tok))

        elif tok.type == TT_LPAREN:
            res.register_advancements()
            self.advance()
            expr = res.register(self.expression())
            if res.error:
                return res
            if self.current_token.type == TT_RPAREN:
                res.register_advancements()
                self.advance()
                return res.success(expr)
            else:
                return res.failure(InvalidSyntaxError(
                    self.current_token.pos_st,
                    self.current_token.pos_end,
                    "Lo! A ')' was sought, yet none did appear"
                ))
        elif tok.matches(TT_KEYWORD, "shouldst"):
            if_expr = res.register(self.if_expr())
            if res.error:
                return res
            else:
                return res.success(if_expr)
        elif tok.matches(TT_KEYWORD, "whilst"):
            while_expr = res.register(self.while_expr())
            if res.error:
                return res
            else:
                return res.success(while_expr)
        elif tok.matches(TT_KEYWORD, "each"):
            for_expr = res.register(self.for_expr())
            if res.error:
                return res
            else:
                return res.success(for_expr)
            
        elif tok.matches(TT_KEYWORD, "craft"):
            func_def = res.register(self.func_def())
            if res.error:
                return res
            else:
                return res.success(func_def)
            
        elif tok.type == TT_LEFT_SQ:
            li = res.register(self.make_list())
            if res.error:
                return res
            else: 
                return res.success(li)

        return res.failure(InvalidSyntaxError(
            tok.pos_st,
            tok.pos_end,
            "Thou wast to bring forth a +, -, (, [, identifier, keyword, or a numeral, integer or float, yet thy offering was but naught."
        ))

    def power(self):
        return self.bin_op(self.call, (TT_POWER, ), self.factor)

    def factor(self):
        res = ParserResult()
        tok = self.current_token

        if tok.type in (TT_PLUS, TT_MINUS):
            res.register_advancements()
            self.advance()
            factor = res.register(self.factor())
            if res.error:
                return res
            return res.success(UnaryOpNode(tok, factor))
        else:
            return self.power()



    def term(self):
        return self.bin_op(self.factor, (TT_MULTI, TT_DIVISION, TT_MODULUS, TT_FLOORDIV, TT_POWER))


    def comp_expr(self):
        res = ParserResult()

        if self.current_token.matches(TT_KEYWORD, "not"):
            op_tok = self.current_token
            res.register_advancements()
            self.advance()
            node = res.register(self.comp_expr())
            if res.error: return res
            else:
                return res.success(UnaryOpNode(op_tok, node))
        else:
            node = res.register(self.bin_op(self.arithemetic, (TT_EQUAL, TT_NOT_EQUAL, TT_GRTRTHAN, TT_GRT_EQ, TT_LESSTHAN, TT_LESSTHAN_EQ)))
            if res.error:
                return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, "Thou wast to bring forth a +, -, (, identifier, 'not', or a numeral, integer or float, yet thy offering was but naught." ))

        return res.success(node)


    def arithemetic(self):
        return self.bin_op(self.term, (TT_PLUS, TT_MINUS))

    def expression(self):
        res = ParserResult()
     

        if self.current_token.matches(TT_KEYWORD, "hath"):
            res.register_advancements()
            self.advance()

            if self.current_token.type != TT_IDENTIFIER:
                return res.failure(InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, "Lo! The place for a name is barren"))
            else:
                var_name = self.current_token
                res.register_advancements()
                self.advance()
                if self.current_token.type != TT_EQUAL_TO:
                    return res.failure(
                        InvalidSyntaxError(self.current_token.pos_st, self.current_token.pos_end, "Wherefore is the assignment operator thou shouldst have spoken?"))
                else:
                    res.register_advancements()
                    self.advance()
                    expression = res.register(self.expression())
                    if res.error: return res
                    else: return res.success(VarAssignNode(var_name, expression))

        node = res.register(self.bin_op(self.comp_expr, ((TT_KEYWORD, "and"), (TT_KEYWORD, "or"))))



        return res.success(node)

    def bin_op(self, func_1, ops, func_2=None):
        if func_2 == None:
            func_2 = func_1
        res = ParserResult()
        left = res.register(func_1())
        if res.error:
            return res

        while self.current_token.type in ops or (self.current_token.type, self.current_token.value) in ops:
            op_tok = self.current_token
            res.register_advancements()
            self.advance()
            right = res.register(func_2())
            if res.error:
                return res
            left = BinOpNode(left, op_tok, right)

        return res.success(left)



class ParserResult:
    def __init__(self):
        self.error = None
        self.node = None

    def register(self, res):
          if res.error:
            self.error = res.error
    
          return res.node

    def register_advancements(self):
      pass

    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        if not self.error:
            self.error = error
        return self
