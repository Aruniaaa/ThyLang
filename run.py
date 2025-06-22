from Lexer import Lexer
from parser import Parser
from interpreter import Interpreter, Context, SymbolTable
from tokens import *
from values import Numbers, BuiltInFunctions



global_symbol_table = SymbolTable()
global_symbol_table.set("falsehood", Numbers.false)
global_symbol_table.set("sooth", Numbers.true)
global_symbol_table.set("printeth", BuiltInFunctions.printeth)
global_symbol_table.set("recieve_sentence", BuiltInFunctions.recieve_sentence)
global_symbol_table.set("recieve_number", BuiltInFunctions.recieve_number)
global_symbol_table.set("beith_whole", BuiltInFunctions.beith_whole)
global_symbol_table.set("beith_tongue", BuiltInFunctions.beith_tongue)
global_symbol_table.set("beith_listeth", BuiltInFunctions.beith_listeth)
global_symbol_table.set("includeth", BuiltInFunctions.includeth)
global_symbol_table.set("banish", BuiltInFunctions.banish)
global_symbol_table.set("length", BuiltInFunctions.length)




def run(file_name,text):
    lexer = Lexer(file_name, text)
    tokens, error = lexer.make_tokens()


    if error:
        return None, error

    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error: return None, ast.error
    inter = Interpreter()
    context = Context("<program>")
    context.symbol_table = global_symbol_table
    result = inter.visit(ast.node, context)

    return result.value, result.error
