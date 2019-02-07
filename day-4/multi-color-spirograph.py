
import turtle

t = turtle.Pen()
colors = []
turtle.bgcolor("black")
t.speed(0)

addColor = input("Enter a basic color: ").lower()
while(addColor != ""):
     colors.append(addColor)
     addColor = input("Type a color or press 'Enter' to choose your shape. ").lower()

sides = len(colors)
question = "How many sides would you like your shape to be? "
shape = int(input(question))

while(question != ""):
     if(shape > sides):
          print("Too many, (Maximum of", sides, "sides): ")
          shape = int(input(question))
     else:
          for x in range(shape):
               for y in range(shape):
                    t.pencolor(colors[y%shape])
                    t.forward(50)
                    t.left(360/shape)
               t.right(360/shape)
          break
     
          #if you dont put this 'break' here,
          #your program will run on forever.

