from math import *

class Point:

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z


    def __str__(self) -> str:
        return f"x: {self.x} y: {self.y} z: {self.z}"


class PointFactory:   
    # No need to define these methods as static
    
    def new_cartesian_point(self,x,y,z):
        return Point(x, y, z)
    
    
    def new_cilindrical_point(self,r, theta, z):
        return Point(x = r * cos(theta),
                     y = r * sin(theta),
                     z = z)
    
    def new_spherical_point(self,rho, tita, phi):
        return Point.new_cilindrical_point(
            r = rho * sin(phi),
            theta = tita,
            z = rho * cos(phi)
        )

point_factory = PointFactory()

# Rectangular points
r_point_1 = point_factory.new_cartesian_point(2,3,1) 
r_point_2 = point_factory.new_cartesian_point(5,3,15) 
r_point_3 = point_factory.new_cartesian_point(2,6,3) 

print(r_point_1, r_point_2, r_point_3)

c_point_1 = point_factory.new_cilindrical_point(5, pi/4, 4)
c_point_2 = point_factory.new_cilindrical_point(4, 2/3* pi, -2)

print(c_point_1, c_point_2)