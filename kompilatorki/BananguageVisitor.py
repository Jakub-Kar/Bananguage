# Generated from C:/Users/admin/PycharmProjects/kompilatorki/Bananguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Bananguage import Bananguage
else:
    from Bananguage import Bananguage

# This class defines a complete generic visitor for a parse tree produced by Bananguage.

class BananguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Bananguage#program.
    def visitProgram(self, ctx:Bananguage.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#statement.
    def visitStatement(self, ctx:Bananguage.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#expr.
    def visitExpr(self, ctx:Bananguage.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#assignment.
    def visitAssignment(self, ctx:Bananguage.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#floatAssignment.
    def visitFloatAssignment(self, ctx:Bananguage.FloatAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#numAssignment.
    def visitNumAssignment(self, ctx:Bananguage.NumAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#stringAssignment.
    def visitStringAssignment(self, ctx:Bananguage.StringAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#booleanAssignment.
    def visitBooleanAssignment(self, ctx:Bananguage.BooleanAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#idReassignment.
    def visitIdReassignment(self, ctx:Bananguage.IdReassignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#floatReassignment.
    def visitFloatReassignment(self, ctx:Bananguage.FloatReassignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#intReassignment.
    def visitIntReassignment(self, ctx:Bananguage.IntReassignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#longReassignment.
    def visitLongReassignment(self, ctx:Bananguage.LongReassignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#stringReassignment.
    def visitStringReassignment(self, ctx:Bananguage.StringReassignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#arrayAssignment.
    def visitArrayAssignment(self, ctx:Bananguage.ArrayAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#arrayReassignment.
    def visitArrayReassignment(self, ctx:Bananguage.ArrayReassignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#arrayType.
    def visitArrayType(self, ctx:Bananguage.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#arrayItem.
    def visitArrayItem(self, ctx:Bananguage.ArrayItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#arrayGet.
    def visitArrayGet(self, ctx:Bananguage.ArrayGetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#type.
    def visitType(self, ctx:Bananguage.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#value.
    def visitValue(self, ctx:Bananguage.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#floatValue.
    def visitFloatValue(self, ctx:Bananguage.FloatValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#numValue.
    def visitNumValue(self, ctx:Bananguage.NumValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#numbers.
    def visitNumbers(self, ctx:Bananguage.NumbersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#booleanExpr.
    def visitBooleanExpr(self, ctx:Bananguage.BooleanExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#printStatement.
    def visitPrintStatement(self, ctx:Bananguage.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Bananguage#readStatement.
    def visitReadStatement(self, ctx:Bananguage.ReadStatementContext):
        return self.visitChildren(ctx)



del Bananguage