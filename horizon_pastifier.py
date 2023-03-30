

from stl_ast_visitor import StlAstVisitor
# from rtamt.pastifier.ltl.horizon import LtlHorizon
from stl_temporal_nodes import *

from exception import MonException


class StlHorizon(StlAstVisitor):

    def __init__(self):
        # LtlHorizon.__init__(self)
        pass

    def visit(self, node, *args, **kwargs):
        return StlAstVisitor.visit(self, node, *args, **kwargs)

    def visitTimedEventually(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)
        return op_horizon + node.end

    def visitTimedAlways(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)
        return op_horizon + node.end

    def visitTimedUntil(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)

        return max(op1_horizon, op2_horizon) + node.end

    def visitTimedOnce(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)
        return op_horizon

    def visitTimedHistorically(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)
        return op_horizon

    def visitTimedSince(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)
        return max(op1_horizon, op2_horizon)

    def visitTimedPrecedes(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)
        return max(op1_horizon, op2_horizon)

    def visitDefault(self, node):
        raise MonException('STL Pastifier: encountered unexpected type of node.')
    
##########################################################################################################

class StlPastifier(StlAstVisitor):

    def __init__(self):
        # LtlPastifier.__init__(self)
        pass

    def pastify(self, ast):
        h = StlHorizon()
        horizons = dict()
        for spec in ast.specs:
            horizon = h.visit(spec, None)
            horizons[spec] = horizon
        pastified_specs = []
        for spec in ast.specs:
            horizon = horizons[spec]
            pastified_spec = self.visit(spec, horizon)
            pastified_specs.append(pastified_spec)
        ast.specs = pastified_specs
        return ast

    def visit(self, node, *args, **kwargs):
        return StlAstVisitor.visit(self, node, *args, **kwargs)

    def visitVariable(self, node, *args, **kwargs):
        horizon = args[0]
        node = Variable(node.var, node.field, node.io_type)
        if horizon > 0:
            node = TimedOnce(node, Interval(horizon, horizon))
        return node

    def visitTimedEventually(self, node, *args, **kwargs):
        begin = node.begin
        end = node.end
        horizon = args[0] - end
        node = self.visit(node.children[0], horizon)
        if end - begin > 0:
            node = TimedOnce(node, Interval(0, end - begin))
        return node

    def visitTimedAlways(self, node, *args, **kwargs):
        begin = node.begin
        end = node.end
        horizon = args[0] - end
        node = self.visit(node.children[0], horizon)
        if end - begin > 0:
            node = TimedHistorically(node, Interval(0, end - begin))
        return node

    def visitTimedUntil(self, node, *args, **kwargs):
        begin = node.begin
        end = node.end
        horizon = args[0] - end
        child1_node = self.visit(node.children[0], horizon)
        child2_node = self.visit(node.children[1], horizon)
        node = TimedPrecedes(child1_node, child2_node, Interval(begin, end))
        return node

    def visitTimedOnce(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = TimedOnce(child_node, Interval(node.begin, node.end))
        return node

    def visitTimedHistorically(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = TimedHistorically(child_node, Interval(node.begin, node.end))
        return node

    def visitTimedSince(self, node, *args, **kwargs):
        child_node_1 = self.visit(node.children[0], *args, **kwargs)
        child_node_2 = self.visit(node.children[1], *args, **kwargs)
        node = TimedSince(child_node_1, child_node_2, Interval(node.begin, node.end))
        return node

    def visitTimedPrecedes(self, node, *args, **kwargs):
        end = node.end
        begin = node.begin
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = TimedPrecedes(child1_node, child2_node, Interval(begin, end))
        return node

    def visitDefault(self, node):
        raise MonException('STL Pastifier: encountered unexpected type of node.')