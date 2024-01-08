# Predicates and methods

def yes_no_answear():

    while True:
        answear = input("Wybierz (T/N)\n").lower()
        if answear == "t" or answear == "n":
            return answear

def end_game_print():

    print("KONIEC GRY! STRACIŁEŚ WSZYSTKIE PIENIĄDZE!\nCZY CHCESZ ZAGRAĆ PONOWNIE?\n")

def game_continuation(answear):
    game_on = False
    start = False
    player_decision = "0"
    next_round = False
    if answear == "n":
        print("\nDZIĘKUJĘ ZA GRĘ! NARA!")
        return game_on, start, player_decision, next_round

    if answear == "t":
        start = True
        print("\n" * 20)
        return game_on, start, player_decision, next_round

def next_turn(turn):
    print("\n" * 2)
    player_decision = "0"
    next_round = False
    turn += 1

    return player_decision, next_round, turn


