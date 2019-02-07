import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = []
addColor = input("type in a basic color. ")
while addColor != "":
    colors.append(addColor)
    addColor = input("Type a basic color or press enter to see a spiral")
for x in range(1000):
    t.pencolor(colors[x%len(colors)])
    t.forward(x)
    t.left(60)
    

