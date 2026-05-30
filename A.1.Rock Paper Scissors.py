import random
rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_movie = input("Choose [r]ock, [p]aper, or [s]cissors: ")

if player_movie == "r":
    player_movie = rock
elif player_movie == "p":
    player_movie = paper
elif player_movie == "s":
    player_movie = scissors
else:
    raise SystemExit("Invalid input. Try again...")

computer_random_number = random.randint(1, 3)
computer_movie = " "

if computer_random_number == 1:
    computer_movie = rock
elif computer_random_number == 3:
    computer_movie = paper
else:
    computer_movie = scissors
print(f"The computer chose {computer_movie}.")

if (player_movie == rock and computer_movie == scissors) or (player_movie == paper and computer_movie == rock) or (player_movie == scissors and computer_movie == paper):
    print("You win!")
elif player_movie == computer_movie:
    print("Draw!")
else:
    print("You lose!")