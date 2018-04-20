"""Point and Rectangle classes.

Point: point with (x,y) coordinates
Rect:  two points, forming a rectangle
"""

import math


class Point:

    """A point identified by (x,y) coordinates."""

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, p):
        """Point(x1+x2, y1+y2)"""
        return Point(self.x+p.x, self.y+p.y)

    def __sub__(self, p):
        """Point(x1-x2, y1-y2)"""
        return Point(self.x-p.x, self.y-p.y)

    def __mul__(self, n):
        """Point(x*n, y*n)"""
        return Point(self.x*n, self.y*n)

    def __div__(self, n):
        """Point(x1/n, y1/n)"""
        return Point(self.x/n, self.y/n)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def __repr__(self):
        return "%s(%r, %r)" % (self.__class__.__name__, self.x, self.y)

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to(self, p):
        """Calculate the distance between two points."""
        return (self - p).length()

    def as_tuple(self):
        """(x, y)"""
        return (self.x, self.y)

    def clone(self):
        """Return a full copy of this point."""
        return Point(self.x, self.y)

    def integerize(self):
        """Convert co-ordinate values to integers."""
        self.x = int(self.x)
        self.y = int(self.y)

    def floatize(self):
        """Convert co-ordinate values to floats."""
        self.x = float(self.x)
        self.y = float(self.y)

    def set(self, x, y):
        """Reset x & y coordinates."""
        self.x = x
        self.y = y

    def add(self, p):
        """Move to Point(x1+x2, y1+y2)."""
        self.x = self.x + p.x
        self.y = self.y + p.y

    def add(self, dx, dy):
        """Move to Point(x+dx,y+dy)."""
        self.x = self.x + dx
        self.y = self.y + dy

    def rotate(self, rad):
        """Rotate counter-clockwise by rad radians.

        Positive y goes *up,* as in traditional mathematics.

        Interestingly, you can use this in y-down computer graphics, if
        you just remember that it turns clockwise, rather than
        counter-clockwise.

        The new position is returned as a new Point.
        """
        s, c = [f(rad) for f in (math.sin, math.cos)]
        x, y = (c*self.x - s*self.y, s*self.x + c*self.y)
        return Point(x, y)

    def rotate_about(self, p, theta):
        """Rotate counter-clockwise around a point, by theta degrees.

        Positive y goes *up,* as in traditional mathematics.

        The new position is returned as a new Point.
        """
        result = self.clone()
        result.slide(-p.x, -p.y)
        result.rotate(theta)
        result.slide(p.x, p.y)
        return result


class Rect:

    """A rectangle identified by two points (min and max).

    origin                         min   top
       +-----> x increases                |
       |                           left  -+-  right
       v                                  |
    y increases                         bottom  max
    """

    def __init__(self, p1=Point(), p2=Point()):
        """Initialize a rectangle from two points."""
        self.set_points(p1, p2)

    def __eq__(self, other):
        return (self.min == other.min) and (self.max == other.max)

    def __iter__(self):
        """Yields all integer points in the rectangle."""
        for y in range(int(self.min.y), int(self.max.y)+1):
            for x in range(int(self.min.x), int(self.max.x)+1):
                yield Point(x, y)

    def __contains__(self, p):
        return self.contains(p)

    def set_points(self, p1, p2):
        """Set the rectangle coordinates."""
        self.min = p1
        self.max = p2

    def contains(self, p):
        """Return true if a point is inside the rectangle."""
        return (self.min.x <= p.x <= self.max.x and
                self.min.y <= p.y <= self.max.y)

    def overlaps(self, other):
        """Return true if a rectangle overlaps this rectangle."""
        return (self.max.x > other.min.x and self.min.x < other.max.x and
                self.min.y < other.max.y and self.max.y > other.min.y)

    def expanded_by(self, n):
        """Return a rectangle with extended borders.

        Create a new rectangle that is wider and taller than the
        immediate one. All sides are extended by 'n' points.
        """
        p1 = Point(self.min.x-n, self.min.y-n)
        p2 = Point(self.max.x+n, self.max.y+n)
        return Rect(p1, p2)

    def shift_by(self, dx, dy):
        """Return a rectangle that is shifted by dx and dy."""
        p1 = Point(self.min.x+dx, self.min.y+dy)
        p2 = Point(self.max.x+dx, self.max.y+dy)
        return Rect(p1, p2)

    def __str__(self):
        return "<Rect (%s,%s)-(%s,%s)>" % (self.left, self.top,
                                           self.right, self.bottom)

    def __repr__(self):
        return "%s(%r, %r)" % (self.__class__.__name__,
                               Point(self.left, self.top),
                               Point(self.right, self.bottom))
