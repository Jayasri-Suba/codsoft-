import random

options = ["rock","paper","scissors"]
playing = True

while playing: 

  player = None
  computer = random.choice(options)
  while player not in options:
    player = input("enter your choice (rock, paper, scissors)")

  print(f"player: {player}")
  print(f"computer: {computer}")
    
  if player == computer:
   print("match is tie....")    
  elif player == "rock" and computer == "scissors":
   print("you win.....")
  elif player == "paper" and computer =="rock":
   print("you win.....")
  elif player == "scissors" and computer == "paper":
   print("you win.....")
  else:
   print("you lose......")      

  play_again = input("play again? (yes/no): ").lower()
  if not play_again == "yes":
    playing = False
        
print("thanks for playing rock, paper, scissors....")        