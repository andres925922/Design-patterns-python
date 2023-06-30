from abc import ABC                                 #Abstract class

class Render(ABC):

    def render_circle(self, radius):
        pass

    # def render_square(self, sq):
    #     pass


class VectorRender(Render):

    def render_circle(self, radius):
        print(f"Rendering a circle or radius {radius}")

class RasterRender(Render):

    def render_circle(self, radius):
        print(f"Drawing pixels for a circle of radius {radius}")

class Shape:

    def __init__(self, renderer) -> None:
        self.renderer = renderer

    def draw(self): pass

    def resize(self, factor): pass

class Circle(Shape):

    def __init__(self, renderer: Render, radius) -> None:
        super().__init__(renderer)
        self.radius = radius

    def draw(self): 
        self.renderer.render_circle(self.radius)

    def resize(self, factor): self.radius *= factor

if __name__ == "__main__":

    raster = RasterRender()
    vector = VectorRender()

    circle = Circle(vector, 10)
    circle.draw()
    circle.resize(2)
    circle.draw()

    circle_2 = Circle(raster, 4)
    circle_2.draw()
    circle_2.resize(2)
    circle_2.draw()