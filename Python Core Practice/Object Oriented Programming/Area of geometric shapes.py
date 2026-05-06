"""5. You are creating a system that calculates the area of different geometric shapes.
Design a base class that represents the concept of a shape.
This class must:
• Define a method named area().
• Not provide any formula, because the formula depends entirely on the shape type.
• Prevent the creation of objects that do not define how area is calculated.
Create concrete shape classes such as rectangle, circle, and triangle.
Write code that:
• Stores different shapes in a single collection.
• Calculates area without checking which shape it is.
Explain:
• Why forcing every shape to implement area() avoids runtime errors.
• Why using condition-based logic is harder to scale.
• Why this design makes future shapes easy to add."""
