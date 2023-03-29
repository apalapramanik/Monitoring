from operations import AbstractRuntimeOperation
import math

class AbsOperation(AbstractRuntimeOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample):
        sample_result = abs(sample)
        return sample_result
    
class AdditionOperation(AbstractRuntimeOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right):
        sample_result = sample_left + sample_right
        return sample_result

class SubtractionOperation(AbstractRuntimeOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right):
        sample_result = sample_left - sample_right
        return sample_result

class DivisionOperation(AbstractRuntimeOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right):
        sample_result = sample_left / sample_right
        return sample_result
    
class ExpOperation(AbstractRuntimeOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample):
        sample_result = math.exp(sample)
        return sample_result
    
class MultiplicationOperation(AbstractRuntimeOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right):
        sample_result = sample_left * sample_right
        return sample_result
    
class PowOperation(AbstractRuntimeOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right):
        sample_result = math.pow(sample_left, sample_right)
        return sample_result

class SqrtOperation(AbstractRuntimeOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample):
        if sample < 0:
            raise Exception('sqrt: input is smaller than 0.')
        sample_result = math.sqrt(sample)
        return sample_result
    
