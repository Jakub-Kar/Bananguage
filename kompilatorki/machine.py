import llvmlite.binding as llvm


def compile_to_machine_code(llvm_ir):
    # Tworzenie obiektu modułu LLVM
    mod = llvm.parse_assembly(llvm_ir)

    # Kompilacja modułu do kodu maszynowego
    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    mod.verify()

    return target_machine.emit_object(mod)
