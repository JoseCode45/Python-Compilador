# Generated from ExprParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#code.
    def visitCode(self, ctx:ExprParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#stat.
    def visitStat(self, ctx:ExprParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#query.
    def visitQuery(self, ctx:ExprParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#cond.
    def visitCond(self, ctx:ExprParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx:ExprParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#func.
    def visitFunc(self, ctx:ExprParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#params.
    def visitParams(self, ctx:ExprParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#func_call.
    def visitFunc_call(self, ctx:ExprParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#loop_for.
    def visitLoop_for(self, ctx:ExprParser.Loop_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#loop_while.
    def visitLoop_while(self, ctx:ExprParser.Loop_whileContext):
        return self.visitChildren(ctx)



del ExprParser