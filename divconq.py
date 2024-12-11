#importing libraries
import math
from typing import List,Tuple #list for merge sort and tuple for closed pair(Divide and conquer)
#defining class which represents 2D points
class Point2D:
    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y
#string represents 2D point object
    def __str__(self) -> str:
        return f"@Point2D ({self._x}, {self._y})"
#equality operator to compare two 2D points objects
    def __eq__(self, value: object) -> bool:
        return self.x == value.x and self.y == value.y
#to get x-coordinate
    @property
    def x(self) -> float:
        return self._x
#to get y-coordinate
    @property
    def y(self) -> float:
        return self._y
#function implements merge sort algorithm for sorting 2D point objects
def merge_sort(points: List[Point2D], key=lambda p: p) -> List[Point2D]:
    if len(points) <= 1:
        return points
#helper function merges two sorted points
    def merge(A: List[Point2D], p: int, q: int, r: int, key) -> None:
        n1 = math.ceil((q - p + 1) / 2)
        n2 = math.ceil((r - q) / 2)
        L = A[p:q+1] + [Point2D(math.inf, math.inf)]#left half using math.lib
        R = A[q+1:r+1] + [Point2D(math.inf, math.inf)]#right half using math.lib

        i = j = 0
        for k in range(p, r+1):
            if key(L[i]) <= key(R[j]):
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
#recursive function merge sort performs merge sort
    def merge_sort_recursive(A: List[Point2D], p: int, r: int, key) -> None:
        if p < r:
            q = (p + r) // 2
            merge_sort_recursive(A, p, q, key)#sorts left half
            merge_sort_recursive(A, q + 1, r, key)#sorts right half
            merge(A, p, q, r, key)#merges both right and left half
    merge_sort_recursive(points, 0, len(points) - 1, key)
    return points
    pass
#calculates Euclidean distance between two points
def dist(p1: Point2D,p2: Point2D) -> float:
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)#Euclidean distance formula

#brute force method finds the closest pair of points
def brute_force_closest_points(points: List[Point2D]) -> Tuple[Point2D, Point2D]:
    min_dist = float('inf')
    pair = (None, None)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = dist(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return pair

#combines step to find the closest pair
def combine(Y: List[Point2D], l_x: float, pair1: Tuple[Point2D, Point2D], pair2: Tuple[Point2D, Point2D]) -> Tuple[
    Point2D, Point2D]:
    if pair1 is None:
        p1, p2 = pair2
        d = dist(p1, p2)
    elif pair2 is None:
        p1, p2 = pair1
        d = dist(p1, p2)
    else:
        d1 = dist(pair1[0], pair1[1])
        d2 = dist(pair2[0], pair2[1])
        if d1 < d2:
            p1, p2 = pair1
            d = d1
        else:
            p1, p2 = pair2
            d = d2
#points within the 2D strip width
    Y_prime = [p for p in Y if l_x - d <= p.x <= l_x + d]
#checks upto 7 points
    for i in range(len(Y_prime)):
        for j in range(1, 8):
            if i + j < len(Y_prime):
                p3, p4 = Y_prime[i], Y_prime[i + j]
                d3 = dist(p3, p4)
                if d3 < d:
                    p1, p2 = p3, p4
                    d = d3

    return (p1, p2)

#main function closest pair finds closest pair of points using divide and conquer rule
def closest_pair(points: List[Point2D]) -> Tuple[Point2D, Point2D]:
    if not points:
        return (None, None)

    if len(points) == 1:
        return (None, None)

    X = merge_sort(points, key=lambda p: p.x)#sorts points by x-coordinate
    Y = merge_sort(points, key=lambda p: p.y)#sorts points by x-coordinate
#recursive function finds the closest points in the list
    def find_closest_points(X: List[Point2D], Y: List[Point2D]) -> Tuple[Point2D, Point2D]:
        if len(X) > 3:
            m = len(X) // 2
            l_x = (X[m - 1].x + X[m].x) / 2
            X_l = X[:m]
            X_r = X[m:]
            Y_l = [p for p in Y if p.x <= l_x]
            Y_r = [p for p in Y if p.x > l_x]

            (p1, p2) = find_closest_points(X_l, Y_l)
            (p3, p4) = find_closest_points(X_r, Y_r)
            return combine(Y, l_x, (p1, p2), (p3, p4))
        else:
            return brute_force_closest_points(X)

    return find_closest_points(X, Y)
    pass

