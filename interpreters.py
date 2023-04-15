#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod
from exception import MonException
from node import *
from time_interpreter import *
import operator



class AbstractInterpreter(object):
    """
    Abstract Operation: template for any monitoring operation
    """
    __metaclass__ = ABCMeta
    NOT_IMPLEMENTED = "You should implement this."

    def exist_ast(self):
        if self.ast is None:
            raise MonException('ast is empty')
        return

    def set_ast(self, ast):
        self.ast = ast
        return


################################################################################################

class AbstractOfflineInterpreter(AbstractInterpreter):
    def __init__(self):
        super(AbstractOfflineInterpreter, self).__init__()
        return

    @abstractmethod
    def evaluate(self, dataset):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    def visitSpec(self, node, *args, **kwargs):
        sample_return = self.visit(node, *args, **kwargs)
        self.ast.var_object_dict[node] = sample_return  #TODO subspec name is necessary as a key for var_object_dict.
        return sample_return
    
##############################################################################################

class AbstractOnlineInterpreter(AbstractInterpreter):
    def __init__(self):
        super(AbstractOnlineInterpreter, self).__init__()
        return

    def reset(self):
        # reset sub-specs
        for key in self.ast.var_subspec_dict:
            node = self.ast.var_subspec_dict[key]
            self.resetVisitor.visitAst(node, self.online_operator_dict)

        # reset spec
        self.resetVisitor.visitAst(self.ast, self.online_operator_dict)
        return

    def set_ast(self, ast):
        super(AbstractOnlineInterpreter, self).set_ast(ast)

        # init dict of online operators
        self.online_operator_dict = dict()

        self.visitAst(self.ast)

        # construct online_operator_dict for sub-specs
        #for key in self.ast.var_subspec_dict:
        #    node = self.ast.var_subspec_dict[key]
        #    self.visitAst(node)

        # construct online_operator_dict for spec
        #self.visitAst(self.ast)
        return

    @abstractmethod
    def update(self, *args, **kargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)
    
##########################################################################

class AbstractAstVisitor(object):
    __metaclass__ = ABCMeta

    def visitChildren(self, node, *args, **kwargs):
        result = None
        for nodeChild in node.children:
            # print("node children:", nodeChild)
            result = self.visit(nodeChild, *args, **kwargs)  
        # print(result)    
        return result   # visitChildren reterns only last result

    def visit(self, node, *args, **kwargs):
        if isinstance(node, BinaryNode):
            result = self.visitBinary(node, *args, **kwargs)
            # print("node type b:",result)
        elif isinstance(node, UnaryNode):
            result = self.visitUnary(node, *args, **kwargs)
            # print("node type u:",result)
        elif isinstance(node, LeafNode):
            result = self.visitLeaf(node, *args, **kwargs)
            # print("node type l:",result)
        else:
            raise MonException('{} is not RTAMT AST node'.format(node.__class__.__name__))
        return result

    def visitAst(self, ast, *args, **kwargs):
        out = []
        # print("ast.spec:", ast.spec)
        for spec in ast.specs:
            out.append(self.visit(spec, *args, **kwargs))
        # print(out)
        return out

    def visitSpec(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitBinary(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitUnary(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitLeaf(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)
###################################################################################

class AbstractOnlineResetVisitor(AbstractAstVisitor):
    def visitBinary(self, node, online_operator_dict):
        self.visitChildren(node, online_operator_dict)
        operator = online_operator_dict[node.name]
        # print("operator",operator)
        operator.reset()
        return

    def visitUnary(self, node, online_operator_dict):
        self.visitChildren(node, online_operator_dict)
        operator = online_operator_dict[node.name]
        operator.reset()
        return

    def visitLeaf(self, node, online_operator_dict):
        pass

######################################################################

class AbstractOnlineUpdateVisitor(AbstractAstVisitor):
    def visitSpec(self, node, online_operator_dict, var_object_dict):
        sample_return = self.visit(node, online_operator_dict, var_object_dict)
        var_object_dict[node] = sample_return  #TODO subspec name is necessary as a key for var_object_dict.
        return sample_return

    def visitBinary(self, node, online_operator_dict, var_object_dict):
        sample_left  = self.visit(node.children[0], online_operator_dict, var_object_dict)
        sample_right = self.visit(node.children[1], online_operator_dict, var_object_dict)
        operator = online_operator_dict[node.name]
        sample_return = operator.update(sample_left, sample_right)
        return sample_return

    def visitUnary(self, node, online_operator_dict, var_object_dict):
        sample = self.visit(node.children[0], online_operator_dict, var_object_dict)
        op = online_operator_dict[node.name]
        sample_return = op.update(sample)
        return sample_return

    def visitLeaf(self, node, online_operator_dict, var_object_dict):
        if isinstance(node, Constant):
            sample_return = self.visitConstant(node, online_operator_dict, var_object_dict)
        elif isinstance(node, Variable):
            sample_return = self.visitVariable(node, online_operator_dict, var_object_dict)
        return sample_return
    
######################################### abstract discrete time online interpreters ######################################################################

class AbstractDiscreteTimeOnlineInterpreter(AbstractOnlineInterpreter, DiscreteTimeInterpreter):

    def __init__(self):
        super(AbstractDiscreteTimeOnlineInterpreter, self).__init__()
        self.updateVisitor = DiscreteTimeOnlineUpdateVisitor()
        self.resetVisitor = AbstractOnlineResetVisitor()
        return

    # timestamp - float
    # inputs - list of [var name, var value] pairs
    # Example:
    # update(1, [['a', 2.2], ['b', 3.3]])
    #TODO merge dense and discrete into update AbstractOnlineInterpreter
    def update(self, timestamp, dataset):
        # check ast exists
        self.exist_ast()

        # update the value of every input variable
        self.set_variable_to_ast_from_dataset(dataset)

        # evaluate spec forest
        rob = self.updateVisitor.visitAst(self.ast, self.online_operator_dict, self.ast.var_object_dict)
        rob = rob[len(rob) - 1]

        out = self.ast.var_object_dict[self.ast.out_var]
        if self.ast.out_var_field:
            setattr(out, self.ast.out_var_field, rob)


        # Check if the difference between two consecutive timestamps is between
        # the accepted tolerance - if not, increase the violation counter
        if self.update_counter > 0:
            duration = (timestamp - self.previous_time) * self.normalize
            self.update_sampling_violation_counter(duration)

        # update time stamp and update counter
        self.previous_time = timestamp
        self.update_counter = self.update_counter + 1

        return rob

    def reset(self):
        super(AbstractDiscreteTimeOnlineInterpreter, self).reset()

        self.update_counter = int(0)
        self.previous_time = float(0.0)
        self.sampling_violation_counter = int(0)
        return

    def set_variable_to_ast_from_dataset(self, dataset):
        for data in dataset:
            var_name = data[0]
            var_value = data[1]
            self.ast.var_object_dict[var_name] = var_value

    @property
    def update_counter(self):
        return self.__update_counter

    @update_counter.setter
    def update_counter(self, update_counter):
        self.__update_counter = update_counter


class DiscreteTimeOnlineUpdateVisitor(AbstractOnlineUpdateVisitor):
    def visitVariable(self, node, online_operator_dict, var_object_dict):
        var = var_object_dict[node.var]
        if node.field:  #TODO Tom did not understand this line.
            sample_return = operator.attrgetter(node.field)(var)
        else:
            sample_return = var
        return sample_return

    def visitConstant(self, node, online_operator_dict, var_object_dict):
        return node.val


def discrete_time_online_interpreter_factory(AstVisitor):
    if not issubclass(AstVisitor, AbstractAstVisitor):  # type check
        raise MonException('{} is not RTAMT AST visitor'.format(AstVisitor.__name__))

    class DiscreteTimeOnlineInterpreter(AbstractDiscreteTimeOnlineInterpreter, AstVisitor):
        def __init__(self, *args, **kwargs):
            super(DiscreteTimeOnlineInterpreter, self).__init__(*args, **kwargs)

    return DiscreteTimeOnlineInterpreter

############### abstract discrete time offline interpreters ##################################################################################

class AbstractDiscreteTimeOfflineInterpreter(AbstractOfflineInterpreter, DiscreteTimeInterpreter):

    def __init__(self):
        super(AbstractDiscreteTimeOfflineInterpreter, self).__init__()
        return

    #input format
    #dataset = {
    #   'time': [0, 1, 2, 3, 4],
    #   'req': [100, -1, -2, 5, -1],
    #   'gnt': [20, -2, 10, 4, -1]
    #}
    #TODO merge dense and discrete into evaluate AbstractOfflineInterpreter
    def evaluate(self, dataset):
        # check ast exists
        self.exist_ast()

        #TODO move both of spec and sub-specs visit into syntax layer.
        # update the value of every input variable
        self.set_variable_to_ast_from_dataset(dataset)

        # evaluate spec forest
        length = len(dataset['time'])
        rob = self.visitAst(self.ast, length)
        rob = rob[len(rob)-1]

        # Check if the difference between two consecutive timestamps is between
        # the accepted tolerance - if not, increase the violation counter
        ts = dataset['time']
        for i in range(len(ts) - 1):
            duration = (ts[i+1] - ts[i]) * self.normalize
        self.update_sampling_violation_counter(duration)

        # convert format
        out_t = [[a[0], a[1]] for a in zip(ts, rob)]
        rob = out_t

        return rob

    def set_variable_to_ast_from_dataset(self, dataset):
        for key in dataset:
            if key != 'time':
                self.ast.var_object_dict[key] = dataset[key]


def discrete_time_offline_interpreter_factory(AstVisitor):
    if not issubclass(AstVisitor, AbstractAstVisitor):  # type check
        raise MonException('{} is not RTAMT AST visitor'.format(AstVisitor.__name__))

    class DiscreteTimeOfflineInterpreter(AbstractDiscreteTimeOfflineInterpreter, AstVisitor):
        def __init__(self, *args, **kwargs):
            super(DiscreteTimeOfflineInterpreter, self).__init__(*args, **kwargs)
    return DiscreteTimeOfflineInterpreter