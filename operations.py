from abc import ABCMeta, abstractmethod


class AbstractInterpreter(object):
    """
    Abstract Operation: template for any monitoring operation
    """
    __metaclass__ = ABCMeta
    NOT_IMPLEMENTED = "You should implement this."

    def exist_ast(self):
        if self.ast is None:
            raise RTAMTException('ast is empty')
        return

    def set_ast(self, ast):
        self.ast = ast
        return
    
################################################################################################

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
    
###############################################################################################

class DenseTimeInterpreter(TimeInterpreter):

    def __init__(self):
        super(DenseTimeInterpreter, self).__init__()
        return

    #input format
    #a = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
    #b = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]
    #dataset = [['a', a], ['b', b]]
    # def dataset_check(self, dataset):
    #     #TODO check that data fromat more.
    #     #TODO chage to dict format
    #     pass

    def set_variable_to_ast_from_dataset(self, dataset):
        for data in dataset:
            var_name = data[0]
            var_object = data[1]
            self.ast.var_object_dict[var_name] = var_object

    def time_unit_transformer(self, node):
        b = node.begin
        e = node.end
        b_unit = node.begin_unit
        e_unit = node.end_unit
        if len(node.begin_unit) == 0:
            if len(node.end_unit) > 0:
                b_unit = node.end_unit
            else:
                b_unit = self.ast.unit
                e_unit = self.ast.unit

        b = b * (self.ast.U[self.ast.unit] / self.ast.U[b_unit])
        e = e * (self.ast.U[self.ast.unit] / self.ast.U[e_unit])

        return b, e

    
################################################################################################


class AbstractOnlineOperation:
    """
    Abstract Operation: template for online operation
    """
    __metaclass__ = ABCMeta

    NOT_IMPLEMENTED = "You should implement this."

    @abstractmethod
    def __init__(self, *args, **kargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def update(self, node, *args, **kargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def reset(self):
        raise NotImplementedError(self.NOT_IMPLEMENTED)
    
    
##################################################################################################
    
class AbstractDenseTimeOnlineOperation(AbstractOnlineOperation):
    """
    Abstract Desne TimeOperation: template for online operation
    """

    @abstractmethod
    def update_final(self, node, *args, **kargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

####################################################################################################

