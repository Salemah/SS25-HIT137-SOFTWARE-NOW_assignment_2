import turtle

# setup the screen and turle for the coding
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Question 3 - Soharub - group 29")

t = turtle.Turtle()
t.speed(0)  
t.color("black")

def draw_edge(length, depth):
    """
    Recursive function to draw an edge with an inward indentation.
    Splits the line into 4 segments of length/3. As like as the question said.
    """
    if depth == 0:
        t.forward(length)
    else:
        new_length = length / 3
        
        
        draw_edge(new_length, depth - 1)
        
        # Here I coded the inward indentation (60 degrees right)
        t.right(60) 
        draw_edge(new_length, depth - 1)
        
        # Here Completing the triangle (120 degrees left)
        t.left(120)
        draw_edge(new_length, depth - 1)
        
        #Back to original orientation
        t.right(60)
        draw_edge(new_length, depth - 1)

def draw_polygon(sides, length, depth):
    angle = 360 / sides
    for _ in range(sides):
        draw_edge(length, depth)
        t.right(angle) 

def main():
    try:
        # Prompt from the user 
        sides = int(input("Enter the number of sides: "))
        length = int(input("Enter the side length (e.g., 300): "))
        depth = int(input("Enter the recursion depth (e.g., 3): "))

        # Input Validation
        if sides < 3:
            print("A polygon must have at least 3 sides.")
            return

        t.penup()
        t.goto(-length/2, length/2)
        t.pendown()

        # Generate the pattern
        draw_polygon(sides, length, depth)
        
        # Final output
        t.hideturtle()
        print("Pattern generated successfully!")
        turtle.done()

    except ValueError:
        print("Please enter valid integers for all inputs.")

if __name__ == "__main__":
    main()
