#!/usr/bin/env python3
import sys
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
from ltl_ast_visitor import *
from ltl_pastifier import *



def monitor_a():
    # # stl
    spec = StlDiscreteTimeSpecification()
    spec.declare_var('a', 'float')
    spec.declare_var('b', 'float')
    spec.spec = 'eventually[0,1](a >= b)'

    try:
        spec.parse()
        # spec.pastify()
    except MonException as err:
        print('Mon Exception: {}'.format(err))
        sys.exit()
        
    a = [1.0, 2.0, 3.0, 4.0]
    
    rob = spec.update(0, [('a', 100.0), ('b', 20.0)])
    print('time=' + str(0) + ' rob=' + str(rob))

    rob = spec.update(1, [('a', -1.0), ('b', 2.0)])
    print('time=' + str(0) + ' rob=' + str(rob))

    rob = spec.update(2, [('a', -2.0), ('b', -10.0)])
    print('time=' + str(0) + ' rob=' + str(rob))

# 

def monitor_b():
    # # stl
    spec = StlDiscreteTimeSpecification()
    spec.declare_var('a', 'float')
    # spec.declare_var('b', 'float')
    spec.spec = 'a >= 2'

    try:
        spec.parse()
        spec.pastify()
    except MonException as err:
        print('Mon Exception: {}'.format(err))
        sys.exit()

    rob= spec.update(0, [('a', 10.0)])  
    print('time=' + str(0) + ' rob=' + str(rob))

    rob = spec.update(1, [('a', -1.0)])
    print('time=' + str(0) + ' rob=' + str(rob))

    rob = spec.update(2, [('a', -2.0)])
    print('time=' + str(0) + ' rob=' + str(rob))



        
def monitor_d():
    # # stl
    spec = StlDiscreteTimeSpecification()
    spec.declare_var('pred', 'float')
    spec.declare_var('dist', 'float')
    spec.spec = '(always[0,3](pred >= dist)) implies (eventually[3,5](pred < dist))'
    # spec.spec = '(always[0,3](pred >= dist))'
    spec.parse()
   


    # try:
    #     spec.parse()
        
    # except MonException as err:
    #     print('Mon Exception: {}'.format(err))
    #     sys.exit()
        
    prediction = [0.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0]
    
    rob = spec.update(0, [('pred', prediction), ('dist', 2.0)])
    print('time = ' + str(0) + ',  robustness = ' + str(rob))

    


if __name__ == '__main__':
    # Process arguments
    monitor_d()
  


# def monitor_b():
#     # data
#     dataSet = {
#          'time': [0, 1, 2],
#          'a': [100.0, -1.0, -2.0],
#          'b': [20.0, 2.0, -10.0]
#     }

#     # # stl
#     spec = StlDiscreteTimeSpecification()
#     spec.name = 'STL discrete-time online Python monitor'
#     spec.declare_var('a', 'float')
#     spec.declare_var('b', 'float')
#     spec.spec = 'a + b >= - 2'

#     try:
#         spec.parse()
#     except MonException as err:
#         print('STL Parse Exception: {}'.format(err))
#         sys.exit()

#     rob = spec.evaluate(dataSet)
#     print('Robustness: ' + str(rob))