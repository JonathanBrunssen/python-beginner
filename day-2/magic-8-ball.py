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
