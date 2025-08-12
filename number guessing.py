import random
a = -1
b = random.randint(1,123)
guesses = 0
while (a!=b):
    guesses+=1
    a = int(input("Enter A Number And Guess The Right Number:"))
    if(a == b):
      print("Your Guess Right")
    elif(a>b):
       print("Your Guess Too High")    
    elif(a<b):
       print("Your Guess Too Low")    
    else:
      print("Invalid Choice")    

print(f"You Guess Correct Number {b} in {guesses} Attempts")      