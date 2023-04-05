from node import *
from interpreters import AbstractAstVisitor
from discrete_operators import *
import logging
import operator
from antlr.ltlParserVisitor import ltlParserVisitor
from antlr4 import *
from enumerations import *


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
    
    
    
class LtlAstParserVisitor(ltlParserVisitor):

    def visitExprPredicate(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        op_type = self.str_to_op_type(ctx.comparisonOp().getText())
        node = Predicate(child1, child2, op_type)

        return node

    def visitExprId(self, ctx):
        id = ctx.Identifier().getText();

        # Identifier is a constant
        if id in self.const_val_dict:
            val = self.const_val_dict[id]
            node = Constant(float(val))
        # Identifier is either an input variable or a sub-formula
        elif id in self.var_subspec_dict:
                node = self.var_subspec_dict[id]
                return node
        else:
            id_tokens = id.split('.')
            id_head = id_tokens[0]
            id_tokens.pop(0)
            id_tail = '.'.join(id_tokens)

            try:
                var = self.create_var_from_name(id_head)
                if (not id_tail):
                    if (not isinstance(var, (int, float))):
                        raise MonException('Variable {} is not of type int or float'.format(id))
                else:
                    try:
                        value = operator.attrgetter(id_tail)(var)
                        if (not isinstance(value, (int, float))):
                            raise MonException(
                                'The field {0} of the variable {1} is not of type int or float'.format(id, id_head))
                    except AttributeError as err:
                        raise MonException(err)
            except KeyError:
                if id_tail:
                    raise MonException('{0} refers to undeclared variable {1} of unknown type'.format(id, id_head))
                else:
                    var = float()
                    self.var_object_dict[id] = var
                    self.add_var(id)
                    logging.warning('The variable {} is not explicitely declared. It is implicitely declared as a '
                                'variable of type float'.format(id))

            var_io = self.var_io_dict[id_head]
            node = Variable(id_head, id_tail, var_io)

        return node


    def visitVariableDeclaration(self, ctx):
        # fetch the variable name, type and io signature
        var_name = ctx.Identifier().getText()
        var_type = ctx.domainType().getText()

        self.declare_var(var_name, var_type)
        self.var_io_dict[var_name] = 'output'

        # If 'var' is input, add to the set of input vars
        # If 'var' is output, add to the set of output vars
        if (not ctx.ioType() is None):
            if (not ctx.ioType().Input() is None):
                var_iotype = 'input'
            elif (not ctx.ioType().Output() is None):
                var_iotype = 'output'
        self.set_var_io_type(var_name, var_iotype)

        self.visitChildren(ctx)

    def visitConstantDeclaration(self, ctx):
        # fetch the variable name, type and io signature
        const_name = ctx.identifier().getText()
        const_type = ctx.domainType().getText()
        const_value = ctx.literal().getText()

        self.declare_const(const_name, const_type, const_value)

        self.visitChildren(ctx)

    def visitRosTopic(self, ctx):
        var_name = ctx.Identifier(0).getText()
        topic_name = ctx.Identifier(1).getText()
        self.set_var_topic(var_name, topic_name)

    def visitModImport(self, ctx):
        module_name = ctx.Identifier(0).getText()
        var_type = ctx.Identifier(1).getText()
        self.import_module(module_name, var_type)

    def visitExprAddition(self, ctx):
        child1 = self.visit(ctx.real_expression(0))
        child2 = self.visit(ctx.real_expression(1))
        node = Addition(child1, child2)
        return node

    def visitExprSubtraction(self, ctx):
        child1 = self.visit(ctx.real_expression(0))
        child2 = self.visit(ctx.real_expression(1))
        node = Subtraction(child1, child2)
        return node

    def visitExprMultiplication(self, ctx):
        child1 = self.visit(ctx.real_expression(0))
        child2 = self.visit(ctx.real_expression(1))
        node = Multiplication(child1, child2)
        return node

    def visitExprDivision(self, ctx):
        child1 = self.visit(ctx.real_expression(0))
        child2 = self.visit(ctx.real_expression(1))
        node = Division(child1, child2)
        return node

    def visitExprAbs(self, ctx):
        child = self.visit(ctx.real_expression())
        node = Abs(child)
        return node

    def visitExprSqrt(self, ctx):
        child = self.visit(ctx.real_expression())
        node = Sqrt(child)
        return node

    def visitExprExp(self, ctx):
        child = self.visit(ctx.real_expression())
        node = Exp(child)
        return node

    def visitExprPow(self, ctx):
        child1 = self.visit(ctx.real_expression(0))
        child2 = self.visit(ctx.real_expression(1))
        node = Pow(child1, child2)
        return node

    def visitExprNot(self, ctx):
        child = self.visit(ctx.expression())
        node = Neg(child)
        return node

    def visitExprRise(self, ctx):
        child = self.visit(ctx.expression())
        node = Rise(child)
        return node

    def visitExprLiteral(self, ctx):
        val = float(ctx.literal().getText())
        node = Constant(val)
        return node

    def visitExprFall(self, ctx):
        child = self.visit(ctx.expression())
        node = Fall(child)
        return node

    def visitExprAnd(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        node = Conjunction(child1, child2)
        return node

    def visitExprOr(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        node = Disjunction(child1, child2)
        return node

    def visitExprImplies(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        node = Implies(child1, child2)
        return node

    def visitExprIff(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        node = Iff(child1, child2)
        return node

    def visitExprXor(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        node = Xor(child1, child2)
        return node

    def visitExprAlways(self, ctx):
        child = self.visit(ctx.expression())
        node = Always(child)
        return node

    def visitExprEv(self, ctx):
        child = self.visit(ctx.expression())
        node = Eventually(child)
        return node

    def visitExprPrevious(self, ctx):
        child = self.visit(ctx.expression())
        node = Previous(child)
        return node

    def visitExprNext(self, ctx):
        child = self.visit(ctx.expression())
        node = Next(child)
        return node

    def visitExpreOnce(self, ctx):
        child = self.visit(ctx.expression())
        node = Once(child)
        return node

    def visitExprHist(self, ctx):
        child = self.visit(ctx.expression())
        node = Historically(child)
        return node

    def visitExprSince(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        node = Since(child1, child2)
        return node

    def visitExprUntil(self, ctx):
        # Parse children
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))

        node = Until(child1, child2)
        return node

    def visitExprUnless(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        interval = self.visit(ctx.interval())

        left = Always(child1, 0, interval.end)
        right = Until(child1, child2)
        node = Disjunction(left, right)

        return node

    def visitExprParen(self, ctx):
        return self.visit(ctx.expression())

    def visitExpr(self, ctx):
        return self.visit(ctx.expression())

    def visitAssertion(self, ctx):
        out = self.visit(ctx.expression())

        implicit = False
        if not ctx.Identifier():
            id = 'out'
            implicit = True
        else:
            id = ctx.Identifier().getText();

        self.var_subspec_dict[id] = out
        id_tokens = id.split('.')
        id_head = id_tokens[0]
        id_tokens.pop(0)
        id_tail = '.'.join(id_tokens)

        try:
            var = self.var_object_dict[id_head]
            var = self.create_var_from_name(id_head)
            if (not id_tail):
                if (not isinstance(var, (int, float))):
                    raise MonException('Variable {} is not of type int or float'.format(id))
            else:
                try:
                    value = operator.attrgetter(id_tail)(var)
                    if (not isinstance(value, (int, float))):
                        raise MonException(
                            'The field {0} of the variable {1} is not of type int or float'.format(id, id_head))
                except AttributeError as err:
                    raise MonException(err)
        except KeyError:
            if id_tail:
                raise MonException('{0} refers to undeclared variable {1} of unknown type'.format(id, id_head))
            else:
                var = float()
                self.var_object_dict[id] = var
                self.add_var(id)
                if not implicit:
                    logging.warning('The variable {} is not explicitly declared. It is implicitly declared as a '
                                    'variable of type float'.format(id))

        self.out_var = id_head
        self.out_var_field = id_tail
        self.free_vars.discard(id_head)
        self.specs.append(out)
        return

    def visitSpecification_file(self, ctx):
        self.visit(ctx.specification())
        return

    def visitSpecification(self, ctx):
        self.visitChildren(ctx)
        try:
            del self.var_subspec_dict[self.out_var + self.out_var_field]
        except KeyError:
            pass
        return

    def visitSpecificationId(self, ctx):
        self.visitChildren(ctx)
        # The specification name is updated only if it is given
        # by the user
        if not ctx.Identifier() is None:
            self.name = ctx.Identifier().getText()

    def str_to_op_type(self, input):
        if input == "<":
            # return self.comp_op_mod.StlComparisonOperator.LESS
            return StlComparisonOperator.LESS
        elif input == '<=':
            return StlComparisonOperator.LEQ
        elif input == ">=":
            return StlComparisonOperator.GEQ
        elif input == ">":
            return StlComparisonOperator.GREATER
        elif input == "==":
            return StlComparisonOperator.EQUAL
        else:
            return StlComparisonOperator.NEQ