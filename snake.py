import random

choices = {
    "stone": 1,
    "paper": 2,
    "sciser": 3
}

reverse = {
    1: "stone",
    2: "paper",
    3: "sciser"
}

user = input("Enter stone, paper or sciser: ").lower()

if user not in choices:
    print("Invalid choice!")
else:
    user_choice = choices[user]
    computer_choice = random.randint(1, 3)

    print("Computer chose:", reverse[computer_choice])

    if user_choice == computer_choice:
        print("Draw!")

    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        print("You won!")

    else:
        print("You lost!")