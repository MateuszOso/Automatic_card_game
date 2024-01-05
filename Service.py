# Predicates and methods

def yes_no_answear():

    while True:
        answear = input("T/N").lower()
        if answear == "t" or answear == "n":
            return answear

def end_game_print():

    print("KONIEC GRY! STRACIŁEŚ WSZYSTKIE PIENIĄDZE!\nCZY CHCESZ ZAGRAĆ PONOWNIE?\n")

def game_continuation(answear):
    game_on = False
    start = False
    next_round = False
    if answear == "n":
        print("\nDZIĘKUJĘ ZA GRĘ! NARA!")
        return game_on, start, next_round

    if answear == "t":
        start = True
        print("\n" * 20)
        return game_on, start, next_round


