
# draw Square in Python Turtle using loop (GeeksforGeeks, n.d.).
import turtle

t = turtle.Turtle()

# input for user to choose side length with integer check
while True:
    try:
        s = int(input("Enter the length of the side of the square: "))
        break  # Exit loop if input is a valid integer
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

for _ in range(4):
    t.forward(s) # Forward turtle by s units
    t.left(90) # Turn turtle by 90 degree
# keep the window open so you can admire your square
turtle.done()
