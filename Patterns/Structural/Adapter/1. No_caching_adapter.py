# Given this vvvvvvvvvvvvv

class Point:
    def __init__(self, 
                 x: int, 
                 y: int) -> None:
        self.x = x
        self.y = y

def draw_point(p:Point):
    print(".", end="")

# Supose that in your app, everything is made of lines.

class Line:
    def __init__(self,
                 start_point: Point,
                 end_point: Point) -> None:
        self.start = start_point
        self.end = end_point

class Rectangle(list):              # A rectangle is a list of lines 
    def __init__(self, start, end, width, height):
        list.__init__()             # Inicializamos el padre.
        # Llenamos las 4 líneas
        """
        x, y                    --->        x + width, y
        x + width, y            --->        x + width, y + height
        x + width, y + height   --->        x, y + height
        x, y + height           --->        x, y
        """
        self.append(Line(Point(start, end), Point(start + width, end)))
        self.append(Line(Point(start + width, end), Point(start + width, end + height)))
        self.append(Line(Point(start + width, end + height), Point(start, end + height)))
        self.append(Line(Point(start, end + height), Point(start, end)))

class LineToPointAdapter(list):
    points_counter = 0

    def __init__(self):
        super().__init__()
        self.points_counter += 1
        # TODO implement the logic to transform lines into points.


def draw_rectangle(rcs: Rectangle):

    for rc in rcs:
        for line in rc:
            # Here is where we need to implement an adaptor since we need to draw a line and we only have been provided with a draw_point function.
            # To do this, we need to represent lines as series of points.
            adapter = LineToPointAdapter(line)
            for point in adapter:
                draw_point(point)


if __name__ == "__main__":

    rectangles = list(
        Rectangle(1,1,10,10),
        Rectangle(3,4,6,7)
    )