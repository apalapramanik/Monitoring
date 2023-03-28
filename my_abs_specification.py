from abc import ABCMeta

class AbstractSpecification(object):
    __metaclass__ = ABCMeta
    
    def __init__(self, ast):
        self.name = 'Abstract Specification'
        self.ast = ast
        self.interpreter = None
        self.set_ast_flag = False
        self.out_var = ''
        self.out_var_field = ''
        self.var_topic_dict = dict()
        self.free_vars = set()
        self.var_object_dict = dict()