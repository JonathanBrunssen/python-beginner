# python-beginner-plans

## Day 1:

---

## Intro to python

Go over programming basics and some mathematical concepts such as:

* modulus (denoted in python by the "%" operator)

* exponents (denoted in python by the "\*\*" operator)

* concatenation (denoted in python with the ",")

* syntax of python (explain importance of whitespace, tabbing, etc)

*Note to instructors: this part alone should take up the first half of the class.*

---

## Greeting.py

#### Start with a basic print statement after asking ther age.

```python
#Greeting.py - start
yourName = input("What is your name? ")
print("Nice to meet you ", yourName)
print("My name is Python")
```

#### Expand upon this by asking for their age, explain differences between variable types like string and integer.

```python
yourName = input("What is your name? ")
print("Nice to meet you ", yourName)
print("My name is Python")

#new material
yourAge = input("How old are you? ")
print("You are ", yourAge, " years old.")
print("I am 29 years old.")
#end new material
```

#### Next we will change it so the ages of the user and python are calculated, rather than input directly from the user or hard-coded into the program.

```python
#new material
import datetime
now = datetime.datetime.now()
pythonAge = now.year - 1989 #year that python came out
#end new material

yourName = input("What is your name? ")
print("Nice to meet you ", yourName)
print("My name is Python")

#new material
yourYear = int(input("What year were you born? "))
yourAge = now.year - yourYear
print("You are ", yourAge, " years old.")
print("I am ", pythonAge, " years old.")
#end new material
```

#### Completed project
At this point we add the age difference and print out how much older or younger the user is, compared to python's age.

```python
import datetime
now = datetime.datetime.now()
pythonAge = now.year - 1989

yourName = input("What is your name? ")
print("Nice to meet you ", yourName)
print("My name is Python")

yourYear = int(input("What year were you born? "))
yourAge = now.year - yourYear
print("You are ", yourAge, " years old.")
print("I am ", pythonAge, " years old.")

#new material
ageDif = pythonAge - yourAge

if(ageDif > 0):
     print("I am older than you by ", ageDif, " years.")
else:
     ageDif = ageDif * -1
     print("You are older than me by ", ageDif, " years.")
#end new material
```

---

## Start on [Magic 8 Ball](https://github.com/Fun2LearnCode/python-beginner-plans/tree/master/day-2) if time allows.