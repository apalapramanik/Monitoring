import sys

import antlr4
from antlr import *
from abstract_ast_parser import *
from abstract_specification import *
from ast_visitor import *
from discrete_operators import *
from enumerations import *
from exception import *
from horizon_pastifier import *
from interpreters import *
from intersection import *
from interval import *
from node import *
from stl_parser_visitor import *
from stl_specification_parser import *
from stl_specification import *
from stl_temporal_nodes import *
from time_interpreter import *
from abstract_ast_parser import AbstractAst



def monitor():
    # # stl
    spec = StlDiscreteTimeSpecification()
    print("Specification instance created:", spec.name)
    spec.declare_var('a', 'float')
    spec.declare_var('b', 'float')
    spec.spec = 'eventually[0,1] (a >= b)'

    try:
        spec.parse()
        spec.pastify()
    except MonException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

    rob = spec.update(0, [('a', 100.0), ('b', 20.0)])
    print('time=' + str(0) + ' rob=' + str(rob))

    rob = spec.update(1, [('a', -1.0), ('b', 2.0)])
    print('time=' + str(0) + ' rob=' + str(rob))

    rob = spec.update(2, [('a', -2.0), ('b', -10.0)])
    print('time=' + str(0) + ' rob=' + str(rob))

if __name__ == '__main__':
    monitor()