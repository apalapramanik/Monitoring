# Generated from stlParser.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,72,283,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,1,0,1,0,1,1,3,1,47,8,1,1,1,5,1,50,8,1,10,1,12,1,53,9,1,
        1,1,1,1,5,1,57,8,1,10,1,12,1,60,9,1,1,1,4,1,63,8,1,11,1,12,1,64,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,3,4,77,8,4,1,4,1,4,1,5,1,
        5,3,5,83,8,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,3,8,96,
        8,8,1,8,1,8,1,8,3,8,101,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,
        10,1,10,3,10,113,8,10,1,11,1,11,1,12,1,12,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,144,8,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,158,8,13,10,
        13,12,13,161,9,13,1,14,1,14,1,14,1,14,1,14,1,14,3,14,169,8,14,1,
        15,1,15,1,15,1,15,3,15,175,8,15,1,16,1,16,1,17,1,17,1,17,1,17,1,
        17,1,17,1,18,1,18,3,18,187,8,18,1,18,1,18,3,18,191,8,18,3,18,193,
        8,18,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        3,20,207,8,20,1,20,1,20,1,20,3,20,212,8,20,1,20,1,20,1,20,3,20,217,
        8,20,1,20,1,20,1,20,3,20,222,8,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,239,8,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,263,8,20,1,20,1,20,
        1,20,1,20,3,20,269,8,20,1,20,1,20,1,20,1,20,3,20,275,8,20,1,20,5,
        20,278,8,20,10,20,12,20,281,9,20,1,20,0,2,26,40,21,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,0,4,2,0,31,34,68,68,
        1,0,26,27,1,0,12,13,1,0,20,23,316,0,42,1,0,0,0,2,46,1,0,0,0,4,66,
        1,0,0,0,6,69,1,0,0,0,8,76,1,0,0,0,10,82,1,0,0,0,12,84,1,0,0,0,14,
        87,1,0,0,0,16,95,1,0,0,0,18,102,1,0,0,0,20,112,1,0,0,0,22,114,1,
        0,0,0,24,116,1,0,0,0,26,143,1,0,0,0,28,168,1,0,0,0,30,174,1,0,0,
        0,32,176,1,0,0,0,34,178,1,0,0,0,36,192,1,0,0,0,38,194,1,0,0,0,40,
        238,1,0,0,0,42,43,3,2,1,0,43,44,5,0,0,1,44,1,1,0,0,0,45,47,3,4,2,
        0,46,45,1,0,0,0,46,47,1,0,0,0,47,51,1,0,0,0,48,50,3,6,3,0,49,48,
        1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,58,1,0,0,0,
        53,51,1,0,0,0,54,57,3,10,5,0,55,57,3,12,6,0,56,54,1,0,0,0,56,55,
        1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,62,1,0,0,0,
        60,58,1,0,0,0,61,63,3,8,4,0,62,61,1,0,0,0,63,64,1,0,0,0,64,62,1,
        0,0,0,64,65,1,0,0,0,65,3,1,0,0,0,66,67,5,37,0,0,67,68,5,68,0,0,68,
        5,1,0,0,0,69,70,5,38,0,0,70,71,5,68,0,0,71,72,5,25,0,0,72,73,5,68,
        0,0,73,7,1,0,0,0,74,75,5,68,0,0,75,77,5,62,0,0,76,74,1,0,0,0,76,
        77,1,0,0,0,77,78,1,0,0,0,78,79,3,40,20,0,79,9,1,0,0,0,80,83,3,16,
        8,0,81,83,3,18,9,0,82,80,1,0,0,0,82,81,1,0,0,0,83,11,1,0,0,0,84,
        85,5,15,0,0,85,86,3,14,7,0,86,13,1,0,0,0,87,88,5,24,0,0,88,89,5,
        5,0,0,89,90,5,68,0,0,90,91,5,13,0,0,91,92,5,68,0,0,92,93,5,6,0,0,
        93,15,1,0,0,0,94,96,3,24,12,0,95,94,1,0,0,0,95,96,1,0,0,0,96,97,
        1,0,0,0,97,98,3,22,11,0,98,100,5,68,0,0,99,101,3,20,10,0,100,99,
        1,0,0,0,100,101,1,0,0,0,101,17,1,0,0,0,102,103,5,29,0,0,103,104,
        3,22,11,0,104,105,5,68,0,0,105,106,5,62,0,0,106,107,3,30,15,0,107,
        19,1,0,0,0,108,109,5,62,0,0,109,113,3,30,15,0,110,111,5,62,0,0,111,
        113,3,40,20,0,112,108,1,0,0,0,112,110,1,0,0,0,113,21,1,0,0,0,114,
        115,7,0,0,0,115,23,1,0,0,0,116,117,7,1,0,0,117,25,1,0,0,0,118,119,
        6,13,-1,0,119,144,5,68,0,0,120,144,3,30,15,0,121,122,5,16,0,0,122,
        123,5,5,0,0,123,124,3,26,13,0,124,125,5,6,0,0,125,144,1,0,0,0,126,
        127,5,17,0,0,127,128,5,5,0,0,128,129,3,26,13,0,129,130,5,6,0,0,130,
        144,1,0,0,0,131,132,5,18,0,0,132,133,5,5,0,0,133,134,3,26,13,0,134,
        135,5,6,0,0,135,144,1,0,0,0,136,137,5,19,0,0,137,138,5,5,0,0,138,
        139,3,26,13,0,139,140,5,13,0,0,140,141,3,26,13,0,141,142,5,6,0,0,
        142,144,1,0,0,0,143,118,1,0,0,0,143,120,1,0,0,0,143,121,1,0,0,0,
        143,126,1,0,0,0,143,131,1,0,0,0,143,136,1,0,0,0,144,159,1,0,0,0,
        145,146,10,8,0,0,146,147,5,2,0,0,147,158,3,26,13,9,148,149,10,7,
        0,0,149,150,5,1,0,0,150,158,3,26,13,8,151,152,10,6,0,0,152,153,5,
        3,0,0,153,158,3,26,13,7,154,155,10,5,0,0,155,156,5,4,0,0,156,158,
        3,26,13,6,157,145,1,0,0,0,157,148,1,0,0,0,157,151,1,0,0,0,157,154,
        1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,27,1,
        0,0,0,161,159,1,0,0,0,162,169,5,59,0,0,163,169,5,58,0,0,164,169,
        5,61,0,0,165,169,5,60,0,0,166,169,5,56,0,0,167,169,5,57,0,0,168,
        162,1,0,0,0,168,163,1,0,0,0,168,164,1,0,0,0,168,165,1,0,0,0,168,
        166,1,0,0,0,168,167,1,0,0,0,169,29,1,0,0,0,170,175,5,66,0,0,171,
        175,5,67,0,0,172,173,5,1,0,0,173,175,3,30,15,0,174,170,1,0,0,0,174,
        171,1,0,0,0,174,172,1,0,0,0,175,31,1,0,0,0,176,177,5,68,0,0,177,
        33,1,0,0,0,178,179,5,9,0,0,179,180,3,36,18,0,180,181,7,2,0,0,181,
        182,3,36,18,0,182,183,5,10,0,0,183,35,1,0,0,0,184,186,3,30,15,0,
        185,187,3,38,19,0,186,185,1,0,0,0,186,187,1,0,0,0,187,193,1,0,0,
        0,188,190,5,68,0,0,189,191,3,38,19,0,190,189,1,0,0,0,190,191,1,0,
        0,0,191,193,1,0,0,0,192,184,1,0,0,0,192,188,1,0,0,0,193,37,1,0,0,
        0,194,195,7,3,0,0,195,39,1,0,0,0,196,197,6,20,-1,0,197,239,3,26,
        13,0,198,199,5,5,0,0,199,200,3,40,20,0,200,201,5,6,0,0,201,239,1,
        0,0,0,202,203,5,39,0,0,203,239,3,40,20,17,204,206,5,47,0,0,205,207,
        3,34,17,0,206,205,1,0,0,0,206,207,1,0,0,0,207,208,1,0,0,0,208,239,
        3,40,20,11,209,211,5,48,0,0,210,212,3,34,17,0,211,210,1,0,0,0,211,
        212,1,0,0,0,212,213,1,0,0,0,213,239,3,40,20,10,214,216,5,51,0,0,
        215,217,3,34,17,0,216,215,1,0,0,0,216,217,1,0,0,0,217,218,1,0,0,
        0,218,239,3,40,20,7,219,221,5,52,0,0,220,222,3,34,17,0,221,220,1,
        0,0,0,221,222,1,0,0,0,222,223,1,0,0,0,223,239,3,40,20,6,224,225,
        5,45,0,0,225,226,5,5,0,0,226,227,3,40,20,0,227,228,5,6,0,0,228,239,
        1,0,0,0,229,230,5,46,0,0,230,231,5,5,0,0,231,232,3,40,20,0,232,233,
        5,6,0,0,233,239,1,0,0,0,234,235,5,55,0,0,235,239,3,40,20,2,236,237,
        5,54,0,0,237,239,3,40,20,1,238,196,1,0,0,0,238,198,1,0,0,0,238,202,
        1,0,0,0,238,204,1,0,0,0,238,209,1,0,0,0,238,214,1,0,0,0,238,219,
        1,0,0,0,238,224,1,0,0,0,238,229,1,0,0,0,238,234,1,0,0,0,238,236,
        1,0,0,0,239,279,1,0,0,0,240,241,10,19,0,0,241,242,3,28,14,0,242,
        243,3,40,20,20,243,278,1,0,0,0,244,245,10,16,0,0,245,246,5,40,0,
        0,246,278,3,40,20,17,247,248,10,15,0,0,248,249,5,41,0,0,249,278,
        3,40,20,16,250,251,10,14,0,0,251,252,5,43,0,0,252,278,3,40,20,15,
        253,254,10,13,0,0,254,255,5,42,0,0,255,278,3,40,20,14,256,257,10,
        12,0,0,257,258,5,44,0,0,258,278,3,40,20,13,259,260,10,9,0,0,260,
        262,5,49,0,0,261,263,3,34,17,0,262,261,1,0,0,0,262,263,1,0,0,0,263,
        264,1,0,0,0,264,278,3,40,20,10,265,266,10,8,0,0,266,268,5,50,0,0,
        267,269,3,34,17,0,268,267,1,0,0,0,268,269,1,0,0,0,269,270,1,0,0,
        0,270,278,3,40,20,9,271,272,10,5,0,0,272,274,5,53,0,0,273,275,3,
        34,17,0,274,273,1,0,0,0,274,275,1,0,0,0,275,276,1,0,0,0,276,278,
        3,40,20,6,277,240,1,0,0,0,277,244,1,0,0,0,277,247,1,0,0,0,277,250,
        1,0,0,0,277,253,1,0,0,0,277,256,1,0,0,0,277,259,1,0,0,0,277,265,
        1,0,0,0,277,271,1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,0,279,280,
        1,0,0,0,280,41,1,0,0,0,281,279,1,0,0,0,28,46,51,56,58,64,76,82,95,
        100,112,143,157,159,168,174,186,190,192,206,211,216,221,238,262,
        268,274,277,279
    ]

class stlParser ( Parser ):

    grammarFileName = "stlParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'+'", "'*'", "'/'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "';'", "':'", "','", "'.'", 
                     "'@'", "'abs'", "'sqrt'", "'exp'", "'pow'", "'s'", 
                     "'ms'", "'us'", "'ns'", "'topic'", "'import'", "'input'", 
                     "'output'", "'internal'", "'const'", "'real'", "'float'", 
                     "'long'", "'complex'", "'int'", "'bool'", "'assertion'", 
                     "'specification'", "'from'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'xor'", "'rise'", 
                     "'fall'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'=='", "'!=='", "'>='", "'<='", "'>'", 
                     "'<'", "'='" ]

    symbolicNames = [ "<INVALID>", "MINUS", "PLUS", "TIMES", "DIVIDE", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                      "SEMICOLON", "COLON", "COMMA", "DOT", "AT", "ABS", 
                      "SQRT", "EXP", "POW", "SEC", "MSEC", "USEC", "NSEC", 
                      "ROS_Topic", "Import", "Input", "Output", "Internal", 
                      "Constant", "DomainTypeReal", "DomainTypeFloat", "DomainTypeLong", 
                      "DomainTypeComplex", "DomainTypeInt", "DomainTypeBool", 
                      "Assertion", "Specification", "From", "NotOperator", 
                      "OrOperator", "AndOperator", "IffOperator", "ImpliesOperator", 
                      "XorOperator", "RiseOperator", "FallOperator", "AlwaysOperator", 
                      "EventuallyOperator", "UntilOperator", "UnlessOperator", 
                      "HistoricallyOperator", "OnceOperator", "SinceOperator", 
                      "NextOperator", "PreviousOperator", "EqualOperator", 
                      "NotEqualOperator", "GreaterOrEqualOperator", "LesserOrEqualOperator", 
                      "GreaterOperator", "LesserOperator", "EQUAL", "BooleanLiteral", 
                      "TRUE", "FALSE", "IntegerLiteral", "RealLiteral", 
                      "Identifier", "LINE_TERMINATOR", "WHITESPACE", "COMMENT", 
                      "LINE_COMMENT" ]

    RULE_specification_file = 0
    RULE_specification = 1
    RULE_spec = 2
    RULE_modimport = 3
    RULE_assertion = 4
    RULE_declaration = 5
    RULE_annotation = 6
    RULE_annotation_type = 7
    RULE_variableDeclaration = 8
    RULE_constantDeclaration = 9
    RULE_assignment = 10
    RULE_domainType = 11
    RULE_ioType = 12
    RULE_real_expression = 13
    RULE_comparisonOp = 14
    RULE_literal = 15
    RULE_identifier = 16
    RULE_interval = 17
    RULE_intervalTime = 18
    RULE_unit = 19
    RULE_expression = 20

    ruleNames =  [ "specification_file", "specification", "spec", "modimport", 
                   "assertion", "declaration", "annotation", "annotation_type", 
                   "variableDeclaration", "constantDeclaration", "assignment", 
                   "domainType", "ioType", "real_expression", "comparisonOp", 
                   "literal", "identifier", "interval", "intervalTime", 
                   "unit", "expression" ]

    EOF = Token.EOF
    MINUS=1
    PLUS=2
    TIMES=3
    DIVIDE=4
    LPAREN=5
    RPAREN=6
    LBRACE=7
    RBRACE=8
    LBRACK=9
    RBRACK=10
    SEMICOLON=11
    COLON=12
    COMMA=13
    DOT=14
    AT=15
    ABS=16
    SQRT=17
    EXP=18
    POW=19
    SEC=20
    MSEC=21
    USEC=22
    NSEC=23
    ROS_Topic=24
    Import=25
    Input=26
    Output=27
    Internal=28
    Constant=29
    DomainTypeReal=30
    DomainTypeFloat=31
    DomainTypeLong=32
    DomainTypeComplex=33
    DomainTypeInt=34
    DomainTypeBool=35
    Assertion=36
    Specification=37
    From=38
    NotOperator=39
    OrOperator=40
    AndOperator=41
    IffOperator=42
    ImpliesOperator=43
    XorOperator=44
    RiseOperator=45
    FallOperator=46
    AlwaysOperator=47
    EventuallyOperator=48
    UntilOperator=49
    UnlessOperator=50
    HistoricallyOperator=51
    OnceOperator=52
    SinceOperator=53
    NextOperator=54
    PreviousOperator=55
    EqualOperator=56
    NotEqualOperator=57
    GreaterOrEqualOperator=58
    LesserOrEqualOperator=59
    GreaterOperator=60
    LesserOperator=61
    EQUAL=62
    BooleanLiteral=63
    TRUE=64
    FALSE=65
    IntegerLiteral=66
    RealLiteral=67
    Identifier=68
    LINE_TERMINATOR=69
    WHITESPACE=70
    COMMENT=71
    LINE_COMMENT=72

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Specification_fileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def specification(self):
            return self.getTypedRuleContext(stlParser.SpecificationContext,0)


        def EOF(self):
            return self.getToken(stlParser.EOF, 0)

        def getRuleIndex(self):
            return stlParser.RULE_specification_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecification_file" ):
                listener.enterSpecification_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecification_file" ):
                listener.exitSpecification_file(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecification_file" ):
                return visitor.visitSpecification_file(self)
            else:
                return visitor.visitChildren(self)




    def specification_file(self):

        localctx = stlParser.Specification_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_specification_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.specification()
            self.state = 43
            self.match(stlParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def spec(self):
            return self.getTypedRuleContext(stlParser.SpecContext,0)


        def modimport(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.ModimportContext)
            else:
                return self.getTypedRuleContext(stlParser.ModimportContext,i)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(stlParser.DeclarationContext,i)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.AnnotationContext)
            else:
                return self.getTypedRuleContext(stlParser.AnnotationContext,i)


        def assertion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.AssertionContext)
            else:
                return self.getTypedRuleContext(stlParser.AssertionContext,i)


        def getRuleIndex(self):
            return stlParser.RULE_specification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecification" ):
                listener.enterSpecification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecification" ):
                listener.exitSpecification(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecification" ):
                return visitor.visitSpecification(self)
            else:
                return visitor.visitChildren(self)




    def specification(self):

        localctx = stlParser.SpecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_specification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 45
                self.spec()


            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 48
                self.modimport()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 56
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [26, 27, 29, 31, 32, 33, 34, 68]:
                        self.state = 54
                        self.declaration()
                        pass
                    elif token in [15]:
                        self.state = 55
                        self.annotation()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 61
                self.assertion()
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 61326910307631138) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 7) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stlParser.RULE_spec

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SpecificationIdContext(SpecContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.SpecContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Specification(self):
            return self.getToken(stlParser.Specification, 0)
        def Identifier(self):
            return self.getToken(stlParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecificationId" ):
                listener.enterSpecificationId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecificationId" ):
                listener.exitSpecificationId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecificationId" ):
                return visitor.visitSpecificationId(self)
            else:
                return visitor.visitChildren(self)



    def spec(self):

        localctx = stlParser.SpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_spec)
        try:
            localctx = stlParser.SpecificationIdContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(stlParser.Specification)
            self.state = 67
            self.match(stlParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModimportContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stlParser.RULE_modimport

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ModImportContext(ModimportContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ModimportContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def From(self):
            return self.getToken(stlParser.From, 0)
        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(stlParser.Identifier)
            else:
                return self.getToken(stlParser.Identifier, i)
        def Import(self):
            return self.getToken(stlParser.Import, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModImport" ):
                listener.enterModImport(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModImport" ):
                listener.exitModImport(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModImport" ):
                return visitor.visitModImport(self)
            else:
                return visitor.visitChildren(self)



    def modimport(self):

        localctx = stlParser.ModimportContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_modimport)
        try:
            localctx = stlParser.ModImportContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(stlParser.From)
            self.state = 70
            self.match(stlParser.Identifier)
            self.state = 71
            self.match(stlParser.Import)
            self.state = 72
            self.match(stlParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssertionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(stlParser.ExpressionContext,0)


        def Identifier(self):
            return self.getToken(stlParser.Identifier, 0)

        def EQUAL(self):
            return self.getToken(stlParser.EQUAL, 0)

        def getRuleIndex(self):
            return stlParser.RULE_assertion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssertion" ):
                listener.enterAssertion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssertion" ):
                listener.exitAssertion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssertion" ):
                return visitor.visitAssertion(self)
            else:
                return visitor.visitChildren(self)




    def assertion(self):

        localctx = stlParser.AssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 74
                self.match(stlParser.Identifier)
                self.state = 75
                self.match(stlParser.EQUAL)


            self.state = 78
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stlParser.RULE_declaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclVariableContext(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variableDeclaration(self):
            return self.getTypedRuleContext(stlParser.VariableDeclarationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclVariable" ):
                listener.enterDeclVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclVariable" ):
                listener.exitDeclVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclVariable" ):
                return visitor.visitDeclVariable(self)
            else:
                return visitor.visitChildren(self)


    class DeclConstantContext(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def constantDeclaration(self):
            return self.getTypedRuleContext(stlParser.ConstantDeclarationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclConstant" ):
                listener.enterDeclConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclConstant" ):
                listener.exitDeclConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclConstant" ):
                return visitor.visitDeclConstant(self)
            else:
                return visitor.visitChildren(self)



    def declaration(self):

        localctx = stlParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaration)
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27, 31, 32, 33, 34, 68]:
                localctx = stlParser.DeclVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.variableDeclaration()
                pass
            elif token in [29]:
                localctx = stlParser.DeclConstantContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.constantDeclaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(stlParser.AT, 0)

        def annotation_type(self):
            return self.getTypedRuleContext(stlParser.Annotation_typeContext,0)


        def getRuleIndex(self):
            return stlParser.RULE_annotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotation" ):
                listener.enterAnnotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotation" ):
                listener.exitAnnotation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnnotation" ):
                return visitor.visitAnnotation(self)
            else:
                return visitor.visitChildren(self)




    def annotation(self):

        localctx = stlParser.AnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_annotation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(stlParser.AT)
            self.state = 85
            self.annotation_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Annotation_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stlParser.RULE_annotation_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RosTopicContext(Annotation_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.Annotation_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ROS_Topic(self):
            return self.getToken(stlParser.ROS_Topic, 0)
        def LPAREN(self):
            return self.getToken(stlParser.LPAREN, 0)
        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(stlParser.Identifier)
            else:
                return self.getToken(stlParser.Identifier, i)
        def COMMA(self):
            return self.getToken(stlParser.COMMA, 0)
        def RPAREN(self):
            return self.getToken(stlParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRosTopic" ):
                listener.enterRosTopic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRosTopic" ):
                listener.exitRosTopic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRosTopic" ):
                return visitor.visitRosTopic(self)
            else:
                return visitor.visitChildren(self)



    def annotation_type(self):

        localctx = stlParser.Annotation_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_annotation_type)
        try:
            localctx = stlParser.RosTopicContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(stlParser.ROS_Topic)
            self.state = 88
            self.match(stlParser.LPAREN)
            self.state = 89
            self.match(stlParser.Identifier)
            self.state = 90
            self.match(stlParser.COMMA)
            self.state = 91
            self.match(stlParser.Identifier)
            self.state = 92
            self.match(stlParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def domainType(self):
            return self.getTypedRuleContext(stlParser.DomainTypeContext,0)


        def Identifier(self):
            return self.getToken(stlParser.Identifier, 0)

        def ioType(self):
            return self.getTypedRuleContext(stlParser.IoTypeContext,0)


        def assignment(self):
            return self.getTypedRuleContext(stlParser.AssignmentContext,0)


        def getRuleIndex(self):
            return stlParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = stlParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26 or _la==27:
                self.state = 94
                self.ioType()


            self.state = 97
            self.domainType()
            self.state = 98
            self.match(stlParser.Identifier)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 99
                self.assignment()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Constant(self):
            return self.getToken(stlParser.Constant, 0)

        def domainType(self):
            return self.getTypedRuleContext(stlParser.DomainTypeContext,0)


        def Identifier(self):
            return self.getToken(stlParser.Identifier, 0)

        def EQUAL(self):
            return self.getToken(stlParser.EQUAL, 0)

        def literal(self):
            return self.getTypedRuleContext(stlParser.LiteralContext,0)


        def getRuleIndex(self):
            return stlParser.RULE_constantDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantDeclaration" ):
                listener.enterConstantDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantDeclaration" ):
                listener.exitConstantDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantDeclaration" ):
                return visitor.visitConstantDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def constantDeclaration(self):

        localctx = stlParser.ConstantDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_constantDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(stlParser.Constant)
            self.state = 103
            self.domainType()
            self.state = 104
            self.match(stlParser.Identifier)
            self.state = 105
            self.match(stlParser.EQUAL)
            self.state = 106
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stlParser.RULE_assignment

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AsgnExprContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EQUAL(self):
            return self.getToken(stlParser.EQUAL, 0)
        def expression(self):
            return self.getTypedRuleContext(stlParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsgnExpr" ):
                listener.enterAsgnExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsgnExpr" ):
                listener.exitAsgnExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsgnExpr" ):
                return visitor.visitAsgnExpr(self)
            else:
                return visitor.visitChildren(self)


    class AsgnLiteralContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EQUAL(self):
            return self.getToken(stlParser.EQUAL, 0)
        def literal(self):
            return self.getTypedRuleContext(stlParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsgnLiteral" ):
                listener.enterAsgnLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsgnLiteral" ):
                listener.exitAsgnLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsgnLiteral" ):
                return visitor.visitAsgnLiteral(self)
            else:
                return visitor.visitChildren(self)



    def assignment(self):

        localctx = stlParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignment)
        try:
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = stlParser.AsgnLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.match(stlParser.EQUAL)
                self.state = 109
                self.literal()
                pass

            elif la_ == 2:
                localctx = stlParser.AsgnExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.match(stlParser.EQUAL)
                self.state = 111
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DomainTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DomainTypeFloat(self):
            return self.getToken(stlParser.DomainTypeFloat, 0)

        def DomainTypeInt(self):
            return self.getToken(stlParser.DomainTypeInt, 0)

        def DomainTypeLong(self):
            return self.getToken(stlParser.DomainTypeLong, 0)

        def DomainTypeComplex(self):
            return self.getToken(stlParser.DomainTypeComplex, 0)

        def Identifier(self):
            return self.getToken(stlParser.Identifier, 0)

        def getRuleIndex(self):
            return stlParser.RULE_domainType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDomainType" ):
                listener.enterDomainType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDomainType" ):
                listener.exitDomainType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDomainType" ):
                return visitor.visitDomainType(self)
            else:
                return visitor.visitChildren(self)




    def domainType(self):

        localctx = stlParser.DomainTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_domainType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            _la = self._input.LA(1)
            if not(((((_la - 31)) & ~0x3f) == 0 and ((1 << (_la - 31)) & 137438953487) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IoTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Input(self):
            return self.getToken(stlParser.Input, 0)

        def Output(self):
            return self.getToken(stlParser.Output, 0)

        def getRuleIndex(self):
            return stlParser.RULE_ioType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIoType" ):
                listener.enterIoType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIoType" ):
                listener.exitIoType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIoType" ):
                return visitor.visitIoType(self)
            else:
                return visitor.visitChildren(self)




    def ioType(self):

        localctx = stlParser.IoTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ioType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Real_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stlParser.RULE_real_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprSubtractionContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def real_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.Real_expressionContext)
            else:
                return self.getTypedRuleContext(stlParser.Real_expressionContext,i)

        def MINUS(self):
            return self.getToken(stlParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprSubtraction" ):
                listener.enterExprSubtraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprSubtraction" ):
                listener.exitExprSubtraction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprSubtraction" ):
                return visitor.visitExprSubtraction(self)
            else:
                return visitor.visitChildren(self)


    class ExprPowContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def POW(self):
            return self.getToken(stlParser.POW, 0)
        def LPAREN(self):
            return self.getToken(stlParser.LPAREN, 0)
        def real_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.Real_expressionContext)
            else:
                return self.getTypedRuleContext(stlParser.Real_expressionContext,i)

        def COMMA(self):
            return self.getToken(stlParser.COMMA, 0)
        def RPAREN(self):
            return self.getToken(stlParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprPow" ):
                listener.enterExprPow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprPow" ):
                listener.exitExprPow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPow" ):
                return visitor.visitExprPow(self)
            else:
                return visitor.visitChildren(self)


    class ExprDivisionContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def real_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.Real_expressionContext)
            else:
                return self.getTypedRuleContext(stlParser.Real_expressionContext,i)

        def DIVIDE(self):
            return self.getToken(stlParser.DIVIDE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprDivision" ):
                listener.enterExprDivision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprDivision" ):
                listener.exitExprDivision(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprDivision" ):
                return visitor.visitExprDivision(self)
            else:
                return visitor.visitChildren(self)


    class ExprMultiplicationContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def real_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.Real_expressionContext)
            else:
                return self.getTypedRuleContext(stlParser.Real_expressionContext,i)

        def TIMES(self):
            return self.getToken(stlParser.TIMES, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprMultiplication" ):
                listener.enterExprMultiplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprMultiplication" ):
                listener.exitExprMultiplication(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprMultiplication" ):
                return visitor.visitExprMultiplication(self)
            else:
                return visitor.visitChildren(self)


    class ExprLiteralContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(stlParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLiteral" ):
                listener.enterExprLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLiteral" ):
                listener.exitExprLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLiteral" ):
                return visitor.visitExprLiteral(self)
            else:
                return visitor.visitChildren(self)


    class ExprExpContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EXP(self):
            return self.getToken(stlParser.EXP, 0)
        def LPAREN(self):
            return self.getToken(stlParser.LPAREN, 0)
        def real_expression(self):
            return self.getTypedRuleContext(stlParser.Real_expressionContext,0)

        def RPAREN(self):
            return self.getToken(stlParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprExp" ):
                listener.enterExprExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprExp" ):
                listener.exitExprExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprExp" ):
                return visitor.visitExprExp(self)
            else:
                return visitor.visitChildren(self)


    class ExprSqrtContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SQRT(self):
            return self.getToken(stlParser.SQRT, 0)
        def LPAREN(self):
            return self.getToken(stlParser.LPAREN, 0)
        def real_expression(self):
            return self.getTypedRuleContext(stlParser.Real_expressionContext,0)

        def RPAREN(self):
            return self.getToken(stlParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprSqrt" ):
                listener.enterExprSqrt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprSqrt" ):
                listener.exitExprSqrt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprSqrt" ):
                return visitor.visitExprSqrt(self)
            else:
                return visitor.visitChildren(self)


    class ExprIdContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(stlParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprId" ):
                listener.enterExprId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprId" ):
                listener.exitExprId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprId" ):
                return visitor.visitExprId(self)
            else:
                return visitor.visitChildren(self)


    class ExprAbsContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ABS(self):
            return self.getToken(stlParser.ABS, 0)
        def LPAREN(self):
            return self.getToken(stlParser.LPAREN, 0)
        def real_expression(self):
            return self.getTypedRuleContext(stlParser.Real_expressionContext,0)

        def RPAREN(self):
            return self.getToken(stlParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAbs" ):
                listener.enterExprAbs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAbs" ):
                listener.exitExprAbs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAbs" ):
                return visitor.visitExprAbs(self)
            else:
                return visitor.visitChildren(self)


    class ExprAdditionContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def real_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.Real_expressionContext)
            else:
                return self.getTypedRuleContext(stlParser.Real_expressionContext,i)

        def PLUS(self):
            return self.getToken(stlParser.PLUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAddition" ):
                listener.enterExprAddition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAddition" ):
                listener.exitExprAddition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAddition" ):
                return visitor.visitExprAddition(self)
            else:
                return visitor.visitChildren(self)



    def real_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = stlParser.Real_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_real_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [68]:
                localctx = stlParser.ExprIdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 119
                self.match(stlParser.Identifier)
                pass
            elif token in [1, 66, 67]:
                localctx = stlParser.ExprLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 120
                self.literal()
                pass
            elif token in [16]:
                localctx = stlParser.ExprAbsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 121
                self.match(stlParser.ABS)
                self.state = 122
                self.match(stlParser.LPAREN)
                self.state = 123
                self.real_expression(0)
                self.state = 124
                self.match(stlParser.RPAREN)
                pass
            elif token in [17]:
                localctx = stlParser.ExprSqrtContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 126
                self.match(stlParser.SQRT)
                self.state = 127
                self.match(stlParser.LPAREN)
                self.state = 128
                self.real_expression(0)
                self.state = 129
                self.match(stlParser.RPAREN)
                pass
            elif token in [18]:
                localctx = stlParser.ExprExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 131
                self.match(stlParser.EXP)
                self.state = 132
                self.match(stlParser.LPAREN)
                self.state = 133
                self.real_expression(0)
                self.state = 134
                self.match(stlParser.RPAREN)
                pass
            elif token in [19]:
                localctx = stlParser.ExprPowContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 136
                self.match(stlParser.POW)
                self.state = 137
                self.match(stlParser.LPAREN)
                self.state = 138
                self.real_expression(0)
                self.state = 139
                self.match(stlParser.COMMA)
                self.state = 140
                self.real_expression(0)
                self.state = 141
                self.match(stlParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 159
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 157
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = stlParser.ExprAdditionContext(self, stlParser.Real_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_real_expression)
                        self.state = 145
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 146
                        self.match(stlParser.PLUS)
                        self.state = 147
                        self.real_expression(9)
                        pass

                    elif la_ == 2:
                        localctx = stlParser.ExprSubtractionContext(self, stlParser.Real_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_real_expression)
                        self.state = 148
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 149
                        self.match(stlParser.MINUS)
                        self.state = 150
                        self.real_expression(8)
                        pass

                    elif la_ == 3:
                        localctx = stlParser.ExprMultiplicationContext(self, stlParser.Real_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_real_expression)
                        self.state = 151
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 152
                        self.match(stlParser.TIMES)
                        self.state = 153
                        self.real_expression(7)
                        pass

                    elif la_ == 4:
                        localctx = stlParser.ExprDivisionContext(self, stlParser.Real_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_real_expression)
                        self.state = 154
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 155
                        self.match(stlParser.DIVIDE)
                        self.state = 156
                        self.real_expression(6)
                        pass

             
                self.state = 161
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparisonOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stlParser.RULE_comparisonOp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class GeqContext(ComparisonOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ComparisonOpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GreaterOrEqualOperator(self):
            return self.getToken(stlParser.GreaterOrEqualOperator, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeq" ):
                listener.enterGeq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeq" ):
                listener.exitGeq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeq" ):
                return visitor.visitGeq(self)
            else:
                return visitor.visitChildren(self)


    class LeqContext(ComparisonOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ComparisonOpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LesserOrEqualOperator(self):
            return self.getToken(stlParser.LesserOrEqualOperator, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeq" ):
                listener.enterLeq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeq" ):
                listener.exitLeq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeq" ):
                return visitor.visitLeq(self)
            else:
                return visitor.visitChildren(self)


    class GreaterContext(ComparisonOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ComparisonOpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GreaterOperator(self):
            return self.getToken(stlParser.GreaterOperator, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreater" ):
                listener.enterGreater(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreater" ):
                listener.exitGreater(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreater" ):
                return visitor.visitGreater(self)
            else:
                return visitor.visitChildren(self)


    class NeqContext(ComparisonOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ComparisonOpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NotEqualOperator(self):
            return self.getToken(stlParser.NotEqualOperator, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNeq" ):
                listener.enterNeq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNeq" ):
                listener.exitNeq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeq" ):
                return visitor.visitNeq(self)
            else:
                return visitor.visitChildren(self)


    class EqContext(ComparisonOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ComparisonOpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EqualOperator(self):
            return self.getToken(stlParser.EqualOperator, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEq" ):
                listener.enterEq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEq" ):
                listener.exitEq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEq" ):
                return visitor.visitEq(self)
            else:
                return visitor.visitChildren(self)


    class LessContext(ComparisonOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ComparisonOpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LesserOperator(self):
            return self.getToken(stlParser.LesserOperator, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLess" ):
                listener.enterLess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLess" ):
                listener.exitLess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLess" ):
                return visitor.visitLess(self)
            else:
                return visitor.visitChildren(self)



    def comparisonOp(self):

        localctx = stlParser.ComparisonOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_comparisonOp)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                localctx = stlParser.LeqContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(stlParser.LesserOrEqualOperator)
                pass
            elif token in [58]:
                localctx = stlParser.GeqContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(stlParser.GreaterOrEqualOperator)
                pass
            elif token in [61]:
                localctx = stlParser.LessContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.match(stlParser.LesserOperator)
                pass
            elif token in [60]:
                localctx = stlParser.GreaterContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 165
                self.match(stlParser.GreaterOperator)
                pass
            elif token in [56]:
                localctx = stlParser.EqContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 166
                self.match(stlParser.EqualOperator)
                pass
            elif token in [57]:
                localctx = stlParser.NeqContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 167
                self.match(stlParser.NotEqualOperator)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(stlParser.IntegerLiteral, 0)

        def RealLiteral(self):
            return self.getToken(stlParser.RealLiteral, 0)

        def MINUS(self):
            return self.getToken(stlParser.MINUS, 0)

        def literal(self):
            return self.getTypedRuleContext(stlParser.LiteralContext,0)


        def getRuleIndex(self):
            return stlParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = stlParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_literal)
        try:
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.match(stlParser.IntegerLiteral)
                pass
            elif token in [67]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.match(stlParser.RealLiteral)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 172
                self.match(stlParser.MINUS)
                self.state = 173
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stlParser.RULE_identifier

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IdContext(IdentifierContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.IdentifierContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(stlParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)



    def identifier(self):

        localctx = stlParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_identifier)
        try:
            localctx = stlParser.IdContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(stlParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntervalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(stlParser.LBRACK, 0)

        def intervalTime(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.IntervalTimeContext)
            else:
                return self.getTypedRuleContext(stlParser.IntervalTimeContext,i)


        def RBRACK(self):
            return self.getToken(stlParser.RBRACK, 0)

        def COLON(self):
            return self.getToken(stlParser.COLON, 0)

        def COMMA(self):
            return self.getToken(stlParser.COMMA, 0)

        def getRuleIndex(self):
            return stlParser.RULE_interval

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterval" ):
                listener.enterInterval(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterval" ):
                listener.exitInterval(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterval" ):
                return visitor.visitInterval(self)
            else:
                return visitor.visitChildren(self)




    def interval(self):

        localctx = stlParser.IntervalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_interval)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(stlParser.LBRACK)
            self.state = 179
            self.intervalTime()
            self.state = 180
            _la = self._input.LA(1)
            if not(_la==12 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 181
            self.intervalTime()
            self.state = 182
            self.match(stlParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntervalTimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stlParser.RULE_intervalTime

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntervalTimeLiteralContext(IntervalTimeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.IntervalTimeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(stlParser.LiteralContext,0)

        def unit(self):
            return self.getTypedRuleContext(stlParser.UnitContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntervalTimeLiteral" ):
                listener.enterIntervalTimeLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntervalTimeLiteral" ):
                listener.exitIntervalTimeLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntervalTimeLiteral" ):
                return visitor.visitIntervalTimeLiteral(self)
            else:
                return visitor.visitChildren(self)


    class ConstantTimeLiteralContext(IntervalTimeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.IntervalTimeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(stlParser.Identifier, 0)
        def unit(self):
            return self.getTypedRuleContext(stlParser.UnitContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantTimeLiteral" ):
                listener.enterConstantTimeLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantTimeLiteral" ):
                listener.exitConstantTimeLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantTimeLiteral" ):
                return visitor.visitConstantTimeLiteral(self)
            else:
                return visitor.visitChildren(self)



    def intervalTime(self):

        localctx = stlParser.IntervalTimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_intervalTime)
        self._la = 0 # Token type
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 66, 67]:
                localctx = stlParser.IntervalTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.literal()
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0):
                    self.state = 185
                    self.unit()


                pass
            elif token in [68]:
                localctx = stlParser.ConstantTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.match(stlParser.Identifier)
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0):
                    self.state = 189
                    self.unit()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEC(self):
            return self.getToken(stlParser.SEC, 0)

        def MSEC(self):
            return self.getToken(stlParser.MSEC, 0)

        def USEC(self):
            return self.getToken(stlParser.USEC, 0)

        def NSEC(self):
            return self.getToken(stlParser.NSEC, 0)

        def getRuleIndex(self):
            return stlParser.RULE_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnit" ):
                listener.enterUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnit" ):
                listener.exitUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnit" ):
                return visitor.visitUnit(self)
            else:
                return visitor.visitChildren(self)




    def unit(self):

        localctx = stlParser.UnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_unit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stlParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprSinceContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(stlParser.ExpressionContext,i)

        def SinceOperator(self):
            return self.getToken(stlParser.SinceOperator, 0)
        def interval(self):
            return self.getTypedRuleContext(stlParser.IntervalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprSince" ):
                listener.enterExprSince(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprSince" ):
                listener.exitExprSince(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprSince" ):
                return visitor.visitExprSince(self)
            else:
                return visitor.visitChildren(self)


    class ExprParenContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(stlParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(stlParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(stlParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprParen" ):
                listener.enterExprParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprParen" ):
                listener.exitExprParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprParen" ):
                return visitor.visitExprParen(self)
            else:
                return visitor.visitChildren(self)


    class ExprIffContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(stlParser.ExpressionContext,i)

        def IffOperator(self):
            return self.getToken(stlParser.IffOperator, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprIff" ):
                listener.enterExprIff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprIff" ):
                listener.exitExprIff(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprIff" ):
                return visitor.visitExprIff(self)
            else:
                return visitor.visitChildren(self)


    class ExpreOnceContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OnceOperator(self):
            return self.getToken(stlParser.OnceOperator, 0)
        def expression(self):
            return self.getTypedRuleContext(stlParser.ExpressionContext,0)

        def interval(self):
            return self.getTypedRuleContext(stlParser.IntervalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpreOnce" ):
                listener.enterExpreOnce(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpreOnce" ):
                listener.exitExpreOnce(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpreOnce" ):
                return visitor.visitExpreOnce(self)
            else:
                return visitor.visitChildren(self)


    class ExprEvContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EventuallyOperator(self):
            return self.getToken(stlParser.EventuallyOperator, 0)
        def expression(self):
            return self.getTypedRuleContext(stlParser.ExpressionContext,0)

        def interval(self):
            return self.getTypedRuleContext(stlParser.IntervalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprEv" ):
                listener.enterExprEv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprEv" ):
                listener.exitExprEv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprEv" ):
                return visitor.visitExprEv(self)
            else:
                return visitor.visitChildren(self)


    class ExprImpliesContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(stlParser.ExpressionContext,i)

        def ImpliesOperator(self):
            return self.getToken(stlParser.ImpliesOperator, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprImplies" ):
                listener.enterExprImplies(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprImplies" ):
                listener.exitExprImplies(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprImplies" ):
                return visitor.visitExprImplies(self)
            else:
                return visitor.visitChildren(self)


    class ExprUntilContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(stlParser.ExpressionContext,i)

        def UntilOperator(self):
            return self.getToken(stlParser.UntilOperator, 0)
        def interval(self):
            return self.getTypedRuleContext(stlParser.IntervalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprUntil" ):
                listener.enterExprUntil(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprUntil" ):
                listener.exitExprUntil(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprUntil" ):
                return visitor.visitExprUntil(self)
            else:
                return visitor.visitChildren(self)


    class ExprNotContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NotOperator(self):
            return self.getToken(stlParser.NotOperator, 0)
        def expression(self):
            return self.getTypedRuleContext(stlParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprNot" ):
                listener.enterExprNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprNot" ):
                listener.exitExprNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprNot" ):
                return visitor.visitExprNot(self)
            else:
                return visitor.visitChildren(self)


    class ExprNextContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NextOperator(self):
            return self.getToken(stlParser.NextOperator, 0)
        def expression(self):
            return self.getTypedRuleContext(stlParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprNext" ):
                listener.enterExprNext(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprNext" ):
                listener.exitExprNext(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprNext" ):
                return visitor.visitExprNext(self)
            else:
                return visitor.visitChildren(self)


    class ExprAndContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(stlParser.ExpressionContext,i)

        def AndOperator(self):
            return self.getToken(stlParser.AndOperator, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAnd" ):
                listener.enterExprAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAnd" ):
                listener.exitExprAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAnd" ):
                return visitor.visitExprAnd(self)
            else:
                return visitor.visitChildren(self)


    class ExprUnlessContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(stlParser.ExpressionContext,i)

        def UnlessOperator(self):
            return self.getToken(stlParser.UnlessOperator, 0)
        def interval(self):
            return self.getTypedRuleContext(stlParser.IntervalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprUnless" ):
                listener.enterExprUnless(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprUnless" ):
                listener.exitExprUnless(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprUnless" ):
                return visitor.visitExprUnless(self)
            else:
                return visitor.visitChildren(self)


    class ExprPreviousContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PreviousOperator(self):
            return self.getToken(stlParser.PreviousOperator, 0)
        def expression(self):
            return self.getTypedRuleContext(stlParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprPrevious" ):
                listener.enterExprPrevious(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprPrevious" ):
                listener.exitExprPrevious(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPrevious" ):
                return visitor.visitExprPrevious(self)
            else:
                return visitor.visitChildren(self)


    class ExprHistContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def HistoricallyOperator(self):
            return self.getToken(stlParser.HistoricallyOperator, 0)
        def expression(self):
            return self.getTypedRuleContext(stlParser.ExpressionContext,0)

        def interval(self):
            return self.getTypedRuleContext(stlParser.IntervalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprHist" ):
                listener.enterExprHist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprHist" ):
                listener.exitExprHist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprHist" ):
                return visitor.visitExprHist(self)
            else:
                return visitor.visitChildren(self)


    class ExprFallContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FallOperator(self):
            return self.getToken(stlParser.FallOperator, 0)
        def LPAREN(self):
            return self.getToken(stlParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(stlParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(stlParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprFall" ):
                listener.enterExprFall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprFall" ):
                listener.exitExprFall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprFall" ):
                return visitor.visitExprFall(self)
            else:
                return visitor.visitChildren(self)


    class ExprPredicateContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(stlParser.ExpressionContext,i)

        def comparisonOp(self):
            return self.getTypedRuleContext(stlParser.ComparisonOpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprPredicate" ):
                listener.enterExprPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprPredicate" ):
                listener.exitExprPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPredicate" ):
                return visitor.visitExprPredicate(self)
            else:
                return visitor.visitChildren(self)


    class ExprXorContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(stlParser.ExpressionContext,i)

        def XorOperator(self):
            return self.getToken(stlParser.XorOperator, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprXor" ):
                listener.enterExprXor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprXor" ):
                listener.exitExprXor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprXor" ):
                return visitor.visitExprXor(self)
            else:
                return visitor.visitChildren(self)


    class ExprRiseContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RiseOperator(self):
            return self.getToken(stlParser.RiseOperator, 0)
        def LPAREN(self):
            return self.getToken(stlParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(stlParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(stlParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprRise" ):
                listener.enterExprRise(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprRise" ):
                listener.exitExprRise(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprRise" ):
                return visitor.visitExprRise(self)
            else:
                return visitor.visitChildren(self)


    class ExprOrContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(stlParser.ExpressionContext,i)

        def OrOperator(self):
            return self.getToken(stlParser.OrOperator, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprOr" ):
                listener.enterExprOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprOr" ):
                listener.exitExprOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprOr" ):
                return visitor.visitExprOr(self)
            else:
                return visitor.visitChildren(self)


    class ExprAlwaysContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def AlwaysOperator(self):
            return self.getToken(stlParser.AlwaysOperator, 0)
        def expression(self):
            return self.getTypedRuleContext(stlParser.ExpressionContext,0)

        def interval(self):
            return self.getTypedRuleContext(stlParser.IntervalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAlways" ):
                listener.enterExprAlways(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAlways" ):
                listener.exitExprAlways(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAlways" ):
                return visitor.visitExprAlways(self)
            else:
                return visitor.visitChildren(self)


    class ExprRealContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def real_expression(self):
            return self.getTypedRuleContext(stlParser.Real_expressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprReal" ):
                listener.enterExprReal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprReal" ):
                listener.exitExprReal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprReal" ):
                return visitor.visitExprReal(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = stlParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 16, 17, 18, 19, 66, 67, 68]:
                localctx = stlParser.ExprRealContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 197
                self.real_expression(0)
                pass
            elif token in [5]:
                localctx = stlParser.ExprParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 198
                self.match(stlParser.LPAREN)
                self.state = 199
                self.expression(0)
                self.state = 200
                self.match(stlParser.RPAREN)
                pass
            elif token in [39]:
                localctx = stlParser.ExprNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 202
                self.match(stlParser.NotOperator)
                self.state = 203
                self.expression(17)
                pass
            elif token in [47]:
                localctx = stlParser.ExprAlwaysContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 204
                self.match(stlParser.AlwaysOperator)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 205
                    self.interval()


                self.state = 208
                self.expression(11)
                pass
            elif token in [48]:
                localctx = stlParser.ExprEvContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 209
                self.match(stlParser.EventuallyOperator)
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 210
                    self.interval()


                self.state = 213
                self.expression(10)
                pass
            elif token in [51]:
                localctx = stlParser.ExprHistContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 214
                self.match(stlParser.HistoricallyOperator)
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 215
                    self.interval()


                self.state = 218
                self.expression(7)
                pass
            elif token in [52]:
                localctx = stlParser.ExpreOnceContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 219
                self.match(stlParser.OnceOperator)
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 220
                    self.interval()


                self.state = 223
                self.expression(6)
                pass
            elif token in [45]:
                localctx = stlParser.ExprRiseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 224
                self.match(stlParser.RiseOperator)
                self.state = 225
                self.match(stlParser.LPAREN)
                self.state = 226
                self.expression(0)
                self.state = 227
                self.match(stlParser.RPAREN)
                pass
            elif token in [46]:
                localctx = stlParser.ExprFallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 229
                self.match(stlParser.FallOperator)
                self.state = 230
                self.match(stlParser.LPAREN)
                self.state = 231
                self.expression(0)
                self.state = 232
                self.match(stlParser.RPAREN)
                pass
            elif token in [55]:
                localctx = stlParser.ExprPreviousContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 234
                self.match(stlParser.PreviousOperator)
                self.state = 235
                self.expression(2)
                pass
            elif token in [54]:
                localctx = stlParser.ExprNextContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 236
                self.match(stlParser.NextOperator)
                self.state = 237
                self.expression(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 279
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 277
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = stlParser.ExprPredicateContext(self, stlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 240
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 241
                        self.comparisonOp()
                        self.state = 242
                        self.expression(20)
                        pass

                    elif la_ == 2:
                        localctx = stlParser.ExprOrContext(self, stlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 244
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 245
                        self.match(stlParser.OrOperator)
                        self.state = 246
                        self.expression(17)
                        pass

                    elif la_ == 3:
                        localctx = stlParser.ExprAndContext(self, stlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 247
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 248
                        self.match(stlParser.AndOperator)
                        self.state = 249
                        self.expression(16)
                        pass

                    elif la_ == 4:
                        localctx = stlParser.ExprImpliesContext(self, stlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 250
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 251
                        self.match(stlParser.ImpliesOperator)
                        self.state = 252
                        self.expression(15)
                        pass

                    elif la_ == 5:
                        localctx = stlParser.ExprIffContext(self, stlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 253
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 254
                        self.match(stlParser.IffOperator)
                        self.state = 255
                        self.expression(14)
                        pass

                    elif la_ == 6:
                        localctx = stlParser.ExprXorContext(self, stlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 256
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 257
                        self.match(stlParser.XorOperator)
                        self.state = 258
                        self.expression(13)
                        pass

                    elif la_ == 7:
                        localctx = stlParser.ExprUntilContext(self, stlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 259
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 260
                        self.match(stlParser.UntilOperator)
                        self.state = 262
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==9:
                            self.state = 261
                            self.interval()


                        self.state = 264
                        self.expression(10)
                        pass

                    elif la_ == 8:
                        localctx = stlParser.ExprUnlessContext(self, stlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 265
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 266
                        self.match(stlParser.UnlessOperator)
                        self.state = 268
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==9:
                            self.state = 267
                            self.interval()


                        self.state = 270
                        self.expression(9)
                        pass

                    elif la_ == 9:
                        localctx = stlParser.ExprSinceContext(self, stlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 271
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 272
                        self.match(stlParser.SinceOperator)
                        self.state = 274
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==9:
                            self.state = 273
                            self.interval()


                        self.state = 276
                        self.expression(6)
                        pass

             
                self.state = 281
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.real_expression_sempred
        self._predicates[20] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def real_expression_sempred(self, localctx:Real_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 5)
         




