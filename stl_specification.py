# from operations import *
from horizon_pastifier import *
from stl_specification_parser import StlAst
from ast_visitor import *
from abstract_specification import *


# semantics=Semantics.STANDARD, language=Language.PYTHON

def StlDiscreteTimeSpecification():
    spec = AbstractOfflineOnlineSpecification(StlAst(), StlDiscreteTimeOfflineInterpreter(),
                                                  StlDiscreteTimeOnlineInterpreter(),
                                                  pastifier=StlPastifier())
    

