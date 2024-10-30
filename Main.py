
def main():
    stones = 20
    player_tracker = 0
    losing_player = "Player"
    while stones > 1:
        print("There are", stones, "stones left.")
        if player_tracker == 0:
            print("Player One:")
            player_tracker = player_tracker = 1
        else:
            print("Player Two:")
            player_tracker = player_tracker - 1
        user_input = int(input("Would you like to remove 1 or 2 stones? "))
        if user_input == 1:
            stones = stones - 1
        elif user_input == 2:
            stones = stones - 2
        elif user_input != 1 or 2:
            print("Please enter 1 or 2.")
        print()
    while stones == 1:
        print("There is 1 stone left.")
        if player_tracker == 0:
            print("Player One:")
            player_tracker = player_tracker = 1
        else:
            print("Player Two:")
            player_tracker = player_tracker - 1
        user_input = int(input("Would you like to remove 1 or 2 stones? "))
        if player_tracker == 1:
            losing_player = "Player One"
        else:
            losing_player = "Player Two"
            print("Sorry,", losing_player, "you lose!")
    if stones == 0:
        print("Game over!")




if __name__ == '__main__':
    main()