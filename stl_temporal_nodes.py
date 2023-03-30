from node import UnaryNode, BinaryNode, LeafNode
from interval import Interval

class TimedAlways(UnaryNode, Interval):
    """A class for storing STL Always nodes
        Inherits TemporalNode
    """
    def __init__(self, child, interval, is_pure_python=True):
        """Constructor for Always
        Parameters:
            child : stl.Node
            bound : Interval
        """
        UnaryNode.__init__(self, child)
        Interval.__init__(self, interval.begin, interval.end, interval.begin_unit, interval.end_unit)

        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'always[' + str(self.begin) + str(self.begin_unit) + ',' + str(self.end) + str(self.end_unit) + '](' + child.name + ')'



class TimedEventually(UnaryNode, Interval):
    """A class for storing STL Eventually nodes
            Inherits TemporalNode
    """
    def __init__(self, child, interval, is_pure_python=True):
        """Constructor for Eventually node
        Parameters:
            child : stl.Node
            bound : Interval
        """
        UnaryNode.__init__(self, child)
        Interval.__init__(self, interval.begin, interval.end, interval.begin_unit, interval.end_unit)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars
        self.name = 'eventually[' + str(self.begin) + str(self.begin_unit) + ',' + str(self.end) + str(self.end_unit) + '](' + child.name + ')'


class TimedHistorically(UnaryNode, Interval):

    def __init__(self, child, interval, is_pure_python=True):
        UnaryNode.__init__(self, child)
        Interval.__init__(self, interval.begin, interval.end, interval.begin_unit, interval.end_unit)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'historically[' + str(self.begin) + str(self.begin_unit) + ',' + str(self.end) + str(self.end_unit) + '](' + child.name + ')'


class TimedOnce(UnaryNode, Interval):
    """A class for storing STL Once nodes
                Inherits TemporalNode
    """
    def __init__(self, child, interval, is_pure_python=True):
        """Constructor for Once node
        Parameters:
            child : stl.Node
            bound : Interval
        """

        UnaryNode.__init__(self, child)
        Interval.__init__(self, interval.begin, interval.end, interval.begin_unit, interval.end_unit)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'once[' + str(self.begin) + str(self.begin_unit) + ',' + str(self.end) + str(self.end_unit) + '](' + child.name + ')'

class TimedPrecedes(BinaryNode, Interval):
    """A class for storing STL Precedes nodes - an auxilliary operator need for translating
       bounded future STL formulas to pure past formulas
                Inherits TemporalNode
    """

    def __init__(self, child1, child2, interval, is_pure_python=True):
        """Constructor for Precedes node
        Parameters:
            child1 : stl.Node
            child2 : stl.Node
            bound : Interval
        """
        BinaryNode.__init__(self, child1, child2)
        Interval.__init__(self, interval.begin, interval.end, interval.begin_unit, interval.end_unit)

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

        self.name = '(' + child1.name + ')precedes[' + str(self.begin) + str(self.begin_unit) + ',' \
                    + str(self.end) + str(self.end_unit) + '](' + child2.name + ')'
                    
class TimedSince(BinaryNode, Interval):
    """A class for storing STL Since nodes
                Inherits TemporalNode
    """
    def __init__(self, child1, child2, interval, is_pure_python=True):
        """Constructor for Since node
            Parameters:
                child1 : stl.Node
                child2 : stl.Node
                bound : Interval
        """

        BinaryNode.__init__(self, child1, child2)
        Interval.__init__(self, interval.begin, interval.end, interval.begin_unit, interval.end_unit)

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

        self.name = '(' + child1.name + ')since[' + str(self.begin) + str(self.begin_unit) + ',' + str(
                self.end) + str(self.end_unit) + '](' + child2.name + ')'
        
class TimedUntil(BinaryNode, Interval):
    """
    A class for storing STL Since nodes
    Inherits TemporalNode
    """
    def __init__(self, child1, child2, interval, is_pure_python=True):
        """Constructor for Until node
            Parameters:
                child1 : stl.Node
                child2 : stl.Node
                bound : Interval
        """
        BinaryNode.__init__(self, child1, child2)
        Interval.__init__(self, interval.begin, interval.end, interval.begin_unit, interval.end_unit)

        self.name = '(' + child1.name + ')until[' + str(self.begin) + str(self.begin_unit) + ',' + str(
            self.end) + str(self.end_unit) + '](' + child2.name + ')'

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars
        
        
########### from ltl ############

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

