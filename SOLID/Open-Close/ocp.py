"""

Sumary

Open for extension and closed for modifications

After you've written and tested a paticular class or feature, you should not modify it. Instead, you should extend it.

For this particular case, Specifications can be used.

"""

from enum import Enum

class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product():
    def __init__(self, 
                 name: str, 
                 color: Color, 
                 size: Size
    ) -> None:
        self.name = name
        self.color = color
        self.size = size

    def __str__(self) -> str:
        return self.name

# Bad Approach
class BadFilter():

    def filter_by_color(self, 
                        color, 
                        products: list[Product]) -> Product | None:
        """ Function to check whether the producto color matchs with the color we are filtering"""
        for i in products:
            if i.color == color:
                yield i

    def filter_by_size(self, 
                       size, 
                       products: list[Product]) -> Product | None:
        for p in products:
            if p.size == size:
                yield p

    def filter_by_color_and_size(self, 
                                 color,
                                 size,
                                 products: list[Product]) -> Product | None:
        for p in products:
            if p.color == color and p.size == size:
                yield p


# SOLUTION USING OPEN CLOSE PRINCIPLE -> Open for extension, closed for modification
# First we define a class called specification that will be used to define the filtering criteria. It will be used as an interface
class FilterSpecification():
    """ We define a method that checks if the spec is satisfied """
    def is_satisfied(self):
        pass

# Now we define the both critaria we can use for filtering
class ColorSpecification(FilterSpecification):
    def __init__(self, 
                 color: Color) -> None:
        self.color = color

    def is_satisfied(self, 
                     item: Product) -> bool:
        """ We check if the item we are passing meets the spec """
        return self.color == item.color
    
class SizeSpecification(FilterSpecification):
    def __init__(self, 
                 size: Size) -> None:
        self.size = size

    def is_satisfied(self, 
                     item: Product) -> bool:
        """ We check if the item we are passing meets the spec """
        return self.size == item.size


# Then we define a better filter interface
class BetterFilter():
    def filter(self, 
               items: list[Product], 
               spec: ColorSpecification | SizeSpecification
    ):
        for item in items:
            if spec.is_satisfied(item):
                yield item # Yield return and object that can be iterated

if __name__ == "__main__":
    apple = Product("apple", Color.RED, Size.SMALL)
    green_apple = Product("green apple", Color.GREEN, Size.SMALL)
    tree = Product("tree", Color.GREEN, Size.MEDIUM)
    house = Product("house", Color.BLUE, Size.LARGE)

    product_cataloge = [apple, green_apple, tree, house]

    # Check products
    for i in product_cataloge:
        print(i)

    """ BAD APPROACH """
    # filter products using bad approach
    pf = BadFilter()
    # First we filter by color
    for i in pf.filter_by_color(Color.RED, product_cataloge):
        print(f"{i} is red")
    # Now we filter by size
    for i in pf.filter_by_size(Size.LARGE, product_cataloge):
        print(f"{i} is Large")

    """ BETTER APROACH USING OCP"""
    print(
        """ 
####################################################################################
using OCP
####################################################################################
        """    
    )
    bf = BetterFilter()
    green = ColorSpecification(Color.GREEN)
    for i in list(bf.filter(product_cataloge, green)):
        print(f"{i} is green")

    large = SizeSpecification(Size.LARGE)
    for i in list(bf.filter(product_cataloge, large)):
        print(f"{i} is large")

    # TODO
    # 1) Implement and and or filters