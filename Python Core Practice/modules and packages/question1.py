"""1. Write a Python program that attempts to dynamically import a module at
runtime. The program should only import the module if it actually exists;
otherwise, it should print "Module does not exist"."""
import importlib
module_name=input("Write Module Name:")

try:
    np=importlib.import_module(module_name)
except ModuleNotFoundError:
    print("Module Not Found")
else:
    print("Module Imported")