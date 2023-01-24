import random

computer_number = random.randint(1,100)

while True:
    player_number = input("Add number between 1 and 100:")
    if not player_number.isdigit():
        print("Invalid value!")
        continue
    player_number_int = int(player_number)

    if player_number_int > 100 or player_number_int < 1:
        print("Invalid value!")

    if computer_number == player_number_int:
        print("You guess it!")
        break
    elif computer_number > player_number_int:
        print("Too Low!")
    elif computer_number < player_number_int:
        print("Too High!")