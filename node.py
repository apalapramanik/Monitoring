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
        
        
############################################################################################# from syntax > node > ltl

class Variable(LeafNode):
    """A class for storing STL real-valued Variable nodes
            Inherits Node
        """
    def __init__(self, var, field=None, iotype='output'):
        """Constructor for Variable node
        Parameters:
            var : String
            field : String
        """

        super(Variable, self).__init__()
        self.var = var
        self.field = field
        self.io_type = iotype
        self.node = None

        if (iotype == 'input'):
            self.in_vars = [var]
        else:
            self.out_vars = [var]

        if not self.field:
            self.name = self.var
        else:
            self.name = self.var + '.' + self.field

    @property
    def var(self):
        """Getter for var"""
        return self.__var
    
    @var.setter
    def var(self, var):
        """Setter for var"""
        self.__var = var

    @property
    def field(self):
        """Getter for field"""
        return self.__field

    @field.setter
    def field(self, field):
        """Setter for field"""
        self.__field = field

    @property
    def io_type(self):
        """Getter for io_type"""
        return self.__io_type

    @io_type.setter
    def io_type(self, io_type):
        """Setter for io_type"""
        self.__io_type = io_type
        
class Constant(LeafNode):
    """A class for storing STL real-valued Constant nodes
                Inherits Node
    Attributes:
        val : double
    """
    def __init__(self, val):
        """Constructor for Const node
        Parameters:
            val : double
        """

        super(Constant, self).__init__()
        self.val = val

        self.name = str(val)


    @property
    def val(self):
        """Getter for val"""
        return self.__val
    
    @val.setter
    def val(self, val):
        """Setter for child"""
        self.__val = val
        
class Disjunction(BinaryNode):
    """A class for storing STL Or nodes
        Inherits TemporalNode
    """
    def __init__(self, child1, child2):
        """Constructor for Or node
        Parameters:
            child1 : stl.Node
            child2 : stl.Node
        """
        super(Disjunction, self).__init__(child1, child2)

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

        self.name = '(' + child1.name + ')or(' + child2.name + ')'
        


            
    
            
    
    
    
