from operations import *
from horizon_pastifier import *
from stl_specification_parser import StlAst


def StlDiscreteTimeSpecification(semantics=Semantics.STANDARD, language=Language.PYTHON):
    spec = AbstractOfflineOnlineSpecification(StlAst(), StlDiscreteTimeOfflineInterpreter(),
                                                  StlDiscreteTimeOnlineInterpreter(),
                                                  pastifier=StlPastifier())
    
def StlDiscreteTimeOfflineInterpreter():
    stlDiscreteTimeOfflineInterpreter = discrete_time_offline_interpreter_factory(StlDiscreteTimeOfflineAstVisitor)()
    return stlDiscreteTimeOfflineInterpreter

def StlDiscreteTimeOfflineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), StlDiscreteTimeOfflineInterpreter())
    return spec

def StlDiscreteTimeOnlineSpecification():
    spec = AbstractOnlineSpecification(StlAst(), StlDiscreteTimeOnlineInterpreter(),
                                       pastifier=StlPastifier())
    return spec

