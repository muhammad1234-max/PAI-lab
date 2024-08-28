import math

def area_trapezoid( b, a, h):
    return 0.5*(a+b)*h

def area_parrallelogram(base, height):
    return 0.5*base*height

def cylinder(radius, height, option):
    if(option == "surface area"):
        return (2*math.pi*radius*height) + (2*math.pi*radius*radius)
    else:
        return math.pi*radius*radius*height
    
print("area of traperzium: ", area_trapezoid(4,5,6))
print("area of parrallelogram: ", area_parrallelogram(4,6))
print("surface area of cylinder: ",cylinder(4,5,"surface area"))
print("volume of cylinder: ", cylinder(4,5,"volume"))
