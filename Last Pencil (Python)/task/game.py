import string
import random


def get_condition(player1, player2):
    while True:
        numbers = input("How many pencils would you like to use:\n")
        if not numbers.isdigit() or int(numbers) < 0:
            print("The number of pencils should be numeric")
            continue
        if int(numbers) == 0:
            print("The number of pencils should be positive")
            continue
        numbers = int(numbers)
        break
    while True:
        first = input(f"Who will be the first ({player1}, {player2})?\n")
        if first not in (player1, player2):
            print(f"choose between {player1} and {player2}")
            continue
        break
    return numbers, first


def main():
    players = ["John", "Jack"]
    symbol = "|"
    max_pencil_per_turn = 3
    numbers, first = get_condition(*players)
    index = (players.index(first) + 1) % len(players)
    bot = 1
    while numbers:
        print(numbers * symbol)
        index = (index+1) % len(players)
        print(f"{players[index]}'s turn:")
        if index == bot:
            if numbers == 1:
                pick = 1
            elif numbers % 4 == 1:
                pick = random.randint(1, max_pencil_per_turn)
            else:
                pick = numbers % 4 - 1
                if pick < 0:
                    pick = 3
            print(pick)
        else:
            while True:
                pick = input("")
                if not pick.isdigit() or not 1 <= int(pick) <= max_pencil_per_turn:
                    print(f"Possible values: {', '.join(f'{string.punctuation[6]}{a}{string.punctuation[6]}' for a in range(1, max_pencil_per_turn + 1))}")
                    continue
                if int(pick) > numbers:
                    print("Too many pencils were taken")
                    continue
                break
        numbers -= int(pick)
    index = (index + 1) % len(players)
    print(f"{players[index]} won!")


if __name__ == "__main__":
    main()
