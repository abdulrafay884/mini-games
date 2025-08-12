import random

computer = random.choice([-1,0,1])
youstr = input("Enter Choice: ")
youDict =  {"r": 1 , "p": 0 , "s": -1 }
reverseDict = { 1: "Rock", 0: "Paper", -1: "Scissor" }
you = youDict[youstr]
print(f"You Chose {reverseDict[you]}\n  Computer Chose {reverseDict[computer]}")
if(computer == you):
    print("Its A Draw!")
else:
    if(computer == 1 and you == -1):
        print("You Lose!")
    elif(computer == 1 and you == 0):
        print("You Win!")        
    elif(computer == -1 and you == 1):
        print("You Win!")    
    elif(computer == -1 and you == 0):
        print("You Lose!")
    elif(computer == 0 and you == 1):
        print("You Lose!")        
    elif(computer == 0 and you == -1):
        print("You Win!")    
    else:
        print("Invalid Choice")    