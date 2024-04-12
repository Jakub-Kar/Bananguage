from antlr4 import *
from BananguageLexer import BananguageLexer
from Bananguage import  Bananguage
import re
from llvmlite import ir
import llvmlite.binding as llvm

# Inicjalizacja LLVM
llvm.initialize()
llvm.initialize_all_targets()
llvm.initialize_all_asmprinters()

# Utwórz moduł i funkcję main
module = ir.Module(name="bananguage_module")
function_type = ir.FunctionType(ir.VoidType(), [])
function = ir.Function(module, function_type, name="main")
block = function.append_basic_block(name="entry")
builder = ir.IRBuilder(block)

# Przechowuj zmienne w słowniku
variables = {}

# Dodajemy deklaracje funkcji printf i scanf do modułu
printf_ty = ir.FunctionType(ir.IntType(32), [ir.PointerType(ir.IntType(8))], var_arg=True)
printf = ir.Function(module, printf_ty, name="printf")

scanf_ty = ir.FunctionType(ir.IntType(32), [ir.PointerType(ir.IntType(8))], var_arg=True)
scanf = ir.Function(module, scanf_ty, name="scanf")


def assign_variable(type_keyword, identifier, value):
    if type_keyword == "monkeiii":  # int
        var_type = ir.IntType(32)
    elif type_keyword == "monkl":  # long
        var_type = ir.IntType(64)
    elif type_keyword == "gorilla":  # float
        var_type = ir.DoubleType()
    elif type_keyword == "chimp":  # bool
        var_type = ir.IntType(1)
        value = True if value.lower() == "true" else False

    alloca = builder.alloca(var_type, name=identifier)
    const_value = ir.Constant(var_type, value)
    builder.store(const_value, alloca)
    variables[identifier] = alloca

def handle_arithmetic(var, op, value):
    left = builder.load(variables[var], name=var + "_val")
    right = ir.Constant(left.type, value)
    if op == 'ADD':
        result = builder.add(left, right, name=var + "_add")
    elif op == 'SUB':
        result = builder.sub(left, right, name=var + "_sub")
    elif op == 'MUL':
        result = builder.mul(left, right, name=var + "_mul")
    elif op == 'DIV':
        result = builder.sdiv(left, right, name=var + "_div")
    builder.store(result, variables[var])

def print_variable(var):
    var_val = builder.load(variables[var], name=var + "_load")
    format_str = "%d\n\0" if isinstance(var_val.type, ir.IntType) else "%f\n\0"
    fmt_arg = builder.alloca(ir.ArrayType(ir.IntType(8), len(format_str)), name="fmt")
    builder.store(ir.Constant(ir.ArrayType(ir.IntType(8), len(format_str)), bytearray(format_str.encode("utf8"))), fmt_arg)
    builder.call(printf, [builder.bitcast(fmt_arg, ir.PointerType(ir.IntType(8)))])

def read_variable(var):
    fmt_str = "%d\0" if isinstance(variables[var].type.pointee, ir.IntType) else "%f\0"
    fmt_arg = builder.alloca(ir.ArrayType(ir.IntType(8), len(fmt_str)), name="fmt")
    builder.store(ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt_str)), bytearray(fmt_str.encode("utf8"))), fmt_arg)
    builder.call(scanf, [builder.bitcast(fmt_arg, ir.PointerType(ir.IntType(8))), variables[var]])

def parse_tree(tree):
    # Regex do wyłuskania przypisania liczbowego
    num_assignments = re.findall(r"\(numAssignment (\w+) (\w+) = \(value \(numbers (\d+)\)\)\)", tree)
    for type_, var, value in num_assignments:
        assign_variable(type_, var, value)

    # Regex do wyłuskania przypisania z operacjami arytmetycznymi
    arith_assignments = re.findall(r"\(numAssignment (\w+) (\w+) = \(value \(numbers (\d+)\) \+ \(numbers (\d+)\)\)\)", tree)
    for type_, var, val1, val2 in arith_assignments:
        assign_variable(type_, var, val1)  # Początkowa wartość
        handle_arithmetic(var, "ADD", val2)  # Dodaj drugą wartość

    # Regex do wyłuskania przypisania boolean
    bool_assignments = re.findall(r"\(booleanAssignment (\w+) (\w+) = \(booleanExpr (true|false)\)\)", tree)
    for type_, var, value in bool_assignments:
        assign_variable(type_, var, value)

    # Proste przetwarzanie print i read - dla przykładu
    reads = re.findall(r"\(readStatement read \( (\w+) \)\)", tree)
    for var in reads:
        read_variable(var)  # Załóżmy, że mamy funkcję do odczytu

    prints = re.findall(r"\(printStatement print \( (\w+) \)\)", tree)
    for var in prints:
        print_variable(var)  # Załóżmy, że mamy funkcję do wyświetlania

def compile_to_machine_code(llvm_ir):
    # Tworzenie obiektu modułu LLVM
    mod = llvm.parse_assembly(str(llvm_ir))

    # Kompilacja modułu do kodu maszynowego
    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    mod.verify()

    return target_machine.emit_object(mod)

def read_variable(var):
    if var in variables:
        var_alloca = variables[var]
        fmt_str = "%d\0" if isinstance(var_alloca.type.pointee, ir.IntType) else "%f\0"
        fmt_arg = builder.alloca(ir.ArrayType(ir.IntType(8), len(fmt_str)), name="fmt")
        builder.store(ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt_str)), bytearray(fmt_str.encode("utf8"))), fmt_arg)
        builder.call(scanf, [builder.bitcast(fmt_arg, ir.PointerType(ir.IntType(8))), var_alloca])
    else:
        print(f"Variable '{var}' not declared.")


def print_variable(var):
    if var in variables:
        var_val = builder.load(variables[var], name=var + "_load")
        format_str = "%d\n\0" if isinstance(var_val.type, ir.IntType) else "%f\n\0"
        fmt_arg = builder.alloca(ir.ArrayType(ir.IntType(8), len(format_str)), name="fmt")
        builder.store(ir.Constant(ir.ArrayType(ir.IntType(8), len(format_str)), bytearray(format_str.encode("utf8"))), fmt_arg)
        builder.call(printf, [builder.bitcast(fmt_arg, ir.PointerType(ir.IntType(8)))])
    else:
        print(f"Variable '{var}' not declared.")



# Przykładowe użycie
input_stream = FileStream("kod.txt")
lexer = BananguageLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = Bananguage(stream)
tree = parser.program()  # Zmień na odpowiednią regułę
parse_tree(tree.toStringTree(recog=parser))

builder.ret_void()
print("Reprezentacja LLVM IR")
print(module)  # Wyświetlenie wygenerowanego kodu LLVM IR

print("Kod maszynowy")
print(compile_to_machine_code(module))
