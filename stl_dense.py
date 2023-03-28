from operations import AbstractDenseTimeOnlineOperation
import intersection as intersect

class AlwaysOperation(AbstractDenseTimeOnlineOperation):
    def __init__(self):
        self.prev = float("inf")

    def reset(self):
        pass

    def update(self, sample, *args, **kargs):
        sample_result = []

        for i in sample:
            out_time = i[0]
            out_value = min(i[1], self.prev)

            sample_result.append([out_time, out_value])
            self.prev = out_value

        return sample_result

    def update_final(self, sample, *args, **kargs):
        return self.update(sample, *args, **kargs)
    
#################################################################################

class AndOperation(AbstractDenseTimeOnlineOperation):
    def __init__(self):
        self.sample_left_buf = []
        self.sample_right_buf = []
        self.sample_last_buf = []

    def reset(self):
        pass

    def update(self, sample_left, sample_right, *args, **kargs):
        self.sample_left_buf = self.sample_left_buf + sample_left
        self.sample_right_buf = self.sample_right_buf + sample_right

        sample_result, last, left, right = intersect.intersection(self.sample_left_buf, self.sample_right_buf,
                                                                  intersect.conjunction)

        self.sample_left_buf = left
        self.sample_right_buf = right
        if sample_result:
            self.last = last

        return sample_result

    def update_final(self, sample_left, sample_right, *args, **kargs):
        return self.update(sample_left, sample_right, *args, **kargs) + [self.last]
    
##########################################################################################

class ConstantOperation(AbstractDenseTimeOnlineOperation):
    def __init__(self, val):
        self.val = val

    def update(self, *args, **kargs):
        out = [[0, self.val], [float("inf"), self.val]]
        return out

    def update_final(self, *args, **kargs):
        out = [[0, self.val], [float("inf"), self.val]]
        return
    
########################################################################################

class HistoricallyOperation(AbstractDenseTimeOnlineOperation):
    def __init__(self):
        self.prev = float("inf")

    def reset(self):
        pass

    def update(self, sample, *args, **kargs):
        result_sample = []

        for i in sample:
            out_time = i[0]
            out_value = min(i[1], self.prev)

            result_sample.append([out_time, out_value])
            self.prev = out_value

        return result_sample

    def update_final(self, sample, *args, **kargs):
        return self.update(sample, *args, **kargs)
    
####################################################################################

class ImpliesOperation(AbstractDenseTimeOnlineOperation):
    def __init__(self):
        self.sample_left_buf = []
        self.sample_right_buf = []
        self.last = []

    def reset(self):
        pass

    def update(self, sample_left, sample_right, *args, **kargs):
        self.sample_left_buf = self.sample_left_buf + sample_left
        self.sample_right_buf = self.sample_right_buf + sample_right

        sample_result, last, left, right = intersect.intersection(self.sample_left_buf, self.sample_right_buf, intersect.implication)

        self.sample_left_buf = left
        self.sample_right_buf = right
        if sample_result:
            self.last = last

        return sample_result

    def update_final(self, sample_left, sample_right, *args, **kargs):
        return self.update(sample_left, sample_right, *args, **kargs) + [self.last]
    
##############################################################################################

class NotOperation(AbstractDenseTimeOnlineOperation):
    def __init__(self):
        self.input = []

    def reset(self):
        pass

    def update(self, sample, *args, **kargs):
        sample_result = []

        for i in sample:
            out_time = i[0]
            out_value = - i[1]

            sample_result.append([out_time, out_value])

        return sample_result

    def update_final(self, sample, *args, **kargs):
        return self.update(sample, *args, **kargs)
    
###################################################################################################

class OnceOperation(AbstractDenseTimeOnlineOperation):
    def __init__(self):
        self.prev = - float("inf")

    def reset(self):
        pass

    def update(self, sample, *args, **kargs):
        sample_result = []

        for i in sample:
            out_time = i[0]
            out_value = max(i[1], self.prev)

            sample_result.append([out_time, out_value])
            self.prev = out_value

        return sample_result

    def update_final(self, sample, *args, **kargs):
        return self.update(sample, *args, **kargs)
    
##############################################################################################

class OrOperation(AbstractDenseTimeOnlineOperation):
    def __init__(self):
        self.sample_left_buf = []
        self.sample_right_buf = []
        self.last = []

    def reset(self):
        pass

    def update(self, sample_left, sample_right, *args, **kargs):
        self.sample_left_buf = self.sample_left_buf + sample_left
        self.sample_right_buf = self.sample_right_buf + sample_right

        sample_result, last, left, right = intersect.intersection(self.sample_left_buf, self.sample_right_buf, intersect.disjunction)

        self.sample_left_buf = left
        self.sample_right_buf = right
        if sample_result:
            self.last = last

        return sample_result

    def update_final(self, sample_left, sample_right, *args, **kargs):
        return self.update(sample_left, sample_right, *args, **kargs) + [self.last]

#############################################################################################################

class XorOperation(AbstractDenseTimeOnlineOperation):
    def __init__(self):
        self.sample_left_buf = []
        self.sample_right_buf = []
        self.last = []

    def reset(self):
        pass

    def update(self, sample_left, sample_right, *args, **kargs):
        self.sample_left_buf = self.sample_left_buf + sample_left
        self.sample_right_buf = self.sample_right_buf + sample_right

        sample_result, last, left, right = intersect.intersection(self.sample_left_buf, self.sample_right_buf, intersect.xor)

        self.sample_left_buf = left
        self.sample_right_buf = right
        if sample_result:
            self.last = last

        return sample_result

    def update_final(self, sample_left, sample_right, *args, **kargs):
        return self.update(sample_left, sample_right, *args, **kargs) + [self.last]

