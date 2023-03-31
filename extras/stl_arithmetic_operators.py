from operations import AbstractRuntimeOperation
import math
import intersection as intersect


class AbsOperation(AbstractRuntimeOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample, *args, **kargs):
        sample_result = []

        for in_sample in sample:
            out_time = in_sample[0]
            out_value = abs(in_sample[1])
            sample_result.append([out_time, out_value])

        return sample_result

    def update_final(self, sample, *args, **kargs):
        return self.update(sample, *args, **kargs)
    
#######################################################################

class AdditionOperation(AbstractRuntimeOperation):
    def __init__(self):
        self.sample_left_buf = []
        self.sample_right_buf = []

    def reset(self):
        pass

    def update(self, sample_left, sample_right, *args, **kargs):
        sample_result = []
        self.sample_left_buf = self.sample_left_buf + sample_left
        self.sample_right_buf = self.sample_right_buf + sample_right

        sample_result, last, left, right = intersect.intersection(self.sample_left_buf, self.sample_right_buf, intersect.addition)

        self.sample_left_buf = left
        self.sample_right_buf = right
        if sample_result:
            self.last = last

        return sample_result

    def update_final(self, sample_left, sample_right, *args, **kargs):
        return self.update(sample_left, sample_right, *args, **kargs) + [self.last]
    
###################################################################################

class DivisionOperation(AbstractRuntimeOperation):
    def __init__(self):
        self.sample_left_buf = []
        self.sample_right_buf = []

    def reset(self):
        pass

    def update(self, sample_left, sample_right, *args, **kargs):
        sample_result = []
        self.sample_left_buf = self.sample_left_buf + sample_left
        self.sample_right_buf = self.sample_right_buf + sample_right

        sample_result, last, left, right = intersect.intersection(self.sample_left_buf, self.sample_right_buf, intersect.division)


        self.sample_left_buf = left
        self.sample_right_buf = right
        if sample_result:
            self.last = last

        return sample_result

    def update_final(self, sample_left, sample_right, *args, **kargs):
        return self.update(sample_left, sample_right, *args, **kargs) + [self.last]
    
############################################################################################

class ExpOperation(AbstractRuntimeOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample, *args, **kargs):
        sample_result = []

        for i in sample:
            out_time = i[0]
            out_value = math.exp(i[1])
            sample_result.append([out_time, out_value])

        return sample_result

    def update_final(self, sample, *args, **kargs):
        return self.update(sample, *args, **kargs)
    
############################################################################################

class MultiplicationOperation(AbstractRuntimeOperation):
    def __init__(self):
        self.sample_left_buf = []
        self.sample_right_buf = []

    def reset(self):
        pass

    def update(self, sample_left, sample_right, *args, **kargs):
        sample_result = []
        self.sample_left_buf = self.sample_left_buf + sample_left
        self.sample_right_buf = self.sample_right_buf + sample_right

        sample_result, last, left, right = intersect.intersection(self.sample_left_buf, self.sample_right_buf, intersect.multiplication)

        self.sample_left_buf = left
        self.sample_right_buf = right
        if sample_result:
            self.last = last

        return sample_result

    def update_final(self, sample_left, sample_right, *args, **kargs):
        return self.update(sample_left, sample_right, *args, **kargs) + [self.last]
    
##########################################################################################

class PowOperation(AbstractRuntimeOperation):
    def __init__(self):
        self.sample_left_buf = []
        self.sample_right_buf = []

    def reset(self):
        pass

    def update(self, sample_left, sample_right, *args, **kargs):
        self.sample_left_buf = self.sample_left_buf + sample_left
        self.sample_right_buf = self.sample_right_buf + sample_right

        sample_result, last, left, right = intersect.intersection(self.sample_left_buf, self.sample_right_buf, intersect.power)

        self.sample_left_buf = left
        self.sample_right_buf = right
        if sample_result:
            self.last = last

        return sample_result

    def update_final(self, sample_left, sample_right, *args, **kargs):
        return self.update(sample_left, sample_right, *args, **kargs) + [self.last]
    
###########################################################################################

class SqrtOperation(AbstractRuntimeOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample):
        sample_result = []

        for i in sample:
            if i[1] < 0:
                raise Exception('sqrt: input is smaller than 0.')
            out_time = i[0]
            out_value = math.sqrt(i[1])
            sample_result.append([out_time, out_value])

        return sample_result

    def update_final(self, sample, *args, **kargs):
        return self.update(sample, *args, **kargs)
    
#############################################################################################

class SubtractionOperation(AbstractRuntimeOperation):
    def __init__(self):
        self.sample_left = []
        self.sample_right = []

    def reset(self):
        pass

    def update(self, sample_left, sample_right, *args, **kargs):
        self.sample_left = self.sample_left + sample_left
        self.sample_right = self.sample_right + sample_right

        sample_result, last, left, right = intersect.intersection(self.sample_left, self.sample_right, intersect.subtraction)

        self.sample_left = left
        self.sample_right = right
        if sample_result:
            self.last = last

        return sample_result

    def update_final(self, sample_left, sample_right, *args, **kargs):
        return self.update(sample_left, sample_right, *args, **kargs) + [self.last]