# Generated from ExprParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,235,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,37,8,1,1,1,5,1,40,8,1,10,1,
        12,1,43,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,
        57,8,2,1,2,1,2,1,2,5,2,62,8,2,10,2,12,2,65,9,2,1,3,1,3,1,3,3,3,70,
        8,3,1,3,1,3,1,3,4,3,75,8,3,11,3,12,3,76,1,3,1,3,1,3,3,3,82,8,3,1,
        3,1,3,1,3,4,3,87,8,3,11,3,12,3,88,5,3,91,8,3,10,3,12,3,94,9,3,1,
        3,1,3,1,3,1,3,4,3,100,8,3,11,3,12,3,101,3,3,104,8,3,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,119,8,4,1,4,1,4,1,4,
        1,4,1,4,1,4,5,4,127,8,4,10,4,12,4,130,9,4,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,5,5,140,8,5,10,5,12,5,143,9,5,1,5,1,5,1,5,3,5,148,8,5,
        3,5,150,8,5,1,6,1,6,1,6,5,6,155,8,6,10,6,12,6,158,9,6,1,6,1,6,3,
        6,162,8,6,1,6,1,6,1,6,5,6,167,8,6,10,6,12,6,170,9,6,1,6,1,6,3,6,
        174,8,6,3,6,176,8,6,1,7,1,7,1,7,1,7,1,7,5,7,183,8,7,10,7,12,7,186,
        9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,3,8,206,8,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,5,9,215,8,9,
        10,9,12,9,218,9,9,1,9,5,9,221,8,9,10,9,12,9,224,9,9,3,9,226,8,9,
        1,9,1,9,5,9,230,8,9,10,9,12,9,233,9,9,1,9,0,2,4,8,10,0,2,4,6,8,10,
        12,14,16,18,0,3,2,0,5,5,26,27,2,0,6,7,28,28,2,0,9,9,12,12,269,0,
        23,1,0,0,0,2,36,1,0,0,0,4,56,1,0,0,0,6,66,1,0,0,0,8,118,1,0,0,0,
        10,131,1,0,0,0,12,175,1,0,0,0,14,177,1,0,0,0,16,189,1,0,0,0,18,212,
        1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,
        23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,27,5,0,0,1,27,1,1,0,
        0,0,28,37,3,8,4,0,29,37,3,4,2,0,30,37,3,6,3,0,31,37,3,14,7,0,32,
        37,3,10,5,0,33,37,3,18,9,0,34,37,3,16,8,0,35,37,5,22,0,0,36,28,1,
        0,0,0,36,29,1,0,0,0,36,30,1,0,0,0,36,31,1,0,0,0,36,32,1,0,0,0,36,
        33,1,0,0,0,36,34,1,0,0,0,36,35,1,0,0,0,37,41,1,0,0,0,38,40,5,3,0,
        0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,3,1,
        0,0,0,43,41,1,0,0,0,44,45,6,2,-1,0,45,57,5,25,0,0,46,47,5,2,0,0,
        47,57,3,4,2,3,48,49,5,15,0,0,49,50,3,4,2,0,50,51,5,16,0,0,51,57,
        1,0,0,0,52,53,3,8,4,0,53,54,7,0,0,0,54,55,3,8,4,0,55,57,1,0,0,0,
        56,44,1,0,0,0,56,46,1,0,0,0,56,48,1,0,0,0,56,52,1,0,0,0,57,63,1,
        0,0,0,58,59,10,4,0,0,59,60,5,1,0,0,60,62,3,4,2,5,61,58,1,0,0,0,62,
        65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,5,1,0,0,0,65,63,1,0,0,
        0,66,69,5,20,0,0,67,70,3,4,2,0,68,70,3,8,4,0,69,67,1,0,0,0,69,68,
        1,0,0,0,70,71,1,0,0,0,71,72,5,17,0,0,72,74,5,3,0,0,73,75,3,2,1,0,
        74,73,1,0,0,0,75,76,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,92,1,
        0,0,0,78,81,5,23,0,0,79,82,3,4,2,0,80,82,3,8,4,0,81,79,1,0,0,0,81,
        80,1,0,0,0,82,83,1,0,0,0,83,84,5,17,0,0,84,86,5,3,0,0,85,87,3,2,
        1,0,86,85,1,0,0,0,87,88,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,91,
        1,0,0,0,90,78,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,
        93,103,1,0,0,0,94,92,1,0,0,0,95,96,5,21,0,0,96,97,5,17,0,0,97,99,
        5,3,0,0,98,100,3,2,1,0,99,98,1,0,0,0,100,101,1,0,0,0,101,99,1,0,
        0,0,101,102,1,0,0,0,102,104,1,0,0,0,103,95,1,0,0,0,103,104,1,0,0,
        0,104,7,1,0,0,0,105,106,6,4,-1,0,106,119,5,35,0,0,107,119,5,30,0,
        0,108,119,5,31,0,0,109,119,5,29,0,0,110,111,5,35,0,0,111,112,5,4,
        0,0,112,119,3,8,4,3,113,114,5,15,0,0,114,115,3,8,4,0,115,116,5,16,
        0,0,116,119,1,0,0,0,117,119,3,14,7,0,118,105,1,0,0,0,118,107,1,0,
        0,0,118,108,1,0,0,0,118,109,1,0,0,0,118,110,1,0,0,0,118,113,1,0,
        0,0,118,117,1,0,0,0,119,128,1,0,0,0,120,121,10,5,0,0,121,122,7,1,
        0,0,122,127,3,8,4,6,123,124,10,4,0,0,124,125,7,2,0,0,125,127,3,8,
        4,5,126,120,1,0,0,0,126,123,1,0,0,0,127,130,1,0,0,0,128,126,1,0,
        0,0,128,129,1,0,0,0,129,9,1,0,0,0,130,128,1,0,0,0,131,132,5,13,0,
        0,132,133,5,35,0,0,133,134,5,15,0,0,134,135,3,12,6,0,135,136,5,16,
        0,0,136,137,5,17,0,0,137,141,5,3,0,0,138,140,3,2,1,0,139,138,1,0,
        0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,149,1,0,
        0,0,143,141,1,0,0,0,144,145,5,14,0,0,145,147,3,8,4,0,146,148,5,3,
        0,0,147,146,1,0,0,0,147,148,1,0,0,0,148,150,1,0,0,0,149,144,1,0,
        0,0,149,150,1,0,0,0,150,11,1,0,0,0,151,152,5,35,0,0,152,156,5,18,
        0,0,153,155,5,35,0,0,154,153,1,0,0,0,155,158,1,0,0,0,156,154,1,0,
        0,0,156,157,1,0,0,0,157,162,1,0,0,0,158,156,1,0,0,0,159,162,5,35,
        0,0,160,162,5,19,0,0,161,151,1,0,0,0,161,159,1,0,0,0,161,160,1,0,
        0,0,162,176,1,0,0,0,163,164,3,8,4,0,164,168,5,18,0,0,165,167,3,8,
        4,0,166,165,1,0,0,0,167,170,1,0,0,0,168,166,1,0,0,0,168,169,1,0,
        0,0,169,174,1,0,0,0,170,168,1,0,0,0,171,174,3,8,4,0,172,174,5,19,
        0,0,173,163,1,0,0,0,173,171,1,0,0,0,173,172,1,0,0,0,174,176,1,0,
        0,0,175,161,1,0,0,0,175,173,1,0,0,0,176,13,1,0,0,0,177,178,5,35,
        0,0,178,179,5,15,0,0,179,184,3,8,4,0,180,181,5,18,0,0,181,183,3,
        8,4,0,182,180,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,184,185,1,
        0,0,0,185,187,1,0,0,0,186,184,1,0,0,0,187,188,5,16,0,0,188,15,1,
        0,0,0,189,190,5,33,0,0,190,191,5,35,0,0,191,192,5,34,0,0,192,193,
        5,32,0,0,193,205,5,15,0,0,194,206,3,8,4,0,195,196,3,8,4,0,196,197,
        5,18,0,0,197,198,3,8,4,0,198,206,1,0,0,0,199,200,3,8,4,0,200,201,
        5,18,0,0,201,202,3,8,4,0,202,203,5,18,0,0,203,204,3,8,4,0,204,206,
        1,0,0,0,205,194,1,0,0,0,205,195,1,0,0,0,205,199,1,0,0,0,206,207,
        1,0,0,0,207,208,5,16,0,0,208,209,5,17,0,0,209,210,5,3,0,0,210,211,
        3,8,4,0,211,17,1,0,0,0,212,225,5,24,0,0,213,215,3,8,4,0,214,213,
        1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,226,
        1,0,0,0,218,216,1,0,0,0,219,221,3,4,2,0,220,219,1,0,0,0,221,224,
        1,0,0,0,222,220,1,0,0,0,222,223,1,0,0,0,223,226,1,0,0,0,224,222,
        1,0,0,0,225,216,1,0,0,0,225,222,1,0,0,0,226,227,1,0,0,0,227,231,
        5,17,0,0,228,230,3,2,1,0,229,228,1,0,0,0,230,233,1,0,0,0,231,229,
        1,0,0,0,231,232,1,0,0,0,232,19,1,0,0,0,233,231,1,0,0,0,29,23,36,
        41,56,63,69,76,81,88,92,101,103,118,126,128,141,147,149,156,161,
        168,173,175,184,205,216,222,225,231
    ]

class ExprParser ( Parser ):

    grammarFileName = "ExprParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'not'", "'\\n'", "'='", 
                     "'=='", "'*'", "'**'", "';'", "'+'", "'.'", "'J'", 
                     "'-'", "'def'", "'return'", "'('", "')'", "':'", "','", 
                     "'None'", "'if'", "'else'", "'pass'", "<INVALID>", 
                     "'while'", "<INVALID>", "'>'", "'<'", "'/'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'range'", "'for'", "'in'" ]

    symbolicNames = [ "<INVALID>", "OP_BOOL", "NOT", "BL", "EQ", "EQ2", 
                      "MUL", "POT", "SEMI", "PLUS", "DOT", "J", "MINUS", 
                      "DEF", "RETURN", "B_PARATENSIS", "C_PARATENSIS", "COLON", 
                      "COMMA", "NONE", "IF", "ELSE", "PASS", "ELIF", "WHILE", 
                      "BOOL", "GREATER", "LESSER", "DIVIDE", "COMPLEX", 
                      "INT", "FLOAT", "RANGE", "FOR", "IN", "ID", "WS" ]

    RULE_code = 0
    RULE_stat = 1
    RULE_query = 2
    RULE_cond = 3
    RULE_expr = 4
    RULE_func = 5
    RULE_params = 6
    RULE_func_call = 7
    RULE_loop_for = 8
    RULE_loop_while = 9

    ruleNames =  [ "code", "stat", "query", "cond", "expr", "func", "params", 
                   "func_call", "loop_for", "loop_while" ]

    EOF = Token.EOF
    OP_BOOL=1
    NOT=2
    BL=3
    EQ=4
    EQ2=5
    MUL=6
    POT=7
    SEMI=8
    PLUS=9
    DOT=10
    J=11
    MINUS=12
    DEF=13
    RETURN=14
    B_PARATENSIS=15
    C_PARATENSIS=16
    COLON=17
    COMMA=18
    NONE=19
    IF=20
    ELSE=21
    PASS=22
    ELIF=23
    WHILE=24
    BOOL=25
    GREATER=26
    LESSER=27
    DIVIDE=28
    COMPLEX=29
    INT=30
    FLOAT=31
    RANGE=32
    FOR=33
    IN=34
    ID=35
    WS=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_code

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode" ):
                return visitor.visitCode(self)
            else:
                return visitor.visitChildren(self)




    def code(self):

        localctx = ExprParser.CodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_code)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 46763384836) != 0):
                self.state = 20
                self.stat()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def query(self):
            return self.getTypedRuleContext(ExprParser.QueryContext,0)


        def cond(self):
            return self.getTypedRuleContext(ExprParser.CondContext,0)


        def func_call(self):
            return self.getTypedRuleContext(ExprParser.Func_callContext,0)


        def func(self):
            return self.getTypedRuleContext(ExprParser.FuncContext,0)


        def loop_while(self):
            return self.getTypedRuleContext(ExprParser.Loop_whileContext,0)


        def loop_for(self):
            return self.getTypedRuleContext(ExprParser.Loop_forContext,0)


        def PASS(self):
            return self.getToken(ExprParser.PASS, 0)

        def BL(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.BL)
            else:
                return self.getToken(ExprParser.BL, i)

        def getRuleIndex(self):
            return ExprParser.RULE_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = ExprParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 28
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 29
                self.query(0)
                pass

            elif la_ == 3:
                self.state = 30
                self.cond()
                pass

            elif la_ == 4:
                self.state = 31
                self.func_call()
                pass

            elif la_ == 5:
                self.state = 32
                self.func()
                pass

            elif la_ == 6:
                self.state = 33
                self.loop_while()
                pass

            elif la_ == 7:
                self.state = 34
                self.loop_for()
                pass

            elif la_ == 8:
                self.state = 35
                self.match(ExprParser.PASS)
                pass


            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 38
                    self.match(ExprParser.BL) 
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ExprParser.BOOL, 0)

        def NOT(self):
            return self.getToken(ExprParser.NOT, 0)

        def query(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.QueryContext)
            else:
                return self.getTypedRuleContext(ExprParser.QueryContext,i)


        def B_PARATENSIS(self):
            return self.getToken(ExprParser.B_PARATENSIS, 0)

        def C_PARATENSIS(self):
            return self.getToken(ExprParser.C_PARATENSIS, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def LESSER(self):
            return self.getToken(ExprParser.LESSER, 0)

        def GREATER(self):
            return self.getToken(ExprParser.GREATER, 0)

        def EQ2(self):
            return self.getToken(ExprParser.EQ2, 0)

        def OP_BOOL(self):
            return self.getToken(ExprParser.OP_BOOL, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_query

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)



    def query(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.QueryContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_query, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 45
                self.match(ExprParser.BOOL)
                pass

            elif la_ == 2:
                self.state = 46
                self.match(ExprParser.NOT)
                self.state = 47
                self.query(3)
                pass

            elif la_ == 3:
                self.state = 48
                self.match(ExprParser.B_PARATENSIS)
                self.state = 49
                self.query(0)
                self.state = 50
                self.match(ExprParser.C_PARATENSIS)
                pass

            elif la_ == 4:
                self.state = 52
                self.expr(0)
                self.state = 53
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 201326624) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 54
                self.expr(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.QueryContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_query)
                    self.state = 58
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 59
                    self.match(ExprParser.OP_BOOL)
                    self.state = 60
                    self.query(5) 
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COLON)
            else:
                return self.getToken(ExprParser.COLON, i)

        def BL(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.BL)
            else:
                return self.getToken(ExprParser.BL, i)

        def query(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.QueryContext)
            else:
                return self.getTypedRuleContext(ExprParser.QueryContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ELIF)
            else:
                return self.getToken(ExprParser.ELIF, i)

        def ELSE(self):
            return self.getToken(ExprParser.ELSE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_cond

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond" ):
                return visitor.visitCond(self)
            else:
                return visitor.visitChildren(self)




    def cond(self):

        localctx = ExprParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ExprParser.IF)
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 67
                self.query(0)
                pass

            elif la_ == 2:
                self.state = 68
                self.expr(0)
                pass


            self.state = 71
            self.match(ExprParser.COLON)
            self.state = 72
            self.match(ExprParser.BL)
            self.state = 74 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 73
                    self.stat()

                else:
                    raise NoViableAltException(self)
                self.state = 76 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 92
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 78
                    self.match(ExprParser.ELIF)
                    self.state = 81
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        self.state = 79
                        self.query(0)
                        pass

                    elif la_ == 2:
                        self.state = 80
                        self.expr(0)
                        pass


                    self.state = 83
                    self.match(ExprParser.COLON)
                    self.state = 84
                    self.match(ExprParser.BL)
                    self.state = 86 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 85
                            self.stat()

                        else:
                            raise NoViableAltException(self)
                        self.state = 88 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
             
                self.state = 94
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 95
                self.match(ExprParser.ELSE)
                self.state = 96
                self.match(ExprParser.COLON)
                self.state = 97
                self.match(ExprParser.BL)
                self.state = 99 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 98
                        self.stat()

                    else:
                        raise NoViableAltException(self)
                    self.state = 101 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def FLOAT(self):
            return self.getToken(ExprParser.FLOAT, 0)

        def COMPLEX(self):
            return self.getToken(ExprParser.COMPLEX, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def B_PARATENSIS(self):
            return self.getToken(ExprParser.B_PARATENSIS, 0)

        def C_PARATENSIS(self):
            return self.getToken(ExprParser.C_PARATENSIS, 0)

        def func_call(self):
            return self.getTypedRuleContext(ExprParser.Func_callContext,0)


        def MUL(self):
            return self.getToken(ExprParser.MUL, 0)

        def DIVIDE(self):
            return self.getToken(ExprParser.DIVIDE, 0)

        def POT(self):
            return self.getToken(ExprParser.POT, 0)

        def PLUS(self):
            return self.getToken(ExprParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ExprParser.MINUS, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 106
                self.match(ExprParser.ID)
                pass

            elif la_ == 2:
                self.state = 107
                self.match(ExprParser.INT)
                pass

            elif la_ == 3:
                self.state = 108
                self.match(ExprParser.FLOAT)
                pass

            elif la_ == 4:
                self.state = 109
                self.match(ExprParser.COMPLEX)
                pass

            elif la_ == 5:
                self.state = 110
                self.match(ExprParser.ID)

                self.state = 111
                self.match(ExprParser.EQ)
                self.state = 112
                self.expr(3)
                pass

            elif la_ == 6:
                self.state = 113
                self.match(ExprParser.B_PARATENSIS)
                self.state = 114
                self.expr(0)
                self.state = 115
                self.match(ExprParser.C_PARATENSIS)
                pass

            elif la_ == 7:
                self.state = 117
                self.func_call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 128
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 126
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 120
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 121
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 268435648) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 122
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 123
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 124
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==12):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 125
                        self.expr(5)
                        pass

             
                self.state = 130
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(ExprParser.DEF, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def B_PARATENSIS(self):
            return self.getToken(ExprParser.B_PARATENSIS, 0)

        def params(self):
            return self.getTypedRuleContext(ExprParser.ParamsContext,0)


        def C_PARATENSIS(self):
            return self.getToken(ExprParser.C_PARATENSIS, 0)

        def COLON(self):
            return self.getToken(ExprParser.COLON, 0)

        def BL(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.BL)
            else:
                return self.getToken(ExprParser.BL, i)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatContext,i)


        def RETURN(self):
            return self.getToken(ExprParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = ExprParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(ExprParser.DEF)
            self.state = 132
            self.match(ExprParser.ID)
            self.state = 133
            self.match(ExprParser.B_PARATENSIS)
            self.state = 134
            self.params()
            self.state = 135
            self.match(ExprParser.C_PARATENSIS)
            self.state = 136
            self.match(ExprParser.COLON)
            self.state = 137
            self.match(ExprParser.BL)
            self.state = 141
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 138
                    self.stat() 
                self.state = 143
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 144
                self.match(ExprParser.RETURN)
                self.state = 145
                self.expr(0)
                self.state = 147
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 146
                    self.match(ExprParser.BL)




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def COMMA(self):
            return self.getToken(ExprParser.COMMA, 0)

        def NONE(self):
            return self.getToken(ExprParser.NONE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = ExprParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 151
                    self.match(ExprParser.ID)
                    self.state = 152
                    self.match(ExprParser.COMMA)
                    self.state = 156
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==35:
                        self.state = 153
                        self.match(ExprParser.ID)
                        self.state = 158
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass

                elif la_ == 2:
                    self.state = 159
                    self.match(ExprParser.ID)
                    pass

                elif la_ == 3:
                    self.state = 160
                    self.match(ExprParser.NONE)
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 163
                    self.expr(0)
                    self.state = 164
                    self.match(ExprParser.COMMA)
                    self.state = 168
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 38117867520) != 0):
                        self.state = 165
                        self.expr(0)
                        self.state = 170
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass

                elif la_ == 2:
                    self.state = 171
                    self.expr(0)
                    pass

                elif la_ == 3:
                    self.state = 172
                    self.match(ExprParser.NONE)
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def B_PARATENSIS(self):
            return self.getToken(ExprParser.B_PARATENSIS, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def C_PARATENSIS(self):
            return self.getToken(ExprParser.C_PARATENSIS, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = ExprParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(ExprParser.ID)
            self.state = 178
            self.match(ExprParser.B_PARATENSIS)
            self.state = 179
            self.expr(0)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 180
                self.match(ExprParser.COMMA)
                self.state = 181
                self.expr(0)
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 187
            self.match(ExprParser.C_PARATENSIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ExprParser.FOR, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def IN(self):
            return self.getToken(ExprParser.IN, 0)

        def RANGE(self):
            return self.getToken(ExprParser.RANGE, 0)

        def B_PARATENSIS(self):
            return self.getToken(ExprParser.B_PARATENSIS, 0)

        def C_PARATENSIS(self):
            return self.getToken(ExprParser.C_PARATENSIS, 0)

        def COLON(self):
            return self.getToken(ExprParser.COLON, 0)

        def BL(self):
            return self.getToken(ExprParser.BL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_loop_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_for" ):
                return visitor.visitLoop_for(self)
            else:
                return visitor.visitChildren(self)




    def loop_for(self):

        localctx = ExprParser.Loop_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_loop_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(ExprParser.FOR)
            self.state = 190
            self.match(ExprParser.ID)
            self.state = 191
            self.match(ExprParser.IN)
            self.state = 192
            self.match(ExprParser.RANGE)
            self.state = 193
            self.match(ExprParser.B_PARATENSIS)
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 194
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 195
                self.expr(0)
                self.state = 196
                self.match(ExprParser.COMMA)
                self.state = 197
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 199
                self.expr(0)
                self.state = 200
                self.match(ExprParser.COMMA)
                self.state = 201
                self.expr(0)
                self.state = 202
                self.match(ExprParser.COMMA)
                self.state = 203
                self.expr(0)
                pass


            self.state = 207
            self.match(ExprParser.C_PARATENSIS)
            self.state = 208
            self.match(ExprParser.COLON)
            self.state = 209
            self.match(ExprParser.BL)
            self.state = 210
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_whileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(ExprParser.WHILE, 0)

        def COLON(self):
            return self.getToken(ExprParser.COLON, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def query(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.QueryContext)
            else:
                return self.getTypedRuleContext(ExprParser.QueryContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_loop_while

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_while" ):
                return visitor.visitLoop_while(self)
            else:
                return visitor.visitChildren(self)




    def loop_while(self):

        localctx = ExprParser.Loop_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_loop_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(ExprParser.WHILE)
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 38117867520) != 0):
                    self.state = 213
                    self.expr(0)
                    self.state = 218
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 38151421956) != 0):
                    self.state = 219
                    self.query(0)
                    self.state = 224
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


            self.state = 227
            self.match(ExprParser.COLON)
            self.state = 231
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 228
                    self.stat() 
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.query_sempred
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def query_sempred(self, localctx:QueryContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




