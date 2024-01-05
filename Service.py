# Predicates and methods

def yes_no_answear():

    while True:
        answear = input("T/N").lower()
        if answear == "t" or answear == "n":
            return answear

def end_game_print():

    print("KONIEC GRY! STRACIŁEŚ WSZYSTKIE PIENIĄDZE!\nCZY CHCESZ ZAGRAĆ PONOWNIE?\n")

def game_continuation(answear):

    if answear == "n":
        print("\nDZIĘKUJĘ ZA GRĘ! NARA!")
        game_on = False
        start = False
        next_round = False
    if answear == "t":
        print("\n" * 20)
        game_on = False
        next_round = False

