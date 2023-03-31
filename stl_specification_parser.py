from stl_parser_visitor import StlAstParserVisitor
from antlr.stlLexer import stlLexer
from antlr.stlParser import stlParser
from abstract_ast_parser import ast_factory

from antlr4.error.ErrorListener import ErrorListener
from exception import MonException

class STLParserErrorListener( ErrorListener ):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise MonException (str(line) + ":" + str(column) + ": Syntax ERROR, " + str(msg))

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise MonException("Ambiguity ERROR, " + str(configs))

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise MonException("Attempting full context ERROR, " + str(configs))

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise MonException("Context ERROR, " + str(configs))

def StlAst():
    antrlLexerType = globals()['stlLexer']
    antrlParserType = globals()['stlParser']
    parserErrorListenerType = globals()['STLParserErrorListener']   #optional
    stlAst = ast_factory(StlAstParserVisitor)(antrlLexerType, antrlParserType, parserErrorListenerType)
    stlAst = ast_factory(StlAstParserVisitor)(antrlLexerType, antrlParserType)
    return stlAst
