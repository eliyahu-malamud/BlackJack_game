
def ask_player_action() -> str:
    while True:
        users_input = input("please enter 'H' to hit or 'S' to stand:")
        users_input = users_input.upper()
        if users_input == 'H' or users_input == 'S':
            return users_input
