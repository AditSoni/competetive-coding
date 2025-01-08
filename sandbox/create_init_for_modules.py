import os
import ast

def create_init_files_with_all(package_path):
    """
    Iterate through a Python package directory and create/update `__init__.py` files.
    Includes all functions and classes from the modules in the package and adds an __all__ attribute.
    
    Args:
        package_path (str): Path to the root of the Python package.
    """
    for root, dirs, files in os.walk(package_path):
        # Filter Python files
        python_files = [f for f in files if f.endswith('.py') and f != '__init__.py']
        all_imports = []
        all_exports = []

        for py_file in python_files:
            file_path = os.path.join(root, py_file)
            module_name = py_file[:-3]  # Remove ".py" from file name
            
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
            
            # Parse Python file to get function and class definitions
            try:
                tree = ast.parse(file_content)
                for node in tree.body:
                    if isinstance(node, ast.FunctionDef):  # Function
                        all_imports.append(f"from .{module_name} import {node.name}")
                        all_exports.append(f"{node.name}")
                    elif isinstance(node, ast.ClassDef):  # Class
                        all_imports.append(f"from .{module_name} import {node.name}")
                        all_exports.append(f"{node.name}")
            except SyntaxError as e:
                print(f"Skipping {file_path} due to syntax error: {e}")

        # Write `__init__.py` file
        init_file_path = os.path.join(root, '__init__.py')
        with open(init_file_path, 'w', encoding='utf-8') as init_file:
            init_file.write("# Auto-generated __init__.py\n")
            if all_imports:
                init_file.write("\n".join(all_imports) + "\n")
            if all_exports:
                all_ = ', '.join(f'\"{name}\"' for name in all_exports)
                init_file.write(f"\n__all__ = [{all_}]\n")
            else:
                init_file.write("# No functions or classes found.\n")

        print(f"Updated: {init_file_path}")

# Example Usage
# create_init_files_with_all("path/to/your/package")

create_init_files_with_all("/Users/aditsoni/Desktop/Workspace/GKMIT/s2s-main/S2S-Agent/llm_bridge")