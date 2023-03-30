from stl_parser_visitor import StlAstParserVisitor
from antlr.stlLexer import StlLexer
from antlr.stlParser import StlParser
from abstract_ast_parser import ast_factory
# from rtamt.antlr.parser.stl.error.parser_error_listener import STLParserErrorListener
#parser  error listener???

def StlAst():
    antrlLexerType = globals()['StlLexer']
    antrlParserType = globals()['StlParser']
    parserErrorListenerType = globals()['STLParserErrorListener']   #optional
    stlAst = ast_factory(StlAstParserVisitor)(antrlLexerType, antrlParserType, parserErrorListenerType)
    return stlAst