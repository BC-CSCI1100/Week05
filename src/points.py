# CSCI 1100 Gateway to Computer Science
#
# Some simple problem involving distances
#
# A point is a pair (x, y).

import math

# distance : point * point -> float
def distance(point1, point2):
    (x1, y1) = point1
    (x2, y2) = point2
    return math.sqrt((x1 - x2) ** 2.0 + (y1 - y2) ** 2.0)

# distances : point * list point -> list float
def distances(point, points):
    return [ distance(point, other) for other in points ]

# nearestPoint : point * list point -> point
def nearestPoint(point, points):
    distances = [ (other, distance(point, other)) for other in points ]
    (nearest, shortestDistance) = distances[0]
    for (other, otherDistance) in distances[1:]:
        if otherDistance < shortestDistance:
            (nearest, shortestDistance) = (other, otherDistance)
    return nearest

points = [(1, 1), (1, 2), (3, 4)]
