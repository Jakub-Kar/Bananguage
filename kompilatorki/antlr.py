from antlr4 import *
from BananguageLexer import BananguageLexer
from Bananguage import  Bananguage
import re



input_stream = FileStream("kod.txt")
lexer = BananguageLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = Bananguage(stream)
tree = parser.program()  # Zmień na odpowiednią regułę
print(tree.toStringTree(recog=parser))


def parse_tree(tree):
    # Zmienna do przechowywania wyniku
    result = []

    # Regex do wyłuskania przypisania liczbowego
    num_assignments = re.findall(r"\(numAssignment (\w+) (\w+) = \(value \(numbers (\d+)\)\)\)", tree)
    for type_, var, value in num_assignments:
        result.append(f"assign_variable(\"{type_}\", \"{var}\", {value})")

    # Regex do wyłuskania przypisania z operacjami arytmetycznymi
    arith_assignments = re.findall(r"\(numAssignment (\w+) (\w+) = \(value \(numbers (\d+)\) \+ \(numbers (\d+)\)\)\)", tree)
    for type_, var, val1, val2 in arith_assignments:
        result.append(f"assign_variable(\"{type_}\", \"{var}\", {val1})  # Początkowa wartość")
        result.append(f"result = handle_arithmetic(\"{var}\", \"ADD\", \"{val2}\")  # Dodaj drugą wartość")

    # Regex do wyłuskania przypisania boolean
    bool_assignments = re.findall(r"\(booleanAssignment (\w+) (\w+) = \(booleanExpr (true|false)\)\)", tree)
    for type_, var, value in bool_assignments:
        result.append(f"assign_variable(\"{type_}\", \"{var}\", {value})")

    # Proste przetwarzanie print i read - dla przykładu
    reads = re.findall(r"\(readStatement read \( (\w+) \)\)", tree)
    for var in reads:
        result.append(f"read_variable(\"{var}\")")  # Załóżmy, że mamy funkcję do odczytu

    prints = re.findall(r"\(printStatement print \( (\w+) \)\)", tree)
    for var in prints:
        result.append(f"print_variable(\"{var}\")")  # Załóżmy, że mamy funkcję do wyświetlania

    # Zwrócenie skumulowanego wyniku jako jeden string
    return "\n".join(result)



parsed_tree = parse_tree(tree.toStringTree(recog=parser))
print(parsed_tree)
#
