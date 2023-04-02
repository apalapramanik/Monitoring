
from horizon_pastifier import *
from stl_specification_parser import StlAst
from ast_visitor import *
from abstract_specification import *
from enumerations import *


# semantics=Semantics.STANDARD, language=Language.PYTHON
def StlDiscreteTimeSpecification(semantics=Semantics.STANDARD, language=Language.PYTHON):
    if semantics == Semantics.STANDARD and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(StlAst(), StlDiscreteTimeOfflineInterpreter(),
                                                StlDiscreteTimeOnlineInterpreter(),
                                                pastifier=StlPastifier())
    
    else:
        raise Exception()
    return spec
