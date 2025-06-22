from tokens import *
from tokens import Token


class VarAccessNode:
    def __init__(self, var_name_token):
        self.var_name_token = var_name_token
        self.pos_st = self.var_name_token.pos_st
        self.pos_end = self.var_name_token.pos_end


class VarAssignNode:
    def __init__(self, var_name, value_node):
        self.var_name = var_name
        self.value_node = value_node

        self.pos_st = self.var_name.pos_st
        self.pos_end = self.value_node.pos_end


class NumberNode:
    def __init__(self, tok):
        self.tok = tok
        self.pos_st = tok.pos_st
        self.pos_end = tok.pos_end

    def __repr__(self):
        return f"{self.tok}"
    

class StringNode:
    def __init__(self, tok):
        self.tok = tok
        self.pos_st = tok.pos_st
        self.pos_end = tok.pos_end

    def __repr__(self):
        return f"{self.tok}"


class BinOpNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node
        self.pos_st = left_node.pos_st
        self.pos_end = right_node.pos_end

    def __repr__(self):
        return f"({self.left_node}, {self.op_tok}, {self.right_node})"


class UnaryOpNode:
    def __init__(self, op_tok, node):
        self.op_tok = op_tok
        self.node = node
        self.pos_st = op_tok.pos_st
        self.pos_end = node.pos_end

    def __repr__(self):
        return f"({self.op_tok}, {self.node})"


class IfNode:
    def __init__(self, cases, else_case):
        self.cases = cases
        self.else_case = else_case

        self.pos_st = self.cases[0][0].pos_st
        self.pos_end = (self.else_case or self.cases[len(self.cases )- 1][0]).pos_end

        

class ForNode:
    def __init__(self, iterator_tok, start_value, end_value, body):
        self.iterator_tok = iterator_tok
        self.start_value = start_value
        self.end_value = end_value
        self.body = body
        self.pos_st = self.iterator_tok.pos_st\
        
        if isinstance(self.body, list) and len(self.body) > 0:
            self.pos_end = self.body[-1].pos_end  
        elif hasattr(self.body, 'pos_end'):
            self.pos_end = self.body.pos_end  
        else:
            self.pos_end = self.condition.pos_end 


class WhileNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


        self.pos_st = self.condition.pos_st

        if isinstance(self.body, list) and len(self.body) > 0:
            self.pos_end = self.body[-1].pos_end  
        elif hasattr(self.body, 'pos_end'):
            self.pos_end = self.body.pos_end  
        else:
            self.pos_end = self.condition.pos_end 


class FuncDefNode:
    def __init__(self, name, arguements, body):
        self.name = name
        self.body = body
        self.arguements = arguements

       
        self.pos_st = self.name.pos_st
        self.pos_end = self.body.pos_end
        


class FuncCallNode:
    def __init__(self, to_call, arguements):
        self.to_call = to_call
        self.arguements = arguements

        self.pos_st = self.to_call.pos_st

        if len(self.arguements) > 0:
            self.pos_end = self.arguements[-1].pos_end
        else:
            self.pos_end = self.to_call.pos_end


class ListNode:
    def __init__(self, elements, pos_st, pos_end):
        self.elements = elements
        self.pos_st = pos_st
        self.pos_end = pos_end


        
        
        