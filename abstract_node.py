#import abc meta class from abc module: Abstract Base Class
from abc import ABCMeta

class AbstractNode:
    
    __metaclass__ = ABCMeta
    
    def __init__(self):
        
        """
        declare instance variables to store information about the instance of the class
        
        """
        self.input_variable = []
        self.output_variable = []
        self.children = list()
        self.interpreter = None
        self.name = ''
        self.node = None
    
    def add_child(self, child):
        self.children.append(child)
     
        
    def accept(self, visitor):
        
        """function to visit node
        Args:
            visitor : visitor object
        """
    
        for child in self.children:
            child.accept(visitor)
            
#######################################################################################

class LeafNode(AbstractNode):
    
    def __init__(self):
        super(LeafNode,self).__init__()
            
class UnaryNode(AbstractNode):
    
    def __init__(self, child):
        super(UnaryNode,self).__init__()
        self.add_child(child)
        
class BinaryNode(AbstractNode):
    
    def __init__(self, left_child, right_child):
        super(BinaryNode,self).__init__()
        self.add_child(left_child)
        self.add_child(right_child)
        
        
#############################################################################################


            
    
            
    
    
    
