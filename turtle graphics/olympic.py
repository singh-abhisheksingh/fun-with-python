import turtle

turtle.reset()
turtle.shape('turtle')

def drawingCircle(x, y, color, radius):
	turtle.pensize(11)
	turtle.penup()
	turtle.setposition(x, y)
	turtle.pendown()
	turtle.color(color)
	turtle.circle(radius)

locations = [(90, 0, 'green'), (-90, 0, 'yellow'),(180, 90, 'red'), (0, 90, 'black'), (-180, 90, 'blue')]

if __name__ == '__main__':
	for index in locations:
		drawingCircle(index[0], index[1], index[2], 75)
	turtle.exitonclick()