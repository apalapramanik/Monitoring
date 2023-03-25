# Generated from stlParser.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .stlParser import stlParser
else:
    from stlParser import stlParser

# This class defines a complete generic visitor for a parse tree produced by stlParser.

class stlParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by stlParser#specification_file.
    def visitSpecification_file(self, ctx:stlParser.Specification_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#specification.
    def visitSpecification(self, ctx:stlParser.SpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#SpecificationId.
    def visitSpecificationId(self, ctx:stlParser.SpecificationIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#modImport.
    def visitModImport(self, ctx:stlParser.ModImportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#assertion.
    def visitAssertion(self, ctx:stlParser.AssertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#declVariable.
    def visitDeclVariable(self, ctx:stlParser.DeclVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#declConstant.
    def visitDeclConstant(self, ctx:stlParser.DeclConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#annotation.
    def visitAnnotation(self, ctx:stlParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#rosTopic.
    def visitRosTopic(self, ctx:stlParser.RosTopicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:stlParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#constantDeclaration.
    def visitConstantDeclaration(self, ctx:stlParser.ConstantDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#AsgnLiteral.
    def visitAsgnLiteral(self, ctx:stlParser.AsgnLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#AsgnExpr.
    def visitAsgnExpr(self, ctx:stlParser.AsgnExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#domainType.
    def visitDomainType(self, ctx:stlParser.DomainTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ioType.
    def visitIoType(self, ctx:stlParser.IoTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprSubtraction.
    def visitExprSubtraction(self, ctx:stlParser.ExprSubtractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprPow.
    def visitExprPow(self, ctx:stlParser.ExprPowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprDivision.
    def visitExprDivision(self, ctx:stlParser.ExprDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprMultiplication.
    def visitExprMultiplication(self, ctx:stlParser.ExprMultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprLiteral.
    def visitExprLiteral(self, ctx:stlParser.ExprLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprExp.
    def visitExprExp(self, ctx:stlParser.ExprExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprSqrt.
    def visitExprSqrt(self, ctx:stlParser.ExprSqrtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprId.
    def visitExprId(self, ctx:stlParser.ExprIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprAbs.
    def visitExprAbs(self, ctx:stlParser.ExprAbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprAddition.
    def visitExprAddition(self, ctx:stlParser.ExprAdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#Leq.
    def visitLeq(self, ctx:stlParser.LeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#Geq.
    def visitGeq(self, ctx:stlParser.GeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#Less.
    def visitLess(self, ctx:stlParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#Greater.
    def visitGreater(self, ctx:stlParser.GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#Eq.
    def visitEq(self, ctx:stlParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#Neq.
    def visitNeq(self, ctx:stlParser.NeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#literal.
    def visitLiteral(self, ctx:stlParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#Id.
    def visitId(self, ctx:stlParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#interval.
    def visitInterval(self, ctx:stlParser.IntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#intervalTimeLiteral.
    def visitIntervalTimeLiteral(self, ctx:stlParser.IntervalTimeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#constantTimeLiteral.
    def visitConstantTimeLiteral(self, ctx:stlParser.ConstantTimeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#unit.
    def visitUnit(self, ctx:stlParser.UnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprSince.
    def visitExprSince(self, ctx:stlParser.ExprSinceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprParen.
    def visitExprParen(self, ctx:stlParser.ExprParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprIff.
    def visitExprIff(self, ctx:stlParser.ExprIffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExpreOnce.
    def visitExpreOnce(self, ctx:stlParser.ExpreOnceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprEv.
    def visitExprEv(self, ctx:stlParser.ExprEvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprImplies.
    def visitExprImplies(self, ctx:stlParser.ExprImpliesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprUntil.
    def visitExprUntil(self, ctx:stlParser.ExprUntilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprNot.
    def visitExprNot(self, ctx:stlParser.ExprNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprNext.
    def visitExprNext(self, ctx:stlParser.ExprNextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprAnd.
    def visitExprAnd(self, ctx:stlParser.ExprAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprUnless.
    def visitExprUnless(self, ctx:stlParser.ExprUnlessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprPrevious.
    def visitExprPrevious(self, ctx:stlParser.ExprPreviousContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprHist.
    def visitExprHist(self, ctx:stlParser.ExprHistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprFall.
    def visitExprFall(self, ctx:stlParser.ExprFallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprPredicate.
    def visitExprPredicate(self, ctx:stlParser.ExprPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprXor.
    def visitExprXor(self, ctx:stlParser.ExprXorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprRise.
    def visitExprRise(self, ctx:stlParser.ExprRiseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprOr.
    def visitExprOr(self, ctx:stlParser.ExprOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprAlways.
    def visitExprAlways(self, ctx:stlParser.ExprAlwaysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#ExprReal.
    def visitExprReal(self, ctx:stlParser.ExprRealContext):
        return self.visitChildren(ctx)



del stlParser