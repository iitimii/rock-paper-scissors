import random
# r > s, s > p, p > r
def play():
    round = 1
    round_limit = 4
    comp_score = 0
    user_score = 0


    while round < round_limit:
        print(f"Round {round}")
        computer = random.choice(["r", "s", "p"])
        user = input("rock(r), paper(p), scissors(s)\n")
        if computer == "r":
            print(f"Computer picks rock")
        if computer == "s":
            print(f"Computer picks scissors")
        if computer == "p":
            print(f"Computer picks paper")
        if winner(user, computer) :
            user_score += 1
            print("User wins this round")
        elif computer == user:
            user_score += 1
            comp_score += 1
            print("The round ends in a draw")
        else:
            comp_score += 1
            print("Computer wins this round")
        round += 1

    print(f"Computer - {comp_score}  User - {user_score}")
    if user_score > comp_score:
        print("User wins !")
    elif comp_score > user_score:
        print("Computer wins!")
    else:
        print("It's a Tie!")


def winner(player , opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

play()