"""3. Create two Python modules that import each other. Run the program to observe
what happens with circular imports. Then think of different ways to prevent a
circular-import crash."""
import circularimport1
def func2():
    print("B")
circularimport1.func1()
