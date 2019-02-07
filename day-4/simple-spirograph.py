import turtle

t = turtle.Pen()
colors = ["white","blue","red","green","yellow","orange","grey","purple","gold","brown"]
turtle.bgcolor("black")
t.speed(0)
question = "How many sides would you like your shape to be(max 10). "
shape = int(input(question))

while(question != ""):
    if(shape > len(colors)):
        print("Oops! That was too many sides. Please try again.")
        shape = int(input(question))
    else:
        for x in range(shape):
            for y in range(shape):
                t.pencolor(colors[y%shape])
                t.forward(50)
                t.left(360/shape)
            t.right(360/shape)
        break #if this 'break' isn't here the program will run forever.
