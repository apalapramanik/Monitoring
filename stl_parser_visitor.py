from decimal import Decimal
from fractions import Fraction
from stl_temporal_nodes import *
from antlr.stlParserVisitor import *
from node import *
from ltl_ast_visitor import LtlAstParserVisitor

class StlAstParserVisitor(LtlAstParserVisitor, stlParserVisitor):

    def __init__(self):
        stlParserVisitor.__init__(self)

    def visitExprAlways(self, ctx):
        child = self.visit(ctx.expression())        
        interval = self.visit(ctx.interval())
        node = TimedAlways(child, interval)
        return node


    def visitExprEv(self, ctx):
        child = self.visit(ctx.expression())        
        interval = self.visit(ctx.interval())
        node = TimedEventually(child, interval)
        return node

    def visitExpreOnce(self, ctx):
        child = self.visit(ctx.expression())        
        interval = self.visit(ctx.interval())
        node = TimedOnce(child, interval)
        return node

    def visitExprHist(self, ctx):
        child = self.visit(ctx.expression())        
        interval = self.visit(ctx.interval())
        node = TimedHistorically(child, interval)
        return node

    def visitExprSince(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))        
        interval = self.visit(ctx.interval())
        node = TimedSince(child1, child2, interval)
        return node

    def visitExprUntil(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        interval = self.visit(ctx.interval())
        node = TimedUntil(child1, child2, interval)
        return node

    def visitExprUnless(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        interval = self.visit(ctx.interval())
        
        interval_left = Interval(0, interval.end, interval.begin_unit, interval.end_unit)
        left = TimedAlways(child1, interval_left)
        right = TimedUntil(child1, child2, interval)
        node = Disjunction(left, right)
        return node

    def visitConstantTimeLiteral(self, ctx):
        const_name = ctx.Identifier().getText()

        val = self.const_val_dict[const_name]

        out = Fraction(Decimal(val))

        if ctx.unit() is None:
            unit = 'default'
        else:
            unit = ctx.unit().getText()

        return out, unit


    def visitIntervalTimeLiteral(self, ctx):
        time_bound = Fraction(Decimal(ctx.literal().getText()))
        if ctx.unit() is None:
            unit = ''
        else:
            unit = ctx.unit().getText()

        return time_bound, unit


    def visitInterval(self, ctx):
        begin, begin_unit = self.visit(ctx.intervalTime(0))
        end, end_unit = self.visit(ctx.intervalTime(1))
        interval = Interval(begin, end, begin_unit, end_unit)
        return interval

    def get_sampling_period(self):
        return self.sampling_period * self.U[self.sampling_period_unit]

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit):
        self.__unit = unit