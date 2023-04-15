#!/usr/bin/env python3
from abc import ABCMeta
from enumerations import StlIOType

class AbstractNode:
    
    __metaclass__ = ABCMeta
    
    def __init__(self):
        self.in_vars = []
        self.out_vars = []
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

class Always(UnaryNode):
    """A class for storing STL Always nodes
        Inherits TemporalNode
    """

    def __init__(self, child):
        """Constructor for Always
        Parameters:
            child : stl.Node
            bound : Interval
        """
        super(Always, self).__init__(child)

        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'always(' + child.name + ')'
        
class Conjunction(BinaryNode):
    """A class for storing STL Conjunction nodes
        Inherits TemporalNode
    """
    def __init__(self, child1, child2):
        """Constructor for Conjunction node
            Parameters:
                child1 : stl.Node
                child2 : stl.Node
        """
        super(Conjunction, self).__init__(child1, child2)

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

        self.name = '(' + child1.name + ')and(' + child2.name + ')'

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
        
class Eventually(UnaryNode):
    """A class for storing STL Eventually nodes
            Inherits TemporalNode
    """
    def __init__(self, child):
        """Constructor for Eventually node
        Parameters:
            child : stl.Node
            bound : Interval
        """
        super(Eventually, self).__init__(child)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars
        self.name = 'eventually(' + child.name + ')'
        
class Fall(UnaryNode):
    """A class for storing STL Neg nodes
        Inherits Node
    """
    def __init__(self, child):
        """Constructor for Neg node
            Parameters:
                child : stl.Node
        """
        super(Fall, self).__init__(child)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'fall(' + child.name + ')'
        
class Historically(UnaryNode):
    """A class for storing STL Historically nodes
         Inherits TemporalNode
    """
    def __init__(self, child):
        """Constructor for Historically node
            Parameters:
                child : stl.Node
        """
        super(Historically, self).__init__(child)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars
        self.name = 'historically(' + child.name + ')'
        
class Iff(BinaryNode):
    """A class for storing STL Iff nodes
        Inherits TemporalNode
    """
    def __init__(self, child1, child2):
        """Constructor for Iff node
        Parameters:
            child1 : stl.Node
            child2 : stl.Node
        """
        super(Iff, self).__init__(child1, child2)

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

        self.name = '(' + child1.name + ')<->(' + child2.name + ')'
        
class Implies(BinaryNode):
    """A class for storing STL Implies nodes
        Inherits TemporalNode
    """
    def __init__(self, child1, child2):
        """Constructor for Implies node
        Parameters:
            child1 : stl.Node
            child2 : stl.Node
        """
        super(Implies, self).__init__(child1, child2)

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

        self.name = '(' + child1.name + ')->(' + child2.name + ')'
        
class Neg(UnaryNode):
    """A class for storing STL Neg nodes
        Inherits Node
    """
    def __init__(self, child):
        """Constructor for Neg node
            Parameters:
                child : stl.Node
        """
        super(Neg, self).__init__(child)
        self.add_child(child)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'not(' + child.name + ')'
        
class Next(UnaryNode):
    """A class for storing STL Next nodes
        Inherits Node
    """
    def __init__(self, child):
        """Constructor for Next node
            Parameters:
                child : stl.Node
        """
        super(Next, self).__init__(child)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'next(' + child.name + ')'

class Once(UnaryNode):
    """A class for storing STL Once nodes
                Inherits TemporalNode
    """
    def __init__(self, child):
        """Constructor for Once node
        Parameters:
            child : stl.Node
            bound : Interval
        """

        super(Once, self).__init__(child)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars
        self.name = 'once(' + child.name + ')'

class Predicate(BinaryNode):
    """A class for storing STL real-valued Variable nodes
                Inherits Node
    Attributes:
        child1 : Node
        child2 : Node
        operator : OperatorType (LEQ, GEQ, LESS, GREATER, EQ or NEQ)
    """
    def __init__(self, child1, child2, operator):
        """Constructor for Predicate node
        Parameters:
            var : String
            field : String
            io_type : IOType enumeration (INPUT, OUTPUT or UNKNOWN)
            operator : OperatorType (LEQ, GEQ, LESS, GREATER, EQ or NEQ)
        """

        super(Predicate, self).__init__(child1, child2)
        self.operator = operator
        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

        self.name = '(' + child1.name + ')' + str(self.operator) + '(' + child2.name + ')'
        
class Previous(UnaryNode):
    """A class for storing STL Previous nodes
        Inherits Node
    """
    def __init__(self, child):
        """Constructor for Previous node
            Parameters:
                child : stl.Node
        """
        super(Previous, self).__init__(child)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'previous(' + child.name + ')'


class Rise(UnaryNode):
    """A class for storing STL Neg nodes
        Inherits Node
    """
    def __init__(self, child):
        """Constructor for Neg node
            Parameters:
                child : stl.Node
        """
        super(Rise, self).__init__(child)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'rise(' + child.name + ')'
        
class Since(BinaryNode):
    """A class for storing STL Since nodes
                Inherits TemporalNode
    """
    def __init__(self, child1, child2):
        """Constructor for Since node
            Parameters:
                child1 : stl.Node
                child2 : stl.Node
        """

        super(Since, self).__init__(child1, child2)

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars
        self.name = '(' + child1.name + ')since(' + child2.name + ')'
        
class Until(BinaryNode):
    """
    A class for storing STL Since nodes
    Inherits TemporalNode
    """
    def __init__(self, child1, child2):
        """Constructor for Until node
            Parameters:
                child1 : stl.Node
                child2 : stl.Node
                bound : Interval
        """
        super(Until, self).__init__(child1, child2)

        self.name = '(' + child1.name + ')until(' + child2.name + ')'

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars
        
class Xor(BinaryNode):
    """A class for storing STL Xor nodes
        Inherits TemporalNode
    """
    def __init__(self, child1, child2):
        """Constructor for Xor node
        Parameters:
            child1 : stl.Node
            child2 : stl.Node
        """
        super(BinaryNode, self).__init__()
        self.add_child(child1)
        self.add_child(child2)

        self.name = '(' + child1.name + ')xor(' + child2.name + ')'
        
        
####################################################################### syntax > node > arithmetic  ####################################
class Abs(UnaryNode):
    """A class for storing STL Neg nodes
        Inherits Node
    """
    def __init__(self, child):
        """Constructor for Neg node
            Parameters:
                child : stl.Node
        """
        super(Abs, self).__init__(child)

        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'abs(' + child.name + ')'
        
        
class Addition(BinaryNode):
    """A class for storing STL Conjunction nodes
        Inherits TemporalNode
    """
    def __init__(self, child1, child2):
        """Constructor for Conjunction node
            Parameters:
                child1 : stl.Node
                child2 : stl.Node
        """
        super(Addition, self).__init__(child1, child2)

        self.add_child(child1)
        self.add_child(child2)

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

        self.name = '(' + child1.name + ')+(' + child2.name + ')'
        
class Division(BinaryNode):
    """A class for storing STL Division nodes
        Inherits Node
    """
    def __init__(self, child1, child2):
        """Constructor for Division node
            Parameters:
                child1 : stl.Node
                child2 : stl.Node
        """
        super(Division, self).__init__(child1, child2)

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

        self.name = '(' + child1.name + ')/(' + child2.name + ')'
        
class Exp(UnaryNode):
    """A class for storing Exp nodes
        Inherits Node
    """
    def __init__(self, child):
        """Constructor for Exp node
            Parameters:
                child : stl.Node
        """
        super(Exp, self).__init__(child)

        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'exp(' + child.name + ')'
        
class Multiplication(BinaryNode):
    """A class for storing STL Multiplication nodes
        Inherits Node
    """
    def __init__(self, child1, child2):
        """Constructor for Multiplication node
            Parameters:
                child1 : stl.Node
                child2 : stl.Node
        """
        super(Multiplication, self).__init__(child1, child2)

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

        self.name = '(' + child1.name + ')*(' + child2.name + ')'
        
        
class Pow(BinaryNode):
    """A class for storing Pow nodes
        Inherits Node
    """
    def __init__(self, child1, child2):
        """Constructor for Pow node
            Parameters:
                child1 : stl.Node
                child2 : stl.Node
        """
        super(Pow, self).__init__(child1, child2)

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

        self.name = 'pow(' + child1.name + ',' + child2.name + ')'

class Sqrt(UnaryNode):
    """A class for storing STL Sqrt nodes
        Inherits Node
    """
    def __init__(self, child):
        """Constructor for Neg node
            Parameters:
                child : stl.Node
        """
        super(Sqrt, self).__init__(child)

        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'sqrt(' + child.name + ')'
        
class Subtraction(BinaryNode):
    """A class for storing STL Subtraction nodes
        Inherits Node
    """
    def __init__(self, child1, child2):
        """Constructor for Subtraction node
            Parameters:
                child1 : stl.Node
                child2 : stl.Node
        """
        super(Subtraction, self).__init__(child1, child2)


        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

        self.name = '(' + child1.name + ')-(' + child2.name + ')'

