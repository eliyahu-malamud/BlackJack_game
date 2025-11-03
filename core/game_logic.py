from core import player_io
def calculate_hand_value(hand: list[dict]) -> int:
    counter = 0
    for i in hand:
        if i['rank'] == 'J' or i['rank'] == 'Q' or i['rank'] == 'K':
            counter += 10
        elif i['rank'] == 'A':
            counter += 1
        else:
            counter += int(i['rank'])
    return counter

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    for i in range(2):
        player['hand'].append(deck.pop(0))
        dealer['hand'].append(deck.pop(0))
    print(f'players hand value: {calculate_hand_value(player['hand'])}')
    print(f'dealers hand value: {calculate_hand_value(dealer['hand'])}')

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while True:
        dealer['hand'].append(deck.pop(0))
        if 17 <= calculate_hand_value(dealer['hand']) < 21:
            return True
        elif calculate_hand_value(dealer['hand']) >= 17 and calculate_hand_value(dealer['hand']) > 21:
            print(f'dealers hand value: {calculate_hand_value(dealer['hand'])}')
            print('the dealer lost the game because he past 21!!')
            print('player wind!!')
            return False

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    while True:
        players_input = player_io.ask_player_action()
        if players_input == 'H':
            player['hand'].append(deck.pop(0))
            if calculate_hand_value(player['hand']) > 21:
                print(f'players hand value: {calculate_hand_value(player['hand'])}.')
                print(f'dealers hand value: {calculate_hand_value(dealer['hand'])}')
                print('player had lost the game because he past 21!!')
                print('dealer wind the game!!')
                break
            elif calculate_hand_value(player['hand']) <= 21:
                print(f'players hand value: {calculate_hand_value(player['hand'])}.')
                continue
        elif players_input == 'S':
            a = dealer_play(deck, dealer)
            if not a:
                break
            if a:
                p = calculate_hand_value(player['hand'])
                d = calculate_hand_value(dealer['hand'])
                print(f'players hand value: {p}')
                print(f'dealers hand value: {d}')
                if p > d:
                    print('player wind because he is bigger by value!!')
                    break
                elif p < d:
                    print('dealer wind because he is bigger by value!!')
                    break
                else:
                    print('draw!!')
                    break



















