from math import *

class Point:

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z


    def __str__(self) -> str:
        return f"x: {self.x} y: {self.y} z: {self.z}"
    
    # We define two staticmethods that return the point whether is rectangular, cilindricas o esfericas
    @staticmethod
    def new_cartesian_point(x,y,z):
        return Point(x, y, z)
    
    @staticmethod
    def new_cilindrical_point(r, theta, z):
        return Point(x = r * cos(theta),
                     y = r * sin(theta),
                     z = z)
    
    @staticmethod
    def new_spherical_point(rho, tita, phi):
        return Point.new_cilindrical_point(
            r = rho * sin(phi),
            theta = tita,
            z = rho * cos(phi)
        )


# Rectangular points
r_point_1 = Point.new_cartesian_point(2,3,1) 
r_point_2 = Point.new_cartesian_point(5,3,15) 
r_point_3 = Point.new_cartesian_point(2,6,3) 

print(r_point_1, r_point_2, r_point_3)

c_point_1 = Point.new_cilindrical_point(5, pi/4, 4)
c_point_2 = Point.new_cilindrical_point(4, 2/3* pi, -2)

print(c_point_1, c_point_2)