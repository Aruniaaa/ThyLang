from tokens import *
from errors import RunTimeError
from errors import *
from run_time_result import RTResult






class Context:
    def __init__(self, display_name, parent=None, parent_entry_pos=None):
        self.display_name = display_name
        self.parent  = parent
        self.parent_entry_pos = parent_entry_pos
        self.symbol_table = None

class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent

    def get(self, name):
        value = self.symbols.get(name, None)
        if value == None and self.parent:
            return self.parent.get(name)
        return value

    def set(self, name, value):
        self.symbols[name] = value

    def remove(self, name):
        del self.symbols[name]

class Interpreter:
   
    def visit(self, node, context):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node, context)

    def no_visit_method(self, node, context):
        raise Exception(f"Verily, no method of ‘visit_{type(node).__name__}’ is inscribed in these sacred scripts.")

    def visit_NumberNode(self, node, context):
        from values import Numbers
        return RTResult().success(
            Numbers(node.tok.value).set_context(context).set_pos(node.pos_st, node.pos_end)
         )

    def visit_VarAccessNode(self, node, context):
        res = RTResult()
        var_name = node.var_name_token.value
        value  = context.symbol_table.get(var_name)

        if not value:
            return res.failure(RunTimeError(
                node.pos_st, node.pos_end, f"Verily, no variable of '{var_name}' is inscribed in these sacred scripts.", context
            ))
        else:
            return res.success(value)

    def visit_VarAssignNode(self, node, context):
        res = RTResult()
        var_name = node.var_name.value
        value = res.register(self.visit(node.value_node, context))
        if res.error: return res
        else:
            context.symbol_table.set(var_name, value)
            return res.success(value)

    


    def visit_BinOpNode(self, node, context):
        res = RTResult()
        left = res.register(self.visit(node.left_node, context))
        if res.error : return res
        right = res.register(self.visit(node.right_node, context))
        if res.error : return res

        if node.op_tok.type == TT_PLUS:
            result, error = left.add(right)
        elif node.op_tok.type == TT_MINUS:
            result, error = left.subtract(right)
        elif node.op_tok.type == TT_MULTI:
            result, error = left.multiply(right)
        elif node.op_tok.type == TT_DIVISION:             
            result, error = left.divide(right)
        elif node.op_tok.type == TT_POWER:
            result, error = left.exponentation(right)
        elif node.op_tok.type == TT_EQUAL:
            result, error = left.double_equal_to(right)
        elif node.op_tok.type == TT_NOT_EQUAL:
            result, error = left.not_equal_to(right)
        elif node.op_tok.type == TT_GRTRTHAN:
            result, error = left.greater_than(right)
        elif node.op_tok.type == TT_LESSTHAN:
            result, error = left.less_than(right)
        elif node.op_tok.type == TT_FLOORDIV:
            result, error = left.floor_divide(right)
        elif node.op_tok.type == TT_LESSTHAN_EQ:
            result, error = left.less_eq(right)
        elif node.op_tok.type == TT_GRT_EQ:
            result, error = left.grtr_eq(right)
        elif node.op_tok.matches(TT_KEYWORD, "and"):
            result, error = left.anded(right)
        elif node.op_tok.matches(TT_KEYWORD, "or"):
            result, error = left.ored(right)

        if error:                                                     
            return res.failure(error)
        else:
            return res.success(result.set_pos(node.pos_st, node.pos_end))


    def visit_IfNode(self, node, context):
        res = RTResult()

        for condition, expression in node.cases:
            condition_value = res.register(self.visit(condition, context))
            if res.error:
                return res
            
            if condition_value.is_true():
                  expression_value = res.register(self.visit(expression, context))
                  if res.error:
                      return res
                  else:
                      return res.success(expression_value)
        if node.else_case:
            else_value = res.register(self.visit(node.else_case, context))
            if res.error:
                      return res
            else:
                return res.success(else_value)
            
        return res.success(None)
    

    def visit_WhileNode(self, node, context):
        from values import  Lists
        res = RTResult()
        elements = []

        while True:
            condition = res.register(self.visit(node.condition, context))
          
            if res.error: return res

            if not condition.is_true(): break

            results = []
            for statement in node.body:  
                result = res.register(self.visit(statement, context))
                if res.error: return res
                else:
                    results.append(result)
            
            if len(results) == 1:
                elements.append(results[0])  
            else:
               elements.append(results) 
           

        return res.success(Lists(elements).set_context(context).set_pos(node.pos_st, node.pos_end))
    
    def visit_ForNode(self, node, context):
        from values import Numbers, Lists
        res = RTResult()
        elements = []

        start_value = res.register(self.visit(node.start_value, context))
        if res.error : return res

        
        end_value = res.register(self.visit(node.end_value, context))
        if res.error : return res

        if res.error : return res

        start = start_value.value
        end = end_value.value
        iterator = start

        if start > end:
         while iterator >= end:
            context.symbol_table.set(node.iterator_tok.value, Numbers(iterator))
            iterator -= 1

            results = []
            for statement in node.body:  
                result = res.register(self.visit(statement, context))
                if res.error: return res
                else:
                    results.append(result)
            
            if len(results) == 1:
                elements.append(results[0])  
            else:
               elements.append(results) 

        else:
         while iterator <= end:
            context.symbol_table.set(node.iterator_tok.value, Numbers(iterator))
            iterator += 1

            results = []
            for statement in node.body:  
                result = res.register(self.visit(statement, context))
                if res.error: return res
                else:
                    results.append(result)
            
            if len(results) == 1:
                elements.append(results[0])  
            else:
               elements.append(results) 
        
        return res.success(Lists(elements).set_context(context).set_pos(node.pos_st, node.pos_end))




    def visit_UnaryOpNode(self, node, context):
        from values import Numbers
        res = RTResult()
        number = res.register(self.visit(node.node, context))
        if res.error : return res

        if node.op_tok.type == TT_MINUS:
            number, error = number.multiply(Numbers(-1))
        elif node.op_tok.type == TT_PLUS:
            number, error = number.multiply(Numbers(1))
        elif node.op_tok.matches(TT_KEYWORD, "not"):
            result, error = number.notted()

        if error:
            return res.failure(error)
        else:
            return res.success(number.set_pos(node.pos_st, node.pos_end))
        
    
    def visit_FuncDefNode(self, node, context):
        from values import Functions
        res = RTResult()

        func_name = node.name.value
        body = node.body
        arguement_names = [arguement_name.value for arguement_name in node.arguements]
        func_value = Functions(func_name, body, arguement_names).set_context(context).set_pos(node.pos_st, node.pos_end)
        context.symbol_table.set(func_name, func_value)


        return res.success(func_value)
    
    def visit_FuncCallNode(self, node, context):
        res = RTResult()
        argues = []
        

        value_to_call = res.register(self.visit(node.to_call, context))
        if res.error: return res

        value_to_call = value_to_call.copy().set_pos(node.pos_st, node.pos_end)

        for arg_nodes in node.arguements:
            argument_value = res.register(self.visit(arg_nodes, context))
            if res.error:
                return res
            argues.append(argument_value)
            
        return_value = res.register(value_to_call.execute(argues))
        if res.error:
            return res
        return_value = return_value.copy().set_pos(node.pos_st, node.pos_end).set_context(context)
        
        return res.success(return_value)
    
    def visit_StringNode(self, node, context):
        from values import Strings
        return RTResult().success(Strings(node.tok.value).set_context(context).set_pos(node.pos_st, node.pos_end))
  
    def visit_ListNode(self, node, context):
        from values import Lists
        res = RTResult()
        self.node = node
        self.context = context
        elements = []

        for element in node.elements:
            elements.append(res.register(self.visit(element, context)))
            if res.error: return res

        return res.success(Lists(elements).set_context(context).set_pos(node.pos_st, node.pos_end))



