from stl_parser_visitor import StlAstParserVisitor
from antlr.stlLexer import stlLexer
from antlr.stlParser import stlParser
from abstract_ast_parser import ast_factory
# from rtamt.antlr.parser.stl.error.parser_error_listener import STLParserErrorListener
#parser  error listener???

def StlAst():
    antrlLexerType = globals()['stlLexer']
    antrlParserType = globals()['stlParser']
    # parserErrorListenerType = globals()['sTLParserErrorListener']   #optional
    # stlAst = ast_factory(StlAstParserVisitor)(antrlLexerType, antrlParserType, parserErrorListenerType)
    stlAst = ast_factory(StlAstParserVisitor)(antrlLexerType, antrlParserType)
    return stlAst
