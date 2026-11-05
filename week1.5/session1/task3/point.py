# Week 1.5, Session 1: Task 3

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here

    def __init__(self, x, y):
        """Create a point with x and y coordinates."""
        self.x = x
        self.y = y

    # Add distance() method here

    def distance(self):
        """Return the distance from this point to the origin."""
        return math.hypot(self.x, self.y)
    
    # Add distance_to() method here

    def distance_to(self, other):
        """Return the distance between this point and another point."""
        return math.hypot(self.x - other.x, self.y - other.y)
    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point
p1 = Point(3, 4)
p2 = Point(6, 8)

print(p1.x, p1.y)
print(p1.distance())
print(p1.distance_to(p2))