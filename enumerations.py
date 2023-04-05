from enum import Enum

class BooleanOperator(Enum):
    AND = 0
    OR = 1
    IMPLIES = 2
    IFF = 3
    XOR = 4
    
# class StlComparisonOperator(Enum):
#     LESS = 0
#     LEQ = 1
#     EQ = 2
#     NEQ = 3
#     GREATER = 4
#     GEQ = 5
    
class StlComparisonOperator(Enum):
    LESS = 0
    LEQ = 1
    EQUAL = 2
    NEQ = 3
    GREATER = 4
    GEQ = 5

    def __str__(self):
        if self.value == 0:
            return '<'
        elif self.value == 1:
            return '<='
        elif self.value == 2:
            return '=='
        elif self.value == 3:
            return '!='
        elif self.value == 4:
            return '>'
        else:
            return '>='
        
class StlIOType(Enum):
    IN = 0
    OUT = 1
    UNDEFINED = 2
    
class Semantics(Enum):
    STANDARD = "standard"
    OUTPUT_ROBUSTNESS = "output-robustness"
    INPUT_VACUITY = "input-vacuity"
    INPUT_ROBUSTNESS = "input-robustness"
    OUTPUT_VACUITY = "output-vacuity"

    def __str__(self):
        return self.value

class Language(Enum):
    PYTHON = "python"
    CPP = "C++"
    def __str__(self):
        return self.value

class TimeInterpretation(Enum):
    DISCRETE = "discrete_time"
    DENSE = "dense-time"
    def __str__(self):
        return self.value

