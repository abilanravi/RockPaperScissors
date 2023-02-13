import random

def game():
    user = input("Please select one of the options \n'r' for rock, 's' for scissors, 'p' for paper:")
    comp = random.choice(['r', 's', 'p'])

    print("You chose " + user)

    if user != ('r' or 's' or 'p'):
        print("Please make a valid selection")
    elif user == comp:
        print("Computer picks " + comp)
        print("It's a tie!")
    elif (user == 'p' and comp == 'r') or (user == 'r' and comp == 's') or (user == 's' and comp == 'p'):
        print("Computer picks " + comp)
        print("You win!")
    else:
        print("Computer picks " + comp)
        print("You lose!")

print(game())