# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        if not isinstance(width, int):
            raise TypeError("Width is not an integer")
        if not isinstance(height, int):
            raise TypeError("Height is not an integer")
        if width <= 0 :
            raise ValueError("Width must be an positive")
        if height <= 0 :
            raise ValueError("Height must be an positive")
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height


    # Implement methods is_square(), area() & perimeter() here
    def is_square(self) :
        """ 
        Return True if the rectangle is actually a square.
        """
        if self.width == self.height :
            return True
        else:
            return False

    def area(self) :
        """
        Return the area of the rectangle
        """
        return self.width * self.height
    def perimeter(self) :
        """
        Return the perimeter of the rectangle
        """
        return 2 * (self.width + self.height)

    # (See README.md for details of what they should do)
