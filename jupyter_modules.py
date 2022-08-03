def squareFoot():
    length = input("What is the length of your house in feet? ")
    width = input("What is the width of your house in feet? ")
    sqft = int(length) * int(width)

    print(f'Your house is {sqft} square feet.')

def circum():
    radius = input("What is the radius of the circle in inches? ")
    pi = 3.14159265359
    circumference = 2 * pi * int(radius)
    print(f'The circumference of the circle is {round(circumference, 1)} inches.')
