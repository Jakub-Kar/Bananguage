# Generated from C:/Users/admin/PycharmProjects/kompilatorki/Bananguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Bananguage import Bananguage
else:
    from Bananguage import Bananguage

# This class defines a complete listener for a parse tree produced by Bananguage.
class BananguageListener(ParseTreeListener):

    # Enter a parse tree produced by Bananguage#program.
    def enterProgram(self, ctx:Bananguage.ProgramContext):
        pass

    # Exit a parse tree produced by Bananguage#program.
    def exitProgram(self, ctx:Bananguage.ProgramContext):
        pass


    # Enter a parse tree produced by Bananguage#statement.
    def enterStatement(self, ctx:Bananguage.StatementContext):
        pass

    # Exit a parse tree produced by Bananguage#statement.
    def exitStatement(self, ctx:Bananguage.StatementContext):
        pass


    # Enter a parse tree produced by Bananguage#expr.
    def enterExpr(self, ctx:Bananguage.ExprContext):
        pass

    # Exit a parse tree produced by Bananguage#expr.
    def exitExpr(self, ctx:Bananguage.ExprContext):
        pass


    # Enter a parse tree produced by Bananguage#assignment.
    def enterAssignment(self, ctx:Bananguage.AssignmentContext):
        pass

    # Exit a parse tree produced by Bananguage#assignment.
    def exitAssignment(self, ctx:Bananguage.AssignmentContext):
        pass


    # Enter a parse tree produced by Bananguage#floatAssignment.
    def enterFloatAssignment(self, ctx:Bananguage.FloatAssignmentContext):
        pass

    # Exit a parse tree produced by Bananguage#floatAssignment.
    def exitFloatAssignment(self, ctx:Bananguage.FloatAssignmentContext):
        pass


    # Enter a parse tree produced by Bananguage#numAssignment.
    def enterNumAssignment(self, ctx:Bananguage.NumAssignmentContext):
        pass

    # Exit a parse tree produced by Bananguage#numAssignment.
    def exitNumAssignment(self, ctx:Bananguage.NumAssignmentContext):
        pass


    # Enter a parse tree produced by Bananguage#stringAssignment.
    def enterStringAssignment(self, ctx:Bananguage.StringAssignmentContext):
        pass

    # Exit a parse tree produced by Bananguage#stringAssignment.
    def exitStringAssignment(self, ctx:Bananguage.StringAssignmentContext):
        pass


    # Enter a parse tree produced by Bananguage#booleanAssignment.
    def enterBooleanAssignment(self, ctx:Bananguage.BooleanAssignmentContext):
        pass

    # Exit a parse tree produced by Bananguage#booleanAssignment.
    def exitBooleanAssignment(self, ctx:Bananguage.BooleanAssignmentContext):
        pass


    # Enter a parse tree produced by Bananguage#idReassignment.
    def enterIdReassignment(self, ctx:Bananguage.IdReassignmentContext):
        pass

    # Exit a parse tree produced by Bananguage#idReassignment.
    def exitIdReassignment(self, ctx:Bananguage.IdReassignmentContext):
        pass


    # Enter a parse tree produced by Bananguage#floatReassignment.
    def enterFloatReassignment(self, ctx:Bananguage.FloatReassignmentContext):
        pass

    # Exit a parse tree produced by Bananguage#floatReassignment.
    def exitFloatReassignment(self, ctx:Bananguage.FloatReassignmentContext):
        pass


    # Enter a parse tree produced by Bananguage#intReassignment.
    def enterIntReassignment(self, ctx:Bananguage.IntReassignmentContext):
        pass

    # Exit a parse tree produced by Bananguage#intReassignment.
    def exitIntReassignment(self, ctx:Bananguage.IntReassignmentContext):
        pass


    # Enter a parse tree produced by Bananguage#longReassignment.
    def enterLongReassignment(self, ctx:Bananguage.LongReassignmentContext):
        pass

    # Exit a parse tree produced by Bananguage#longReassignment.
    def exitLongReassignment(self, ctx:Bananguage.LongReassignmentContext):
        pass


    # Enter a parse tree produced by Bananguage#stringReassignment.
    def enterStringReassignment(self, ctx:Bananguage.StringReassignmentContext):
        pass

    # Exit a parse tree produced by Bananguage#stringReassignment.
    def exitStringReassignment(self, ctx:Bananguage.StringReassignmentContext):
        pass


    # Enter a parse tree produced by Bananguage#arrayAssignment.
    def enterArrayAssignment(self, ctx:Bananguage.ArrayAssignmentContext):
        pass

    # Exit a parse tree produced by Bananguage#arrayAssignment.
    def exitArrayAssignment(self, ctx:Bananguage.ArrayAssignmentContext):
        pass


    # Enter a parse tree produced by Bananguage#arrayReassignment.
    def enterArrayReassignment(self, ctx:Bananguage.ArrayReassignmentContext):
        pass

    # Exit a parse tree produced by Bananguage#arrayReassignment.
    def exitArrayReassignment(self, ctx:Bananguage.ArrayReassignmentContext):
        pass


    # Enter a parse tree produced by Bananguage#arrayType.
    def enterArrayType(self, ctx:Bananguage.ArrayTypeContext):
        pass

    # Exit a parse tree produced by Bananguage#arrayType.
    def exitArrayType(self, ctx:Bananguage.ArrayTypeContext):
        pass


    # Enter a parse tree produced by Bananguage#arrayItem.
    def enterArrayItem(self, ctx:Bananguage.ArrayItemContext):
        pass

    # Exit a parse tree produced by Bananguage#arrayItem.
    def exitArrayItem(self, ctx:Bananguage.ArrayItemContext):
        pass


    # Enter a parse tree produced by Bananguage#arrayGet.
    def enterArrayGet(self, ctx:Bananguage.ArrayGetContext):
        pass

    # Exit a parse tree produced by Bananguage#arrayGet.
    def exitArrayGet(self, ctx:Bananguage.ArrayGetContext):
        pass


    # Enter a parse tree produced by Bananguage#type.
    def enterType(self, ctx:Bananguage.TypeContext):
        pass

    # Exit a parse tree produced by Bananguage#type.
    def exitType(self, ctx:Bananguage.TypeContext):
        pass


    # Enter a parse tree produced by Bananguage#value.
    def enterValue(self, ctx:Bananguage.ValueContext):
        pass

    # Exit a parse tree produced by Bananguage#value.
    def exitValue(self, ctx:Bananguage.ValueContext):
        pass


    # Enter a parse tree produced by Bananguage#floatValue.
    def enterFloatValue(self, ctx:Bananguage.FloatValueContext):
        pass

    # Exit a parse tree produced by Bananguage#floatValue.
    def exitFloatValue(self, ctx:Bananguage.FloatValueContext):
        pass


    # Enter a parse tree produced by Bananguage#numValue.
    def enterNumValue(self, ctx:Bananguage.NumValueContext):
        pass

    # Exit a parse tree produced by Bananguage#numValue.
    def exitNumValue(self, ctx:Bananguage.NumValueContext):
        pass


    # Enter a parse tree produced by Bananguage#numbers.
    def enterNumbers(self, ctx:Bananguage.NumbersContext):
        pass

    # Exit a parse tree produced by Bananguage#numbers.
    def exitNumbers(self, ctx:Bananguage.NumbersContext):
        pass


    # Enter a parse tree produced by Bananguage#booleanExpr.
    def enterBooleanExpr(self, ctx:Bananguage.BooleanExprContext):
        pass

    # Exit a parse tree produced by Bananguage#booleanExpr.
    def exitBooleanExpr(self, ctx:Bananguage.BooleanExprContext):
        pass


    # Enter a parse tree produced by Bananguage#printStatement.
    def enterPrintStatement(self, ctx:Bananguage.PrintStatementContext):
        pass

    # Exit a parse tree produced by Bananguage#printStatement.
    def exitPrintStatement(self, ctx:Bananguage.PrintStatementContext):
        pass


    # Enter a parse tree produced by Bananguage#readStatement.
    def enterReadStatement(self, ctx:Bananguage.ReadStatementContext):
        pass

    # Exit a parse tree produced by Bananguage#readStatement.
    def exitReadStatement(self, ctx:Bananguage.ReadStatementContext):
        pass



del Bananguage