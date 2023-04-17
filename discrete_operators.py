#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod
from exception import MonException
from enumerations import StlComparisonOperator
import collections
import math



class AbstractOnlineOperation:
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
    
    
############################################################################################

class AlwaysOperation(AbstractOnlineOperation):
    def __init__(self):
        self.prev_out = float("inf")

    def reset(self):
        self.__init__()

    def update(self, sample):
        sample_return = min(sample, self.prev_out)
        self.prev_out = sample_return
        return sample_return
    
class AndOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right):
        sample_return = min(sample_left, sample_right)
        return sample_return
    
class ConstantOperation(AbstractOnlineOperation):
    def __init__(self, val):
        self.val = val

    def reset(self):
        pass

    def update(self):
        return self.val

class EventuallyOperation(AbstractOnlineOperation):
    def __init__(self):
        self.prev_out = -float("inf")

    def reset(self):
        self.__init__()

    def update(self, sample):
        sample_return = max(sample, self.prev_out)
        self.prev_out = sample_return
        return sample_return

class FallOperation(AbstractOnlineOperation):
    def __init__(self):
        self.prev = float("inf")

    def reset(self):
        self.__init__()

    def update(self, sample):
        sample_return = min(self.prev, - sample)
        self.prev = sample
        return sample_return
    
class HistoricallyOperation(AbstractOnlineOperation):
    def __init__(self):
        self.prev_out = float("inf")

    def reset(self):
        self.__init__()

    def update(self, sample):
        sample_return = min(sample, self.prev_out)
        self.prev_out = sample_return
        return sample_return
class HistoricallyTimedOperation(AbstractOnlineOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.buffer = collections.deque(maxlen=(self.end + 1))

        self.reset()

    def reset(self):
        for i in range(self.end + 1):
            val = float("inf")
            self.buffer.append(val)

    def update(self, sample):
        self.buffer.append(sample)
        sample_return = float("inf")
        for i in range(self.end-self.begin+1):
            sample_return = min(sample_return, self.buffer[i])
        return sample_return
    
#************************************************************************apala implement this ******************************************************************************************
class AlwaysTimedOperation(AbstractOnlineOperation):
    #historically timed
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.buffer = collections.deque(maxlen=(self.end + 1))

        self.reset()

    def reset(self):
        for i in range(self.end + 1):
            val = float("inf")
            self.buffer.append(val)

    def update(self, sample):
        # self.buffer.append(sample)
        # sample_return = float("inf")
        # for i in range(self.end-self.begin+1):
        #     sample_return = min(sample_return, self.buffer[i])
        # return sample_return
    
        # print("begin:", self.begin, "end:", self.end)
        self.buffer.extendleft(sample[self.begin:self.end+1])
        # print(self.buffer)
        sample_return = min(self.buffer)
       
        sample_return = float("inf")
        for i in range(self.end - self.begin + 1):
            sample_range = list(self.buffer)[self.begin + i:self.end + i + 1] # get the range of samples
            # print(sample_range)
            sample_return = min(sample_return, min(sample_range)) # calculate the maximum value in the range
        return sample_return
        


class EventuallyTimedOperation(AbstractOnlineOperation):
    #once timed
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.buffer = collections.deque(maxlen=(self.end + 1))

        self.reset()

    def reset(self):
        for i in range(self.end + 1):
            val = - float("inf")
            self.buffer.append(val)


    def update(self, sample):
       
        # print("begin:", self.begin, "end:", self.end)
        self.buffer.extendleft(sample[self.begin:self.end+1])
        # print(sample[self.begin:self.end+1])
        # print(self.buffer)
        sample_return = max(self.buffer)
       
        sample_return = -float("inf")
        for i in range(self.end - self.begin + 1):
            sample_range = list(self.buffer)[self.begin + i:self.end + i + 1] # get the range of samples
            # print(sample_range)
            sample_return = max(sample_return, max(sample_range)) # calculate the maximum value in the range
        return sample_return
    
########################################################################################################################################################################################
class IffOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right):
        sample_return = -abs(sample_left - sample_right)
        return sample_return
    
class ImpliesOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right):
        sample_return = max(-sample_left, sample_right)
        return sample_return
    
class NotOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample):
        sample_return = - sample
        return sample_return
    
class OnceOperation(AbstractOnlineOperation):
    def __init__(self):
        self.prev_out = -float("inf")

    def reset(self):
        self.__init__()

    def update(self, sample):
        sample_return = max(sample, self.prev_out)
        self.prev_out = sample_return
        return sample_return

class OnceTimedOperation(AbstractOnlineOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.buffer = collections.deque(maxlen=(self.end + 1))

        self.reset()

    def reset(self):
        for i in range(self.end + 1):
            val = - float("inf")
            self.buffer.append(val)

    def update(self, sample):
        self.buffer.append(sample)
        sample_return = -float("inf")
        for i in range(self.end-self.begin+1):
            sample_return = max(sample_return, self.buffer[i])
        return sample_return
    
class OrOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right):
        sample_return = max(sample_left, sample_right)
        return sample_return

class PrecedesTimedOperation(AbstractOnlineOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

        self.buffer = []
        self.buffer.append(collections.deque(maxlen=(self.end + 1)))
        self.buffer.append(collections.deque(maxlen=(self.end + 1)))

        self.reset()

    def reset(self):
        for i in range(self.end + 1):
            s_sample_left = float("inf")
            s_sample_right = - float("inf")
            self.buffer[0].append(s_sample_left)
            self.buffer[1].append(s_sample_right)

    def update(self, sample_left, sample_right):
        self.buffer[0].append(sample_left)
        self.buffer[1].append(sample_right)
        sample_return = - float("inf")

        for i in range(self.begin, self.end+1):
            sample_left = float("inf")
            sample_right = self.buffer[1][i]
            for j in range(0, i):
                sample_left = min(sample_left, self.buffer[0][j])
            sample_return = max(sample_return, min(sample_left, sample_right))

        return sample_return
    
class PredicateOperation(AbstractOnlineOperation):
    def __init__(self, comparison_op):
        self.comparison_op = comparison_op

    def reset(self):
        pass

    def compute(self, sample_left, sample_right):
        if self.comparison_op.value == StlComparisonOperator.EQUAL.value:
            sample_return = - abs(sample_left - sample_right)
        elif self.comparison_op.value == StlComparisonOperator.NEQ.value:
            sample_return = abs(sample_left - sample_right)
        elif self.comparison_op.value == StlComparisonOperator.LEQ.value or self.comparison_op.value == StlComparisonOperator.LESS.value:
            sample_return = sample_right - sample_left
        elif self.comparison_op.value == StlComparisonOperator.GEQ.value or self.comparison_op.value == StlComparisonOperator.GREATER.value:
            sample_return = sample_left - sample_right
        else:
            raise MonException('Unknown predicate operation')

        return sample_return
   #*************************added by apala ************************************************************************************************************************************ 
   
    def update(self, sample_left, sample_right):
        
        # print("type of sample left :", type(sample_left))
        # print("type of sample right :", type(sample_right))
        
        if (isinstance(sample_left, list) or isinstance(sample_left, tuple))  and (isinstance(sample_right, list) or isinstance(sample_right, tuple)):
            # Both samples are lists/tuple
            if len(sample_left) != len(sample_right):
                raise ValueError('Sample lists must have the same length')
            sample_return = []
            for i in range(len(sample_left)):
                sample_return.append(self.compute(sample_left[i], sample_right[i]))
                
                
        elif (isinstance(sample_left, list) or isinstance(sample_left, tuple)) and isinstance(sample_right, float):
            # Only the left sample is a list/tuple
            sample_return = []
            for i in range(len(sample_left)):
                sample_return.append(self.compute(sample_left[i], sample_right))
                
                
        elif (isinstance(sample_right, list) or isinstance(sample_right, tuple)) and isinstance(sample_left, float):
            # Only the right sample is a list/tuple
            sample_return = []
            for i in range(len(sample_right)):
                sample_return.append(self.compute(sample_left, sample_right[i]))
                
                
        else:
            # Neither sample is a list
            sample_return = self.compute(sample_left, sample_right)

        return sample_return
        
#**********************************************************************************************************************************************************************************
    def sat(self, sample_left, sample_right):
        if self.comparison_op.value == StlComparisonOperator.EQUAL.value:
            sample_return = sample_left == sample_right
        elif self.comparison_op.value == StlComparisonOperator.NEQ.value:
            sample_return = sample_left != sample_right
        elif self.comparison_op.value == StlComparisonOperator.GEQ.value:
            sample_return = sample_left >= sample_right
        elif self.comparison_op.value == StlComparisonOperator.GREATER.value:
            sample_return = sample_left > sample_right
        elif self.comparison_op.value == StlComparisonOperator.LEQ.value:
            sample_return = sample_left <= sample_right
        elif self.comparison_op.value == StlComparisonOperator.LESS.value:
            sample_return = sample_left < sample_right
        else:
            raise MonException('Unknown predicate operation')

        return sample_return

class PreviousOperation(AbstractOnlineOperation):
    def __init__(self):
        self.prev = float("inf")

    def reset(self):
        self.__init__()

    def update(self, sample):
        sample_return = self.prev
        self.prev = sample

        return sample_return
    
class RiseOperation(AbstractOnlineOperation):
    def __init__(self):
        self.prev = -float("inf")

    def reset(self):
        self.__init__()

    def update(self, sample):
        sample_return = min(- self.prev, sample)
        self.prev = sample

        return sample_return
    
class SinceOperation(AbstractOnlineOperation):
    def __init__(self):
        self.prev_out = -float("inf")

    def reset(self):
        self.__init__()

    def update(self, sample_left, sample_right):
        sample_return = min(sample_left, self.prev_out)
        sample_return = max(sample_return, sample_right)
        self.prev_out = sample_return
        return sample_return

class SinceTimedOperation(AbstractOnlineOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

        self.buffer_sample_left = collections.deque(maxlen=(self.end + 1))
        self.buffer_sample_right = collections.deque(maxlen=(self.end + 1))

        self.reset()

    def reset(self):
        for i in range(self.end + 1):
            s_sample_left = float("inf")
            s_sample_right = - float("inf")
            self.buffer_sample_left.append(s_sample_left)
            self.buffer_sample_right.append(s_sample_right)

    def update(self, sample_left, sample_right):
        self.buffer_sample_left.append(sample_left)
        self.buffer_sample_right.append(sample_right)
        sample_return = - float("inf")

        for i in range(self.end-self.begin+1):
            sample_left = float("inf")
            sample_right = self.buffer_sample_right[i]
            for j in range(i+1,self.end+1):
                sample_left = min(sample_left, self.buffer_sample_left[j])
            sample_return = max(sample_return, min(sample_left, sample_right))

        return sample_return
    
class XorOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right):
        sample_return = abs(sample_left - sample_right)
        return sample_return
    
####################################arithmetic operations from semantics > arithmetic > discrete_time > online ######################################

class AbsOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample):
        sample_result = abs(sample)
        return sample_result
    
class AdditionOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right):
        sample_result = sample_left + sample_right
        return sample_result

class DivisionOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right):
        sample_result = sample_left / sample_right
        return sample_result

class ExpOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample):
        sample_result = math.exp(sample)
        return sample_result
    
class MultiplicationOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right):
        sample_result = sample_left * sample_right
        return sample_result
    
class PowOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right):
        sample_result = math.pow(sample_left, sample_right)
        return sample_result
    
class SqrtOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample):
        if sample < 0:
            raise Exception('sqrt: input is smaller than 0.')
        sample_result = math.sqrt(sample)
        return sample_result
    
class SubtractionOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right):
        sample_result = sample_left - sample_right
        return sample_result
