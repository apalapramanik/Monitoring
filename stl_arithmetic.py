from node import UnaryNode, BinaryNode

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
        
