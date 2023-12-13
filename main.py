rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
bot_choice = random.randint(0,2)

if user_choice<0 or user_choice > 2:
  print("You input a Wrong number. You Lose !")
else:
  if user_choice==0:
    if bot_choice==0:
      print(f"You Choose: {rock}\n Computer choose {rock} \n Its a draw !")
    elif bot_choice==1:
      print(f"You Choose: {rock}\n Computer choose {paper} \n You Lose!")
    elif bot_choice==2:
      print(f"You Choose: {rock}\n Computer choose: {scissors} \n You Win!")
      
  elif user_choice==1:
    if bot_choice==0:
      print(f"You Choose: {paper}\n Computer choose {rock} \n You Win!")
    elif bot_choice==1:
      print(f"You Choose: {paper}\n Computer choose {paper} \n Its a Draw!")
    elif bot_choice==2:
      print(f"You Choose: {paper}\n Computer choose: {scissors} \n You Lose!")

  elif user_choice==2:
    if bot_choice==0:
      print(f"You Choose: {scissors}\n Computer choose {rock} \n You lose !")
    elif bot_choice==1:
      print(f"You Choose: {scissors}\n Computer choose {paper} \n You Win!")
    elif bot_choice==2:
      print(f"You Choose: {scissors}\n Computer choose: {scissors} \n Its a Draw!")
    
    

