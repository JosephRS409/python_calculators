# Function Practice
import math
#square_area = 0.0
#rectangle_area = 0.0
#circle_area = 0.0
def compute_area_square(length):
    '''Computes the area of a square'''
    #square_area = (length**2)
    square_area = compute_area_rectangle(length, length)
    return square_area
def compute_area_rectangle(width, length):
    '''Computes the area of a square'''
    rectangle_area = width * length
    return rectangle_area
def compute_area_circle(diameter):
    '''Computes the area of a square'''
    circle_radius = diameter/2
    circle_area = circle_radius**2 * math.pi
    return circle_area
def compute_area(shape, value_1, value_2 = 0):
    '''Computes all areas'''
    if(shape == "square"):
        final_area = compute_area_square(value_1)
    elif(shape == "rectangle"):
        final_area = compute_area_rectangle(value_1, value_2)
    elif(shape == "circle"):
        final_area = compute_area_circle(value_1)
    return final_area
answer = ""
while (answer != "quit"):
    answer = input("What shape area are you trying to compute? \n\t CIRCLE \n\t RECTANGLE \n\t SQUARE \n\t Type QUIT to quit \n\t :: ")
    print()
    if(answer.lower() == "square"):
        length_square = float(input("What is the length of your square? "))
        print()
        final_area = compute_area(answer.lower(), length_square)
        print(f"The area of the square is {final_area}.")
        
    elif(answer.lower() == "circle"):
        diameter = float(input("What is the diameter of your circle? "))
        print()
        final_area = compute_area(answer.lower(), diameter)
        print(f"The area of the circle is {final_area}.")
        
    elif(answer.lower() == "rectangle"):
        width = float(input("What is your rectangle width? "))
        length_rectangle = float(input("What is your rectangle length? "))
        print()
        final_area = compute_area(answer.lower(), width, length_rectangle)
        print(f"The area of the rectangle is {final_area}.")
    print()
