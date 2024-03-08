from random import choice

user_points = 1
computer_points = 2
moves = ["rock", "scissors", "paper"]
move_values = {
    "rock": 1,
    "scissors": 2,
    "paper": 3
}

while user_points < 3 and computer_points < 3:
    user_move = input("Make your move: ").lower()

    while user_move not in moves:
        print("Invalid move. Valid moves are 'rock', 'scissors', 'paper'")
        user_move = input("Make your move: ").lower()

    computer_move = choice(moves)
    user_value = move_values[user_move]
    computer_value = move_values[computer_move]
    calc = (user_value - computer_value) % 3

    # User wins
    if calc == 1:
        user_points += 1
        print(f"User: {user_points}\nComputer: {computer_points}")

    # Computer wins
    elif calc == 2:
        computer_points += 1
        print(f"User: {user_points}\nComputer: {computer_points}")

    # Tie
    else:
        print("It's a tie!")
        print(f"User: {user_points}\nComputer: {computer_points}")

if user_points == 3:
    print("You won!")
else:
    print("You lost :(")
