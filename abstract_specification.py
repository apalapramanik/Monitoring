import os
from abc import ABCMeta
from time_interpreter import *
from exception import MonException
from interpreters import *
# from discrete_operators import AbstractOnlineOperation

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
        
        
##########################################################
        
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


    @property
    def out_var(self):
        return self.ast.out_var

    @out_var.setter
    def out_var(self, out_var):
        pass

    @property
    def out_var_field(self):
        return self.ast.out_var_field

    @out_var_field.setter
    def out_var_field(self, out_var_field):
        pass

    @property
    def var_topic_dict(self):
        return self.ast.var_topic_dict

    @var_topic_dict.setter
    def var_topic_dict(self, var_topic_dict):
        pass

    @property
    def var_object_dict(self):
        return self.ast.var_object_dict

    @var_object_dict.setter
    def var_object_dict(self, var_object_dict):
        self.__var_object_dict = var_object_dict
        self.ast.var_object_dict = self.var_object_dict

    @property
    def free_vars(self):
        return self.ast.free_vars

    @free_vars.setter
    def free_vars(self, free_vars):
        pass

###############################################################

    def set_var_topic(self, var_name, var_topic):
        self.ast.set_var_topic(var_name, var_topic)

    def parse(self):
        self.ast.parse()
        
    def set_sampling_period(self, sampling_period=int(1), unit='s', tolerance=float(0.1)):
        if hasattr(self, 'online_interpreter'):            
            self.online_interpreter.set_sampling_period(sampling_period, unit, tolerance)
        

    def get_sampling_frequency(self, sampling_period=int(1), unit='s', tolerance=float(0.1)):
        if hasattr(self, 'online_interpreter'):            
            self.online_interpreter.get_sampling_frequency()
            
    @property
    def sampling_violation_counter(self):
        if hasattr(self, 'online_interpreter'):
            return self.online_interpreter.sampling_violation_counter
            
    @property
    def sampling_tolerance(self):
        if hasattr(self, 'online_interpreter'):         
            return self.online_interpreter.sampling_tolerance
         
                
    ############################################################
    
    
    @property
    def publish_var(self):
        return self.__publish_var

    @publish_var.setter
    def publish_var(self, publish_var):
        self.__publish_var = publish_var

    @property
    def publish_var_field(self):
        return self.__publish_var_field

    @publish_var_field.setter
    def publish_var_field(self, publish_var_field):
        self.__publish_var_field = publish_var_field

    
    ##################################################################
    
    def add_input_var(self, input_var):
        self.in_vars.add(input_var)

    def remove_input_var(self, var):
        self.in_vars.discard(var)

    def add_output_var(self, output_var):
        self.out_vars.add(output_var)

    def remove_output_var(self, var):
        self.out_vars.discard(var)

    def add_op(self, op):
        self.ops.add(op)
        
    def get_spec_from_file(self, path):
        """Opens a text file and returns its content as a string
        Parameters:
            path : String - path to the filename
        Returns
            out : String - file content
        """
        out = None
        if os.path.exists(path):
            f = open(path, "r")
            out = f.read()
            f.close()
        else:
            raise MonException('The file {} does not exist.'.format(path))
        return out
        
######################################################################################   

## WORK ON THIS CLASS-------------------
    
class AbstractOnlineSpecification(AbstractSpecification):
    def __init__(self, ast, onlineInterpreter, pastifier=None):
        AbstractSpecification.__init__(self, ast)
        self.name = 'Abstract Online Specification'
        self.online_interpreter = onlineInterpreter
        self.pastifier = pastifier

    # forwarding pastify
    def pastify(self):
        self.ast = self.pastifier.pastify(self.ast)

    # forwarding to interpreter
    def update(self, *args, **kwargs):
        if self.set_ast_flag != True:
            self.online_interpreter.set_ast(self.ast)
            self.set_ast_flag = True

        
        if isinstance(self.online_interpreter, AbstractOnlineSpecification):
            if len(args) == 0:
                raise Exception()
            elif len(args) == 1:
                dataset = [args[0]]
            else:
                dataset = []
                for i in args:
                    dataset.append(i)
            return self.online_interpreter.update(dataset)
        
        else:
            pass

    def final_update(self, *args, **kwargs):
        if self.set_ast_flag != True:
            self.online_interpreter.set_ast(self.ast)
            self.set_ast_flag = True

       
        if len(args) == 0:
            raise Exception()
        elif len(args) == 1:
            dataset = [args[0]]
        else:
            dataset = []
            for i in args:
                dataset.append(i)

        return self.online_interpreter.final_update(dataset)

    def reset(self):
        self.online_interpreter.reset()

    
class AbstractOfflineSpecification(AbstractSpecification):
    def __init__(self, ast, offlineInterpreter):
        AbstractSpecification.__init__(self, ast)
        self.name = 'Abstract Offline Specification'
        self.offline_interpreter = offlineInterpreter

    # forwarding to interpreter
    def evaluate(self, *args, **kwargs):
        if self.set_ast_flag != True:
            self.offline_interpreter.set_ast(self.ast)
            self.set_ast_flag = True

        #TODO we may make it consistent with interpreter class.
        # if isinstance(self.offline_interpreter, AbstractDenseTimeOfflineInterpreter):
        #     if len(args) == 0:
        #         raise Exception()
        #     elif len(args) == 1:
        #         dataset = [args[0]]
        #     else:
        #         dataset = []
        #         for i in args:
        #             dataset.append(i)
        #     return self.offline_interpreter.evaluate(dataset)
        # elif isinstance(self.offline_interpreter, AbstractDiscreteTimeOfflineInterpreter):
            dataset = args[0]
            return self.offline_interpreter.evaluate(dataset)
        else:
            raise Exception('Wrong interpreter!')



class AbstractOfflineOnlineSpecification(AbstractOfflineSpecification, AbstractOnlineSpecification):
    def __init__(self, ast, offlineInterpreter, onlineInterpreter, pastifier=None):
        AbstractOfflineSpecification.__init__(self, ast, offlineInterpreter)
        AbstractOnlineSpecification.__init__(self, ast, onlineInterpreter, pastifier)
        self.name = 'Abstract Offline Online Specification' 
    
    
        
