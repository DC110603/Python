"""3. Create two Python modules that import each other. Run the program to observe
what happens with circular imports. Then think of different ways to prevent a
circular-import crash."""
import circularimport2
def func1():
    print("A")
circularimport2.func2()
