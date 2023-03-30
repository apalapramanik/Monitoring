from abc import ABCMeta, abstractmethod
from exception import MonException



##########################combine AbstractOnlineOperation and AbstractDenseTimeOnlineOperation into == my class AbstractRuntimeOperation #################################

class AbstractRuntimeOperation:
    """
    Abstract Operation: template for runtime operation
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
    
    @abstractmethod
    def update_final(self, node, *args, **kargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)
    

    

    
# ################################################################################################


# class AbstractOnlineOperation:
#     """
#     Abstract Operation: template for online operation
#     """
#     __metaclass__ = ABCMeta

#     NOT_IMPLEMENTED = "You should implement this."

#     @abstractmethod
#     def __init__(self, *args, **kargs):
#         raise NotImplementedError(self.NOT_IMPLEMENTED)

#     @abstractmethod
#     def update(self, node, *args, **kargs):
#         raise NotImplementedError(self.NOT_IMPLEMENTED)

#     @abstractmethod
#     def reset(self):
#         raise NotImplementedError(self.NOT_IMPLEMENTED)
    
    
# ##################################################################################################
    
# class AbstractDenseTimeOnlineOperation(AbstractOnlineOperation):
#     """
#     Abstract Desne TimeOperation: template for online operation
#     """

#     @abstractmethod
#     def update_final(self, node, *args, **kargs):
#         raise NotImplementedError(self.NOT_IMPLEMENTED)