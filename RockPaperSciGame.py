import random
import time
random.seed(time.time())
print("WELCOME TO THE ROCK-PAPER-SCISSORS GAME!!!")
print("Rules:\nRock beats Scissors\nScissors beats Paper\nPaper beats Rock\n")
play=["rock","paper","scissors"]
user,compt=0,0

while True:
    ch=input("Enter your choice (rock/paper/scissors): ")
    if ch.lower() not in play:
        print("Invalid choice! Please choose from - rock/paper/scissors")
        continue
    ch=ch.lower()
    comp=random.choice(play)
    print(f"Your choice: {ch}")
    print(f"Computer's choice:  {comp}")
    if ch==comp:
        print("ITS A TIE :)")
    elif (ch=="rock" and comp=="scissors") or (ch=="paper" and comp=="rock") or (ch=="scissors" and comp=="paper"):
        print("WOOHOO YOU WIN THIS ROUND!!!!")
        user+=1
    else:
        print("MMM...COMPUTER WINS THIS ROUND!!!")
        compt+=1
    print(f"\nCurrent Score:\nYou: {user} | Computer: {compt}\n")
    
    again = input("Do you want to play again? (yes/no): ").lower()
    
    if again != "yes":
        print("Final Score:")
        print(f"You: {user} | Computer: {compt}")
        if user > compt:
            print("Congratulations, you won the game overall!")
        elif user< compt:
            print("The computer won this time. Better luck next round!")
        else:
            print("Haha It's an overall tie!")
        print("\nThanks for playing!")
        break
