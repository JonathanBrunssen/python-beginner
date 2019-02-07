#Greeting.py
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

ageDif = pythonAge - yourAge

if(ageDif > 0):
     print("I am older than you by ", ageDif, " years.")
else:
     ageDif = ageDif * -1
     print("You are older than me by ", ageDif, " years.")







     
