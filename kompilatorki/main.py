from llvmlite import ir

# Utwórz moduł i funkcję main
module = ir.Module(name="bananguage_module")
function_type = ir.FunctionType(ir.VoidType(), [])
function = ir.Function(module, function_type, name="main")
block = function.append_basic_block(name="entry")
builder = ir.IRBuilder(block)

# Przechowuj zmienne w słowniku
variables = {}

def assign_variable(type_keyword, identifier, value):
    if type_keyword in ["monkeiii", "monkl"]:  # int or long
        var_type = ir.IntType(64) if type_keyword == "monkl" else ir.IntType(32)
        alloca = builder.alloca(var_type, name=identifier)
        const_value = ir.Constant(var_type, int(value))
        builder.store(const_value, alloca)
        variables[identifier] = alloca
    elif type_keyword == "gorilla":  # float
        var_type = ir.DoubleType()
        alloca = builder.alloca(var_type, name=identifier)
        const_value = ir.Constant(var_type, float(value))
        builder.store(const_value, alloca)
        variables[identifier] = alloca
    elif type_keyword == "lemur":  # string
        var_type = ir.IntType(8).as_pointer()
        alloca = builder.alloca(var_type, name=identifier)
        variables[identifier] = alloca
        # Przykład może wymagać użycia funkcji runtime do zarządzania pamięcią dla stringów
    elif type_keyword == "chimp":  # bool
        var_type = ir.IntType(1)
        alloca = builder.alloca(var_type, name=identifier)
        const_value = ir.Constant(var_type, bool(value == "true"))
        builder.store(const_value, alloca)
        variables[identifier] = alloca
    # Obsługa array jest znacznie bardziej złożona, wymagałaby dodatkowej logiki

def handle_arithmetic(expr, op, expr2):
    left = builder.load(variables[expr], name=expr + "_val")
    right = builder.load(variables[expr2], name=expr2 + "_val")
    if op == 'ADD':
        result = builder.add(left, right, name="addtmp")
    elif op == 'SUB':
        result = builder.sub(left, right, name="subtmp")
    elif op == 'MUL':
        result = builder.mul(left, right, name="multmp")
    elif op == 'DIV':
        result = builder.sdiv(left, right, name="divtmp")
    return result

def promote_types(left, right):
    left_type = left.type
    right_type = right.type

    # Promocja int (32 bity) do long (64 bity)
    if left_type == ir.IntType(32) and right_type == ir.IntType(64):
        left = builder.sext(left, ir.IntType(64), name="promote_to_long")
    elif left_type == ir.IntType(64) and right_type == ir.IntType(32):
        right = builder.sext(right, ir.IntType(64), name="promote_to_long")

    # Promocja int lub long do double
    if (left_type in [ir.IntType(32), ir.IntType(64)] and right_type == ir.DoubleType()):
        left = builder.sitofp(left, ir.DoubleType(), name="promote_to_double")
    elif (left_type == ir.DoubleType() and right_type in [ir.IntType(32), ir.IntType(64)]):
        right = builder.sitofp(right, ir.DoubleType(), name="promote_to_double")

    return left, right


assign_variable("monkeiii", "a", 3)
assign_variable("monkl", "b", 4)
assign_variable("gorilla", "c", 1.5)
assign_variable("lemur", "my_string", '"Hello World"')
assign_variable("chimp", "my_bool", "true")

# Operacje arytmetyczne
result = handle_arithmetic("a", "MUL", "a")
builder.ret_void()

print(module)

