if "." in __name__:
    from .ExprParser import ExprParser
    from .ExprParserVisitor import ExprParserVisitor
else:
    from ExprParser import ExprParser
    from ExprParserVisitor import ExprParserVisitor

class Compiler(ExprParserVisitor):

    def __init__(self):
        super(Compiler, self).__init__()
        self.vars = {}
        return None
    
    # Paste here all methods in ExprParserVisitor.py file
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



del (ExprParser, ExprParserVisitor)
