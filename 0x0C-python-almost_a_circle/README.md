# Python almost a circle

# Rectangle Class

This Python module contains the `Rectangle` class, which is designed to represent rectangles in terms of area. The class inherits from the `Base` class and introduces attributes for width, height, x-coordinate, y-coordinate, and an id. It also includes methods for calculating the area, displaying the rectangle, and providing a string representation.

## Class Structure

### Attributes
- `width` (int): Width of the rectangle.
- `height` (int): Height of the rectangle.
- `x` (int): X-coordinate of the rectangle.
- `y` (int): Y-coordinate of the rectangle.
- `id` (int): ID of the rectangle.

### Methods
- `__init__(width, height, x=0, y=0, id=None)`: Initializes a rectangle with the specified width, height, coordinates, and id.
- `area()`: Calculates the area of the rectangle using the formula `area = width * height`.
- `display()`: Displays the rectangle using "#" characters, considering the x and y coordinates.
- `__str__()`: Provides a string representation of the rectangle in the format "[Rectangle] (id) x/y - width/height".

## Usage

```python
from models.rectangle import Rectangle

# Create a rectangle
rectangle = Rectangle(4, 5, 1, 2, 42)

# Get attributes
print(rectangle.width)  # Output: 4
print(rectangle.height)  # Output: 5
print(rectangle.x)  # Output: 1
print(rectangle.y)  # Output: 2
print(rectangle.id)  # Output: 42

# Calculate and print the area
print(rectangle.area())  # Output: 20

# Display the rectangle
rectangle.display()
# Output:
# 
# 
#     ####
#     ####
#     ####
#     ####
#     ####

# Print the string representation of the rectangle
print(str(rectangle))  # Output: "[Rectangle] (42) 1/2 - 4/5"

