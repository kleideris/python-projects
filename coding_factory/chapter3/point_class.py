"""
Challenge: Define the dunder function used to compare two different instances of the Point class. 
"""

import math

class Point:
    """
    A class representing a point in 2D space.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y coordinate of thr point.
    """
    __count = 0

    def __init__(self, x=0, y=0):
        """
        Initialize a Point object with specified x and y coordinates.

        Args:
            x (float): The x-coordinate of the point. Defaults to 0.
            y (float): The y coordinate of thr point. Defaults to 0.
        """
        self.__x = x
        self.__y = y
        Point.__count += 1
        
    def __str__(self):
        """
        Returns a string representation of the object in the format (x, y).
        """
        return f"({self.__x}, {self.__y})"

    def __eq__(self, other):
        """
        Implements == for Points based on their coordinates.
        Makes sure we are comparing Points.
        """
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y == other.__y
        else:
            return False
        

    # TODO: def __lt__, __gt__ (<, >) also greater than equal, less than equal
    def distance_from_center(self):
        """
        Returns the Euclidean distance from the origin (0, 0) to the Point.
        """
        return math.sqrt(math.pow(self.__x, 2) + math.pow(self.__y, 2))

    def __lt__(self, other):
        """
        Implements < for Points based on their coordinates.

        Makes sure we are comparing Points.
        """
        if isinstance(other, Point):
            return self.distance_from_center() < other.distance_from_center()
    
    def __gt__(self,other):
        """
        Implements > for Points based on their coordinates.

        Makes sure we are comparing Points.
        """
        if isinstance(other, Point):
            return self.distance_from_center() > other.distance_from_center()
    
    def __le__(self, other):
        """
        Implements <= for Points based on their coordinates.

        Makes sure we are comparing Points.
        """
        if isinstance(other, Point):
            return self.distance_from_center() <= other.distance_from_center()
    
    def __ge__(self, other):
        """
        Implements >= for Points based on their coordinates.

        Makes sure we are comparing Points.
        """
        if isinstance(other, Point):
            return self.distance_from_center() >= other.distance_from_center()

#TESTING:

def main():
    

    # Define a few Point objects to test
    point_a = Point(3, 4)     # distance = 5
    point_b = Point(6, 8)     # distance = 10
    point_c = Point(3, 4)     # same as point_a
    point_d = Point(0, 0)     # distance = 0

    # Test the string representation
    print("Test __str__:")
    print(str(point_a))  # Expected output: (3, 4)

    # Test equality: same coordinates -> should be equal
    print("\nTest __eq__:")
    print(point_a == point_c)  # Expected: True
    print(point_a == point_b)  # Expected: False

    # Test less than: compare distances from origin
    print("\nTest __lt__:")
    print(point_a < point_b)  # Expected: True
    print(point_b < point_a)  # Expected: False

    # Test greater than
    print("\nTest __gt__:")
    print(point_b > point_d)  # Expected: True
    print(point_d > point_b)  # Expected: False

    # Test less than or equal to
    print("\nTest __le__:")
    print(point_a <= point_c)  # Expected: True (equal)
    print(point_d <= point_a)  # Expected: True

    # Test greater than or equal to
    print("\nTest __ge__:")
    print(point_b >= point_a)  # Expected: True
    print(point_d >= point_b)  # Expected: False

if __name__ == "__main__":
    main()