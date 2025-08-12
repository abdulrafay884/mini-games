import random

computer = random.choice([-1,0,1])

youstr = input("Enter Choice: ")

youDict = {"r":1 , "p":0 , "s":-1}

reverseDict = {1:"Rock" , 0:"Paper" , -1:"Scissor"}

you = youDict[youstr]

print(f"You Chose {reverseDict[you]}\n Computer Chose {reverseDict[computer]}")

''' IT EASY  BUT WE HAVE TO WRITE MORE

if(computer == you):
    print("Its A Draw!")
else:
    if(computer == 1 and you == -1):   (computer - you) = 2 expalin in the bracket 
    (computer = 1 and you = -1 ke to 1 - (-1)and that is two )
        print("You Lose!"

    elif(computer == 1 and you == 0):  (computer - you) = 1 expalin in the bracket 
    (computer = 1 and you = 0 ke to 1 - 0 and that is one  )
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
'''




#ITS DIFFICULT AND HARD TO READ FOR SOMEONE ELSE BUT ITS SHORT
#THIS QUESTION IS DONE BY THE UPPER LOGIC
if(computer == you):
    print("Its A Draw!")
else:
    if((computer - you) == -1 or (computer - you) == 2 ): 
        print("You Lose!")
    else:
        print("You Win!")