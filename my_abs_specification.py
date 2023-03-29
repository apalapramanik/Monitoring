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
        
        
#######################################
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name
        
    @property
    def spec (self):
        return self.ast.spec
    
    @spec.setter
    def spec(self,spec):
        self.ast.spec
        
    
#########################################################

    def add_var(self,var):
        self.ast.vars.add(var)    
        
    
    def get_value(self, var_name):
        return self.ast.get_value(var_name)
    
    
    def add_sub_spec(self, sub_spec):
        self.ast.add_sub_spec(sub_spec)
        
    def set_var_io_type(self, var, io_type):
        self.ast.set_var_io_type(var, io_type)
        
    def declare_var(self, var_name, var_type):
        self.ast.declare_var(var_name, var_type)
        
    def declare_const(self, const_name, const_type, const_val):
        self.ast.declare_const(const_name, const_type, const_val)
        
###############################################################



    
    
    
        
