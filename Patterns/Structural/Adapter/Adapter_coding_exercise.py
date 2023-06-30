class Square:
    def __init__(self, 
                 side: int =0):
        self.side = side

def calculate_area(rc):
    print(rc.width * rc.height)
    return rc.width * rc.height

class SquareToRectangleAdapter:
    def __init__(self, 
                 square: Square):
        # TODO
        # self.width = square.side
        # self.height = square.side
        self.sq = square

    @property
    def width(self):
        return self.sq.side
    
    @property
    def height(self):
        return self.sq.side

sq = Square(10)
rc = SquareToRectangleAdapter(sq)
calculate_area(rc=rc)
sq.side = 11
calculate_area(rc=rc)