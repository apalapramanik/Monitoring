from abc import ABCMeta, abstractmethod


class Interval(object):
    
    def __init__(self, begin, end, begin_unit="", end_unit=""):
        
        """
        begin: beginning of time interval
        end: end of time interval
            
        """
        
        self.begin = begin
        self.end = end
        self.begin_unit = begin_unit
        self.end_unit = end_unit
        
        
        
##########################################################################

class TimeInterpreter(object):
    
    __metaclass__ = ABCMeta
    
    def __init__(self):
        pass

    @abstractmethod
    def dataset_check(self, data):
        pass

    @abstractmethod
    def set_variable_to_ast_from_dataset(self, *args, **kargs):
        pass