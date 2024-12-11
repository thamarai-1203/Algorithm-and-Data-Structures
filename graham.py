# importing libraries
import math
from collections import deque

class Point2D:
    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

# representation of object using string
    def __str__(self) -> str:
        return f"@Point2D ({self._x}, {self._y})"

#method compares two 2D point objects
    def __eq__(self, value: object) -> bool:
        return self.x == value.x and self.y == value.y; 

#method debugs and log
    def __repr__(self) -> str:
        return f"Point2D({self._x}, {self._y})"

#method allows 2D point objects in sets
    def __hash__(self):
        return hash((self._x, self._y))

    @property #to get x-coordinate
    def x(self) -> float:
        return self._x
    
    @property #to get y-coordinate
    def y(self) -> float:
        return self._y
    
#function graham scan follows the algorithm to compute convex hull
def graham_scan(points: list[Point2D]) -> list[Point2D]:
# leftmost lowest function to find the leftmost lowest point
    def leftmost_lowest(points: list[Point2D]) -> Point2D:
        return min(points, key=lambda p: (p.y, p.x))

# polar angle function to calculate the polar angle from p0 to p1
    def polar_angle(p0: Point2D, p1: Point2D) -> float:
        return math.atan2(p1.y - p0.y, p1.x - p0.x)

#distance function to calculate the distance between p0 and p1
    def distance(p0: Point2D, p1: Point2D) -> float:
        return (p1.x - p0.x) ** 2 + (p1.y - p0.y) ** 2

#turns left function to check if the sequence of points makes a left turn
    def turns_left(p0: Point2D, p1: Point2D, p2: Point2D) -> bool:
        return (p1.x - p0.x) * (p2.y - p0.y) - (p1.y - p0.y) * (p2.x - p0.x) > 0

#returns the points as it is if there are one or no points
    if len(points) <= 1:
        return points

# finds the leftmost lowest point p0
    p0 = leftmost_lowest(points)
    points.remove(p0)

#returns p0 and the only one remaining point
    if len(points) == 1:
        return [p0] + points

# Sorts points by polar angle with p0
    points.sort(key=lambda p: (polar_angle(p0, p), distance(p0, p)))

#  Creates deque stack and pushes first three points importing deque library
    hull = deque([p0, points[0], points[1]])

# processes the remaining points
    for p in points[2:]:
#to make sure the points take left turn otherwise it pop
        while len(hull) > 1 and not turns_left(hull[-2], hull[-1], p):
            hull.pop()
        hull.append(p)

    return hull
    pass






