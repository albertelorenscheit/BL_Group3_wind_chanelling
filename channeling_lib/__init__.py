import importlib

# Import channeling_lib.py dynamically
module_name = "channeling_lib.channeling_lib"
module = importlib.import_module(module_name)

# Get all attributes from the module
__all__ = [name for name in dir(module) if not name.startswith("_")]

# Dynamically add each function/class to the package namespace
for name in __all__:
    globals()[name] = getattr(module, name)

