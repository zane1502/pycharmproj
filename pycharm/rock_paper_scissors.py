from random import choice

input_list = ["rock", "paper", "scissors"]


while True:
    computer_user = choice(input_list)
    human_user = input("\nRock, Paper or Scissors?")

    if human_user.lower() == "q" or human_user.lower() == "quit":
        print("\nSee ya!")
        break

    elif human_user.lower() not in input_list:
        print("\nInvalid INPUT!")

    else:
        if human_user == computer_user:
            print("We are tied!")

        if human_user == "rock" and computer_user == "scissors":
            print("You win!")

        if human_user == "scissors" and computer_user == "rock":
            print("You lose!")

        if human_user == "rock" and computer_user == "paper":
            print("You lose!")

        if human_user == "paper" and computer_user == "rock":
            print("You win!")

        if human_user == "paper" and computer_user == "scissors":
            print("You lose!")

        if human_user == "scissors" and computer_user == "paper":
            print("You win!")
