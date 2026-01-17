# Monitoring

A Signal Temporal Logic (STL) and Linear Temporal Logic (LTL) runtime monitoring framework for formal verification of system behaviors.

> **Note:** This repository is based on [RTAMT (Real-Time Analytic Monitoring Tool)](https://github.com/nickovic/rtamt) by Dejan Nickovic and Tomoya Yamaguchi. The original RTAMT library provides a comprehensive framework for runtime monitoring of STL and LTL specifications. This fork contains minor personal modifications for specific use cases.

## Overview

This framework allows you to:
- Define formal specifications using STL and LTL syntax
- Parse specifications into Abstract Syntax Trees (ASTs)
- Evaluate specifications against data streams in offline or online (streaming) mode
- Compute robustness metrics indicating how well a system satisfies specifications
- Integrate with ROS (Robot Operating System) for real-time robot behavior monitoring

## Features

- **Offline Monitoring** - Evaluate complete datasets and return final robustness values
- **Online Monitoring** - Real-time streaming evaluation as new data arrives
- **Robustness Analysis** - Quantitative satisfaction metrics (positive = satisfied, negative = violated)
- **ROS Integration** - Subscribe to topics and publish monitoring results
- **Pastification** - Convert future temporal formulas to equivalent past formulas
- **Multiple Semantics** - Standard, input/output robustness, and vacuity interpretations

## Supported Operators

### Temporal Operators
| Operator | Syntax | Description |
|----------|--------|-------------|
| Always | `always[a,b](φ)` | φ holds throughout interval [a,b] |
| Eventually | `eventually[a,b](φ)` | φ holds at some point in [a,b] |
| Until | `φ until[a,b] ψ` | φ holds until ψ becomes true |
| Since | `φ since[a,b] ψ` | Past version of until |
| Historically | `historically[a,b](φ)` | Past version of always |
| Once | `once[a,b](φ)` | Past version of eventually |

### Logical Operators
`and`, `or`, `not`, `implies`, `iff`, `xor`

### Comparison Operators
`<`, `<=`, `==`, `!=`, `>`, `>=`

### Arithmetic Operators
`+`, `-`, `*`, `/`, `abs()`, `sqrt()`, `exp()`, `pow()`

### Time Units
`s` (seconds), `ms` (milliseconds), `us` (microseconds), `ns` (nanoseconds)

## Installation

```bash
# Clone the repository
git clone https://github.com/apalapramanik/Monitoring.git
cd Monitoring

# Install ANTLR4 runtime
pip install antlr4-python3-runtime

# For ROS integration (optional)
# Ensure ROS is installed with rospy available
```

## Usage

### Basic Example

```python
from stl_specification import StlDiscreteTimeSpecification

# Create specification
spec = StlDiscreteTimeSpecification()
spec.declare_var('pred', 'float')
spec.declare_var('dist', 'float')
spec.spec = '(always[0,3](pred >= dist)) implies (eventually[3,5](pred < dist))'
spec.parse()

# Evaluate with data
prediction = [0.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0]
rob = spec.update(0, [('pred', prediction), ('dist', 2.0)])
print(f'Robustness: {rob}')
```

### ROS Integration

```bash
python ros.py --stl specs/spec.stl --period 1 --unit s
```

### Example Specification File (specs/spec.stl)

```stl
from testrobots.msg import FloatStamped
from testrobots.msg import ListStamped

input ListStamped pred1
@ topic(pred1, pred1_array)
input FloatStamped safe
@ topic(safe, safety)

output FloatStamped worker1
worker1.value = (always[0,2](pred1.data > safe.value)) implies (eventually[2,4](pred1.data < safe.value))
```

## Project Structure

```
Monitoring/
├── README.md
├── stl_specification.py         # Main STL specification entry point
├── abstract_specification.py    # Base specification classes
├── stl_specification_parser.py  # STL parser using ANTLR
├── ast_visitor.py               # AST visitor for STL
├── ltl_ast_visitor.py           # AST visitor for LTL
├── interpreters.py              # Offline/online interpreters
├── discrete_operators.py        # Online temporal operations
├── node.py                      # AST node classes
├── stl_temporal_nodes.py        # STL temporal node types
├── enumerations.py              # Operator and semantic enums
├── time_interpreter.py          # Discrete/dense time handling
├── horizon_pastifier.py         # Future-to-past formula conversion
├── ros.py                       # ROS integration
├── interval.py                  # Temporal interval representation
├── test.py                      # Example demonstrations
├── antlr/                       # ANTLR4 grammar and generated parsers
│   ├── stlLexer.g4              # STL lexer grammar
│   ├── stlParser.g4             # STL parser grammar
│   ├── ltlLexer.g4              # LTL lexer grammar
│   ├── ltlParser.g4             # LTL parser grammar
│   └── *.py                     # Generated parser files
├── specs/                       # Example specifications
│   └── spec.stl
└── extras/                      # Extended functionality
    ├── iastl.py                 # Input/output robust STL
    └── semantics_iastl.py       # Input-aware semantics
```

## Architecture

### Class Hierarchy

```
AbstractSpecification
├── AbstractOfflineSpecification
├── AbstractOnlineSpecification
└── AbstractOfflineOnlineSpecification

AbstractInterpreter
├── AbstractOfflineInterpreter
│   └── StlDiscreteTimeOfflineInterpreter
└── AbstractOnlineInterpreter
    └── StlDiscreteTimeOnlineInterpreter

AbstractNode
├── LeafNode (Predicate, Variable, Constant)
├── UnaryNode (Not, Always, Eventually, etc.)
└── BinaryNode (And, Or, Until, Since, etc.)
```

### Robustness Semantics

- **Positive values** indicate the specification is satisfied
- **Negative values** indicate violation
- **Magnitude** represents the degree of satisfaction/violation

## Use Cases

- **Robotics** - Monitor robot behavior against safety specifications
- **Autonomous Systems** - Verify autonomous vehicle properties
- **Cyber-Physical Systems** - Monitor systems with temporal constraints
- **Runtime Verification** - Real-time checking of temporal properties
- **Safety-Critical Systems** - Verify critical system behaviors

## Requirements

- Python 3.8+
- antlr4-python3-runtime
- rospy (optional, for ROS integration)

## Running Tests

```bash
python test.py
```

## Acknowledgments

This project is derived from **RTAMT (Real-Time Analytic Monitoring Tool)**, developed by Dejan Nickovic and Tomoya Yamaguchi. Full credit goes to the original authors for the core implementation.

- **Original Repository:** [https://github.com/nickovic/rtamt](https://github.com/nickovic/rtamt)
- **RTAMT Paper:** Nickovic, D., & Yamaguchi, T. (2020). *RTAMT: Online Robustness Monitors from STL*

If you use this work in academic research, please cite the original RTAMT project.

## References

- [RTAMT - Original Project](https://github.com/nickovic/rtamt)
- [Signal Temporal Logic](https://en.wikipedia.org/wiki/Signal_temporal_logic)
- [Linear Temporal Logic](https://en.wikipedia.org/wiki/Linear_temporal_logic)
- [ANTLR4](https://www.antlr.org/)
- [ROS - Robot Operating System](https://www.ros.org/)

## License

See the original [RTAMT repository](https://github.com/nickovic/rtamt) for license information.
