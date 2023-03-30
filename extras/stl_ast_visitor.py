
from stl_temporal_nodes import *
from exception import MonException


class StlAstVisitor():

    def visit(self, node, *args, **kwargs):
        if isinstance(node, TimedUntil):
            result = self.visitTimedUntil(node, *args, **kwargs)
        elif isinstance(node, TimedAlways):
            result = self.visitTimedAlways(node, *args, **kwargs)
        elif isinstance(node, TimedEventually):
            result = self.visitTimedEventually(node, *args, **kwargs)
        elif isinstance(node, TimedSince):
            result = self.visitTimedSince(node, *args, **kwargs)
        elif isinstance(node, TimedOnce):
            result = self.visitTimedOnce(node, *args, **kwargs)
        elif isinstance(node, TimedHistorically):
            result = self.visitTimedHistorically(node, *args, **kwargs)
        elif isinstance(node, TimedPrecedes):
            result = self.visitTimedPrecedes(node, *args, **kwargs)
        else:
            result = super(StlAstVisitor, self).visit(node, *args, **kwargs)

        return result

    def visitTimedPrecedes(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitTimedOnce(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitTimedHistorically(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitTimedSince(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitTimedPrecedes(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitTimedAlways(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitTimedEventually(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitTimedUntil(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def raise_exception(self, text):
        raise MonException(text)