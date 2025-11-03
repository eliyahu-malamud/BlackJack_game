import random
def create_card(rank:str, suite:str) -> dict:
    return {'rank': rank, 'suite': suite}

def build_standard_deck() -> list[dict]:
    my_list = []
    rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suite = ['H', 'S', 'D', 'C']
    for x in suite:
        for y in rank:
            my_list.append(create_card(y, x))
    return my_list

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    flag = swaps
    while flag:
        i = random.randint(0, 51)
        j = random.randint(0, 51)
        if i == j:
            continue
        elif deck[i]['suite'] == 'H' and j % 5 != 0:
            continue
        elif deck[i]['suite'] == 'c' and j % 3 != 0:
            continue
        elif deck[i]['suite'] == 'D' and j % 2 != 0:
            continue
        elif deck[i]['suite'] == 'S' and j % 7 != 0:
            continue
        deck[i], deck[j] = deck[j], deck[i]
        flag -= 1
    return deck




