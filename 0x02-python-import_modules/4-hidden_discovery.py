#!/usr/bin/python3
import dis
import types

if __name__ == "__main__":
    # Load the compiled module
    module = types.ModuleType("hidden_4")
    with open("hidden_4.pyc", "rb") as file:
        magic = file.read(4)
        timestamp = file.read(4)
        code_object = compile(file.read(), "", "exec")
        exec(code_object, module.__dict__)

    # Retrieve names defined in the module
    names = [name for name in dir(module) if not name.startswith("__")]

    # Sort and print the names
    for name in sorted(names):
        print(name)
