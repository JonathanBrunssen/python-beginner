# python-beginner-plans

## Day 4:

---

### Spirograph

```python
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
```

This is a variation on the last project, simply making a spirograph. User inputs the number of sides of the shape they want and the computer calculates the rest to draw the shapes. Once again, allow the students to experiment with adding more or fewer colors to their list. Encourage creativity.

---

## Multi\-Color Spiral

```python
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
```

This is an expansion of the previous projects.

---

## Multi\-Color Spirograph

```python
import turtle

t = turtle.Pen()
colors = []
turtle.bgcolor("black")
t.speed(0)

addColor = input("Enter in a basic color: ")
while addColor != "":
    colors.append(addColor)
    addColor = input("Type a basic color or press 'Enter' to choose your shape: ")

sides = len(colors)

question = "How many sides would you like your shape to be?"    
shape = int(input(question))

while(question != ""):
    if(shape > len(colors)):
        print("Oops! That was too many sides. Please try again. (Maximum of", sides, "sides): ")
        shape = int(input(question))
    else:
        for x in range(shape):
            for y in range(shape):
                t.pencolor(colors[y%shape])
                t.forward(50)
                t.left(360/shape)
            t.right(360/shape)
        break #if this 'break' isn't here the program will run forever.
```

This is a combination of the previous projects.

---

## Start on [Draw A Card](https://github.com/Fun2LearnCode/python-beginner-plans/tree/master/day-5) if time allows.
