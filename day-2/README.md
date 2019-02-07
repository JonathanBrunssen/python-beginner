# python-beginner-plans

## Day 2:

---

## Magic\-8\-Ball

```python
import random

choices = ['yes', 'no', 'maybe', 'it is so', 'cannot tell', 'ask again later',
           'surely', 'definitely not', 'absolutely']
greeting = "Welcome to the Magic 8 Ball"
print(greeting)
question = "Type 'shake' for a prophecy, 'quit' to exit. "
answer = input(question)

while(greeting != ""):
     if(answer == "shake"):
          response = random.choice(choices)
          print("The Magic 8 Ball says: ", response)
          answer = input(question)
     elif(answer == "quit"):
          print("Goodbye...")
          break
     else:
          answer = input(question)
```

Students can edit their list to turn this into a random decision maker app, such as:

* Where to go on vacation

* Where to drop in fornite

* Where to eat dinner

These are some simple examples but it can be expanded upon in class.

---

## Start on [Drawing in Turtle](https://github.com/Fun2LearnCode/python-beginner-plans/tree/master/day-3) if time allows.