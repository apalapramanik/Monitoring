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
