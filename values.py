from errors import RunTimeError
from run_time_result import RTResult
from interpreter import Context, SymbolTable





class Value:
	def __init__(self):
		self.set_pos()
		self.set_context()

	def set_pos(self, pos_st=None, pos_end=None):
		self.pos_st = pos_st
		self.pos_end = pos_end
		return self

	def set_context(self, context=None):
		self.context = context
		return self

	def add(self, other):
		return None, self.illegal_operation(other)

	def subtract(self, other):
		return None, self.illegal_operation(other)

	def multiply(self, other):
		return None, self.illegal_operation(other)

	def divide(self, other):
		return None, self.illegal_operation(other)

	def exponentation(self, other):
		return None, self.illegal_operation(other)

	def double_equal_to(self, other):
		return None, self.illegal_operation(other)

	def not_equal_to(self, other):
		return None, self.illegal_operation(other)

	def less_than(self, other):
		return None, self.illegal_operation(other)

	def greater_than(self, other):
		return None, self.illegal_operation(other)

	def less_eq(self, other):
		return None, self.illegal_operation(other)

	def grtr_eq(self, other):
		return None, self.illegal_operation(other)

	def anded(self, other):
		return None, self.illegal_operation(other)

	def ored(self, other):
		return None, self.illegal_operation(other)

	def notted(self, other):
		return None, self.illegal_operation(other)

	def execute(self, args):
		return RTResult().failure(self.illegal_operation())

	def copy(self):
		raise Exception("Alas! Thou hast summoned forth an object most barren, devoid of the sacred rite of duplication!")

	def is_true(self):
		return False

	def illegal_operation(self, other=None):
		if not other: other = self
		return RuntimeError(
			self.pos_st, other.pos_end,
			'Hark! Thou hast attempted an operation most grievous and forbidden!',
			self.context
		)




class Numbers(Value):
    def __init__(self, value):
         super().__init__()
         self.value = value


    def add(self, other):
      if isinstance(other, Numbers):
        return Numbers(self.value + other.value).set_context(self.context), None
      

    def subtract(self, other):
        if isinstance(other, Numbers):
            return Numbers(self.value - other.value).set_context(self.context), None
        return None, Value.illegal_operation(self, other)


    def multiply(self, other):
        if isinstance(other, Numbers):
            return Numbers(self.value * other.value).set_context(self.context), None
        return None, Value.illegal_operation(self, other)


    def double_equal_to(self, other):
        if isinstance(other, Numbers):
            if self.value == other.value:
                return Numbers(1).set_context(self.context), None
            else:
                return Numbers(0).set_context(self.context), None
        return None, Value.illegal_operation(self, other)    
        

    def not_equal_to(self, other):
        if isinstance(other, Numbers):
            if self.value != other.value:
                return Numbers(1).set_context(self.context), None
            else:
                return Numbers(0).set_context(self.context), None
        return None, Value.illegal_operation(self, other)    
        

    def greater_than(self, other):
        if isinstance(other, Numbers):
            if self.value > other.value:
                return Numbers(1).set_context(self.context), None
            else:
                return Numbers(0).set_context(self.context), None
        return None, Value.illegal_operation(self, other)    
        

    def less_than(self, other):
        if isinstance(other, Numbers):
            if self.value < other.value:
                return Numbers(1).set_context(self.context), None
            else:
                return Numbers(0).set_context(self.context), None
        return None, Value.illegal_operation(self, other)    
        

    def less_eq(self, other):
        if isinstance(other, Numbers):
            if self.value <= other.value:
                return Numbers(1).set_context(self.context), None
            else:
                return Numbers(0).set_context(self.context), None
        return None, Value.illegal_operation(self, other)    
        

    def grtr_eq(self, other):
        if isinstance(other, Numbers):
            if self.value >= other.value:
                return Numbers(1).set_context(self.context), None
            else:
                return Numbers(0).set_context(self.context), None
        return None, Value.illegal_operation(self, other)    
        

    def anded(self, other):
        if isinstance(other, Numbers):
            if self.value and other.value:
                return Numbers(1).set_context(self.context), None
            else:
                return Numbers(0).set_context(self.context), None
        return None, Value.illegal_operation(self, other)    
        

    def ored(self, other):
        if isinstance(other, Numbers):
            if self.value or other.value:
                return Numbers(1).set_context(self.context), None
            else:
                return Numbers(0).set_context(self.context), None
        return None, Value.illegal_operation(self, other)    
        

    def divide(self, other):
        if isinstance(other, Numbers):
            if other.value == 0:
                return None, RunTimeError(other.pos_st, other.pos_end, "Thou dared divide by naught.", self.context)
            else:
                return Numbers(self.value / other.value).set_context(self.context), None
        return None, Value.illegal_operation(self, other)


    def notted(self):
        return Numbers(1 if self.value == 0 else 0).set_context(self.context), None

    def floor_divide(self, other):
        if isinstance(other, Numbers):
            if other.value == 0:
                return None, RunTimeError(other.pos_st, other.pos_end, "Thou dared divide by naught.", self.context)
            else:
                return Numbers(self.value // other.value).set_context(self.context), None
            
        return None, Value.illegal_operation(self, other)

    def exponentation(self, other):
        if isinstance(other, Numbers):
            return Numbers(self.value ** other.value).set_context(self.context), None
        
        return None, Value.illegal_operation(self, other)
        


    def copy(self):
        copy = Numbers(self.value)
        copy.set_pos(self.pos_st, self.pos_end)
        copy.set_context(self.context)
        return copy
    
	   

    def is_true(self):
        return self.value != 0

    def __repr__(self):
        return str(self.value)

Numbers.true = Numbers(1)
Numbers.false = Numbers(0)



class Strings(Value):
     def __init__(self, value):
          super().__init__()
          self.value = value

     def add(self, string2):
          if isinstance(string2, Strings):
             return Strings(self.value + string2.value).set_context(self.context), None
          else:
               return None, Value.illegal_operation(self, string2)
          
    
     def multiply(self, num):
          if isinstance(num, Numbers):
             return Strings(self.value * num.value).set_context(self.context), None
          else:
               return None, Value.illegal_operation(self, num)
   
         
          
     def copy(self):
         copy = Strings(self.value)
         copy.set_context(self.context)
         copy.set_pos(self.pos_st, self.pos_end)
         return copy
     

     def __str__(self):
          return self.value
     
     def __repr__(self):
          return f'"{self.value}"'
    
     
      
class BaseFunctions(Value):
     def __init__(self, name):
          super().__init__()
          self.name = name

    
     def generate_context(self):
         new_context = Context(self.name, self.context, self.pos_st)
         parent_symbol_table = None
         if new_context.parent and hasattr(new_context.parent, 'symbol_table'):
             parent_symbol_table = new_context.parent.symbol_table
         new_context.symbol_table = SymbolTable(parent_symbol_table)
         return new_context
     
     def check_agrs(self, argues, arguements):
            res = RTResult()
            if len(argues) > len(arguements):
             return res.failure(RunTimeError(self.pos_st, self.pos_end, f" Hold! Thou hast overwhelmed '{self.name}' function with {len(argues) - len(arguements)} excessive arguments!", self.context))
        
            elif len(argues) < len(arguements):
               return res.failure(RunTimeError(self.pos_st, self.pos_end, f"Verily, '{self.name}' function doth hunger for {len(arguements) - len(argues)} more parameters than thou hast given!", self.context))
             
            return res.success(None)
     
     def populate_arguements(self, argues, arguements, exec_context):
             for i in range(len(argues)):
                  arguement_name = arguements[i]
                  arguement_value = argues[i]
                  arguement_value.set_context(exec_context)
                  exec_context.symbol_table.set(arguement_name, arguement_value)

     def populate_and_check(self, argues, arguements, exec_context):
          res = RTResult()
          res.register(self.check_agrs(argues, arguements))
          if res.error: return res
          self.populate_arguements(argues, arguements, exec_context)
          return res.success(None)

     
     
     



class Functions(BaseFunctions):
    def __init__(self, name, body, arguements):
         super().__init__(name)
         self.body = body
         self.arguements = arguements
 
       
    def execute(self, args):
        return self.exec(args)
    
    def exec(self, argues):
        from interpreter import Interpreter
        res = RTResult()
        interpreter = Interpreter()
        new_context = self.generate_context()
        

        res.register(self.populate_and_check(argues, self.arguements, new_context))
        if res.error: return res
            
        value = res.register(interpreter.visit(self.body, new_context))
        if res.error:
                  return res
        return res.success(value)
        
    def copy(self):
         copy = Functions(self.name, self.body, self.arguements)
         copy.set_context(self.context)
         copy.set_pos(self.pos_st, self.pos_end)
         return copy
    
    def __repr__(self):
         return f"<function {self.name}>"
    


class Lists(Value):
     def __init__(self, elements):
          super().__init__()
          self.elements = elements

     def __iter__(self):
      return iter(self.elements)

    

     def add(self, other):
          new_list = []
          if isinstance(other, Numbers):
               for i in self:
                    res, error = i.add(other)
                    if error: return None, error
                    new_list.append(res)
               return Lists(new_list), None
          elif isinstance(other, Lists):
               other = list(other.elements)
               for i in self:
                    for j in other:
                          res, error = i.add(j)
                          if error: return None, error
                          new_list.append(res)
               return Lists(new_list), None
          else:
               return None, Value.illegal_operation(self, other)
          
     def subtract(self, other):
          new_list = []
          if isinstance(other, Numbers):
               for i in self:
                    res, error = i.subtract(other)
                    if error: return None, error
                    new_list.append(res)
               return Lists(new_list), None
          elif isinstance(other, Lists):
               other = list(other.elements)
               for i in self:
                    for j in other:
                          res, error = i.subtract(j)
                          if error: return None, error
                          new_list.append(res)
               return Lists(new_list), None
          else:
               return None, Value.illegal_operation(self, other)
          
     def multiply(self, other):
          new_list = []
          if isinstance(other, Numbers):
               for i in self:
                    res, error = i.multiply(other)
                    if error: return None, error
                    new_list.append(res)
               return Lists(new_list), None
          elif isinstance(other, Lists):
               other = list(other.elements)
               for i in self:
                    for j in other:
                          res, error = i.multiply(j)
                          if error: return None, error
                          new_list.append(res)
               return Lists(new_list), None
          else:
               return None, Value.illegal_operation(self, other)
          
     
          
     def divide(self, other):
          new_list = []
          
          if isinstance(other, Numbers):
                if other.value == 0:
                 return None, RunTimeError(other.pos_st, other.pos_end, "Thou dared divide by naught.", self.context)
                else:
                  for i in self:
                    res, error = i.divide(other)
                    if error: return None, error
                    new_list.append(res)
                return Lists(new_list), None
          elif isinstance(other, Lists):
               other = list(other.elements)
               for i in self:
                    for j in other:
                            print(j)
                            if other.value == 0:
                               return None, RunTimeError(other.pos_st, other.pos_end, "Thou dared divide by naught.", self.context)
                            else:
                             res, error = i.divide(j)
                             if error: return None, error
                            new_list.append(res)
               return Lists(new_list), None
          else:
               return None, Value.illegal_operation(self, other)

    
          
     def copy(self):
         copy = Lists(self.elements)
         copy.set_context(self.context).elements
         copy.set_pos(self.pos_st, self.pos_end)
         return copy
     
     def __repr__(self):
          return f'[{", ".join([str(x) for  x in self.elements])}]'
    
                    
class BuiltInFunctions(BaseFunctions):
     def __init__(self, name):
          super().__init__(name)

     def execute(self, arguements):
          res = RTResult()
          new_context = self.generate_context()

          method_name = f'execute_{self.name}'
          method = getattr(self, method_name, self.no_visit_method)

          res.register(self.populate_and_check(arguements, method.argues,new_context))
          if res.error: return res

          return_value = res.register(method(new_context))
          if res.error: return res
          return res.success(return_value)

     def no_visit_method(self, node, context):
          raise Exception(f'no execute_{self.name} has been defined')

     def execute_printeth(self, context):
          print(str(context.symbol_table.get("value")))
          return RTResult().success(Numbers(0))
     execute_printeth.argues = ["value"]

     def execute_recieve_sentence(self, context):
          text = input()
          return RTResult().success(Strings(text))
     
     execute_recieve_sentence.argues = []

     def execute_recieve_number(self, context):
          while True:
               num = input()
               try:
                 num = int(num)
                 break
               except ValueError:
                  print(f"'{num}' might not but beest a numb'r")
          return RTResult().success(Numbers(num))
     
     execute_recieve_number.argues = []

     def execute_beith_whole(self, context):
          isNum = isinstance(context.symbol_table.get("value"), Numbers)
          if isNum:
               return RTResult().success(Numbers.true)
          else:
               return RTResult().success(Numbers.false)
     execute_beith_whole.argues = ["value"]

     def execute_beith_tongue(self, context):
          isString = isinstance(context.symbol_table.get("value"), Strings)
          if isString:
               return RTResult().success(Numbers.true)
          else:
               return RTResult().success(Numbers.false)
     execute_beith_tongue.argues = ["value"]

     def execute_length(self, context):
          val = context.symbol_table.get("value")

          if not isinstance(val, Strings) and not isinstance(val, Lists):
               return RTResult().failure(RunTimeError(self.pos_st, self.pos_end, "Thy did input might not but beest a stringeth or listeth", context)) 
          else:
               if isinstance(val, Strings):
                    return RTResult().success(Numbers(len(val.value)))
               elif isinstance(val, Lists):
                    return RTResult().success(Numbers(len(val.elements)))
     execute_length.argues = ["value"]

     def execute_beith_listeth(self, context):
          isList = isinstance(context.symbol_table.get("value"), Lists)
          if isList:
               return RTResult().success(Numbers.true)
          else:
               return RTResult().success(Numbers.false)
     execute_beith_listeth.argues = ["value"]

     def execute_banish(self, context):
          list = context.symbol_table.get('list')
          index = context.symbol_table.get('index')
          res = RTResult()
          if not isinstance(index, Numbers):
               return res.failure(RunTimeError(self.pos_st, self.pos_end, "Index might not but beest a numb'r", context)) 
               
          if isinstance(list, Lists):  
                 try:
                      element = list.elements.pop(index.value)
                 except:
                  return res.failure(RunTimeError(self.pos_st, self.pos_end, "Couldst not removeth index from listeth since t is out of bounds", context)) 
                 return res.success(element)  
          else:
                return res.failure(RunTimeError(self.pos_st, self.pos_end, "Thee w're did expect to passeth a listeth", context))
     execute_banish.argues = ["list", "index"]
               
     def execute_includeth(self, context):
          list = context.symbol_table.get('list')
          value = context.symbol_table.get('value')
          res = RTResult()
          if isinstance(list, Lists):
               list.elements.append(value)
               return res.success(Numbers.true)               
          else:
               return res.failure(RunTimeError(self.pos_st, self.pos_end, "Thee w're did expect to passeth a listeth", context))
     execute_includeth.argues = ["list", "value"]
          
     
     def copy(self):
         copy = BuiltInFunctions(self.name)
         copy.set_pos(self.pos_st, self.pos_end)
         return copy
     
     def __repr__(self):
          return f'build in function <{self.name}>'
     

BuiltInFunctions.printeth           = BuiltInFunctions("printeth")
BuiltInFunctions.recieve_sentence   = BuiltInFunctions("recieve_sentence")
BuiltInFunctions.recieve_number     = BuiltInFunctions("recieve_number")
BuiltInFunctions.beith_whole        = BuiltInFunctions("beith_whole")
BuiltInFunctions.beith_tongue       = BuiltInFunctions("beith_tongue")
BuiltInFunctions.beith_listeth      = BuiltInFunctions("beith_listeth")
BuiltInFunctions.includeth          = BuiltInFunctions("includeth")
BuiltInFunctions.banish             = BuiltInFunctions("banish")
BuiltInFunctions.length             = BuiltInFunctions("length")