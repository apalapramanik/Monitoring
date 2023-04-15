#!/usr/bin/env python3

from interpreters import AbstractAstVisitor
from node import *
from exception import MonException

class LtlAstVisitor(AbstractAstVisitor):

    def visit(self, node, *args, **kwargs):
        if isinstance(node, Predicate):
            result = self.visitPredicate(node, *args, **kwargs)
        elif isinstance(node, Variable):
            result = self.visitVariable(node, *args, **kwargs)
        elif isinstance(node, Neg):
            result = self.visitNot(node, *args, **kwargs)
        elif isinstance(node, Disjunction):
            result = self.visitOr(node, *args, **kwargs)
        elif isinstance(node, Conjunction):
            result = self.visitAnd(node, *args, **kwargs)
        elif isinstance(node, Implies):
            result = self.visitImplies(node, *args, **kwargs)
        elif isinstance(node, Iff):
            result = self.visitIff(node, *args, **kwargs)
        elif isinstance(node, Xor):
            result = self.visitXor(node, *args, **kwargs)
        elif isinstance(node, Eventually):
            result = self.visitEventually(node, *args, **kwargs)
        elif isinstance(node, Always):
            result = self.visitAlways(node, *args, **kwargs)
        elif isinstance(node, Until):
            result = self.visitUntil(node, *args, **kwargs)
        elif isinstance(node, Once):
            result = self.visitOnce(node, *args, **kwargs)
        elif isinstance(node, Historically):
            result = self.visitHistorically(node, *args, **kwargs)
        elif isinstance(node, Since):
            result = self.visitSince(node, *args, **kwargs)
        elif isinstance(node, Abs):
            result = self.visitAbs(node, *args, **kwargs)
        elif isinstance(node, Sqrt):
            result = self.visitSqrt(node, *args, **kwargs)
        elif isinstance(node, Exp):
            result = self.visitExp(node, *args, **kwargs)
        elif isinstance(node, Pow):
            result = self.visitPow(node, *args, **kwargs)
        elif isinstance(node, Addition):
            result = self.visitAddition(node, *args, **kwargs)
        elif isinstance(node, Subtraction):
            result = self.visitSubtraction(node, *args, **kwargs)
        elif isinstance(node, Multiplication):
            result = self.visitMultiplication(node, *args, **kwargs)
        elif isinstance(node, Division):
            result = self.visitDivision(node, *args, **kwargs)
        elif isinstance(node, Rise):
            result = self.visitRise(node, *args, **kwargs)
        elif isinstance(node, Fall):
            result = self.visitFall(node, *args, **kwargs)
        elif isinstance(node, Constant):
            result = self.visitConstant(node, *args, **kwargs)
        elif isinstance(node, Previous):
            result = self.visitPrevious(node, *args, **kwargs)
        elif isinstance(node, Next):
            result = self.visitNext(node, *args, **kwargs)
        else:
            self.raise_exception('{} is not a TL operator'.format(node.__class__.__name__))
        return result

    def raise_exception(self, text):
        raise MonException(text)

    def visitPredicate(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitVariable(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitAbs(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitSqrt(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitPow(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitExp(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitAddition(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitSubtraction(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitMultiplication(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitDivision(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitNot(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitAnd(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitOr(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitImplies(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitIff(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitXor(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitEventually(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitAlways(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitUntil(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitOnce(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitHistorically(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitSince(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitRise(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitFall(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitConstant(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitPrevious(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitNext(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitDefault(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)
    
    
class LtlHorizon(LtlAstVisitor):

    def __init__(self):
        pass

    def visitConstant(self, node, *args, **kwargs):
        return 0

    def visitPredicate(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)

        return max(op1_horizon, op2_horizon)

    def visitVariable(self, node, *args, **kwargs):
        return 0

    def visitAddition(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)

        return max(op1_horizon, op2_horizon)

    def visitMultiplication(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)

        return max(op1_horizon, op2_horizon)

    def visitSubtraction(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)

        return max(op1_horizon, op2_horizon)

    def visitDivision(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)

        return max(op1_horizon, op2_horizon)

    def visitAbs(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)

        return op_horizon

    def visitSqrt(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)

        return op_horizon

    def visitExp(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)

        return op_horizon

    def visitPow(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)

        return max(op1_horizon, op2_horizon)

    def visitRise(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)

        return op_horizon

    def visitFall(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)

        return op_horizon

    def visitNot(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)

        return op_horizon

    def visitAnd(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)

        return max(op1_horizon, op2_horizon)

    def visitOr(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)

        return max(op1_horizon, op2_horizon)

    def visitImplies(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)

        return max(op1_horizon, op2_horizon)

    def visitIff(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)

        return max(op1_horizon, op2_horizon)

    def visitXor(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)

        return max(op1_horizon, op2_horizon)

    def visitEventually(self, node, *args, **kwargs):
        raise MonException('Cannot pastify an unbounded eventually.')

    def visitAlways(self, node, *args, **kwargs):
        raise MonException('Cannot pastify an unbounded always.')

    def visitUntil(self, node, *args, **kwargs):
        raise MonException('Cannot pastify an unbounded until.')

    def visitOnce(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)

        return op_horizon

    def visitPrevious(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)

        return op_horizon

    def visitNext(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)

        return op_horizon

    def visitHistorically(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)

        return op_horizon

    def visitSince(self, node, *args, **kwargs):
        op1_horizon = self.visit(node.children[0], *args, **kwargs)
        op2_horizon = self.visit(node.children[1], *args, **kwargs)

        return max(op1_horizon, op2_horizon)

    def visitDefault(self, node):
        raise MonException('LTL Pastifier: encountered unexpected type of object.')

class LtlPastifier(LtlAstVisitor):

    def __init__(self):
        pass

    def pastify(self, ast):
        h = LtlHorizon()
        horizons = dict()
        for spec in ast.specs:
            horizon = h.visit(spec, None)
            horizons[spec] = horizon
        pastified_specs = []
        for spec in ast.specs:
            horizon = horizons[spec]
            pastified_spec = self.visit(spec, [horizon])
            pastified_specs.append(pastified_spec)
        return pastified_specs

    def visitConstant(self, node, *args, **kwargs):
        node = Constant(node.val)
        return node

    def visitPredicate(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Predicate(child1_node, child2_node, node.operator)
        return node

    def visitVariable(self, node, *args, **kwargs):
        horizon = args[0]
        node = Variable(node.var, node.field, node.io_type)
        for i in range(horizon):
            node = Previous(node)
        return node

    def visitAddition(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Addition(child1_node, child2_node)
        return node

    def visitMultiplication(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Multiplication(child1_node, child2_node)
        return node

    def visitSubtraction(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Subtraction(child1_node, child2_node)
        return node

    def visitDivision(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Division(child1_node, child2_node)
        return node

    def visitAbs(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = Abs(child_node)
        return node

    def visitSqrt(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = Sqrt(child_node)
        return node

    def visitExp(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = Exp(child_node)
        return node

    def visitPow(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Pow(child1_node, child2_node)
        return node

    def visitRise(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = Rise(child_node)
        return node

    def visitFall(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = Fall(child_node)
        return node

    def visitNot(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = Neg(child_node)
        return node

    def visitAnd(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Conjunction(child1_node, child2_node)
        return node

    def visitOr(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Disjunction(child1_node, child2_node)
        return node

    def visitImplies(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Implies(child1_node, child2_node)
        return node

    def visitIff(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Iff(child1_node, child2_node)
        return node

    def visitXor(self, node, *args, **kwargs):
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = Xor(child1_node, child2_node)
        return node

    def visitEventually(self, node, *args, **kwargs):
        raise MonException('Cannot pastify an unbounded eventually.')

    def visitAlways(self, node, *args, **kwargs):
        raise MonException('Cannot pastify an unbounded always.')

    def visitUntil(self, node, *args, **kwargs):
        raise MonException('Cannot pastify an unbounded until.')

    def visitOnce(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = Once(child_node)
        return node

    def visitPrevious(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = Previous(child_node)
        return node

    def visitNext(self, node, *args, **kwargs):
        horizon = args[0] - 1
        child_node = self.visit(node.children[0], horizon)
        return child_node

    def visitHistorically(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = Historically(child_node)
        return node

    def visitSince(self, node, *args, **kwargs):
        child_node_1 = self.visit(node.children[0], *args, **kwargs)
        child_node_2 = self.visit(node.children[1], *args, **kwargs)
        node = Since(child_node_1, child_node_2)
        return node

    def visitDefault(self, node):
        raise MonException('LTL Pastifier: encountered unexpected type of object.')
