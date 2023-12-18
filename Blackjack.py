# importowanie modułów

from Deck import Deck
from Hand import Hand
from Croupier import Croupier


# Initial
start = True
while start:
    print("**********************************")
    print("*     BLACKJACK BY MATOSENS      *")
    print("**********************************")

    name = input("IMIĘ: ")
    player = Hand(name)
    print(f"WITAJ W BLACKJACK {player.name}!")

    croupier = Croupier()
    deck = Deck()
    deck.shuffle()
    player_cards = []
    croupier_cards = []
    player.amount_money()
    input(f"!!!{player.money}!!! JAZDA! ZACZYNAMY!   [WCIŚNIJ ENTER]")
    player.chip_hand()
    player.show_my_chips()
    # TODO, listy, pętle itp. zaczynamy od zero - DONE
    turn = 0
    all_in = "n"

    while True:

        decision_t_n = input("Czy chcesz rozmienić jakiś żeton?  (T/N)\n").lower()
        # TODO, odczytywane znaki zawsze sprowadzaj do małej litery, dzięki temu będziesz miał mniej warunków - DONE
        while decision_t_n not in ("t", "n"):
            decision_t_n = input("Wpisz  (T/N)\n").lower()
        if decision_t_n == "n":
            break
        [token1, token2] = player.exchange_choice(decision_t_n)
        player.exchange(int(token1), int(token2))
        input("GOTOWE!   [WCIŚNIJ ENTER]")
        player.show_my_chips()

    # Game Logic

    game_on = True

    while game_on:

        if turn != 0:
            deck = Deck()
            deck.shuffle()
            player_cards = []
            croupier_cards = []
            all_in = "n"

        player_bet = player.bet_money()
        bet_acceptance = player.checker(player_bet)

      #TODO, jako ostatnie. Wszystkie teksty w jednym pliku, łatwo odczytywalnym (nie lista, nie array, nie zbiór)
        while bet_acceptance == "t" or bet_acceptance == "n":
            while bet_acceptance == "n":
                input("W takim razie obstaw inną kwotę!   [WCIŚNIJ ENTER]")
                # TODO, muszisz (dla samego siebie) starać się jak najlepiej nazywać zmienne - DONE
                player_bet = player.bet_money()
                bet_acceptance = player.checker(player_bet)
            if bet_acceptance == "t":
                exchange = player.exchange_choice(bet_acceptance)
                player.exchange(exchange[0], exchange[1])
                input("GOTOWE!   [WCIŚNIJ ENTER]")
                player.show_my_chips()
                bet_acceptance = player.checker(player_bet)

        bet_chips_list = player.bet(player_bet)
        input(f"KWOTA OBSTAWIONA!. POZOSTAŁO CI {player.money} zł.   [WCIŚNIJ ENTER]")
        input("KRUPIER LOSUJE KARTY!   [WCIŚNIJ ENTER]")
        print("\n" * 20)

        round_no = 0
        croupier_round = 0
        player_sum = 0
        croupier_sum = 0
        next_round = True
        while next_round:

            if round_no == 0:
                for x in range(2):
                    card = deck.take_one()
                    player_cards.append(card)
                    player_sum += card.value

                print("Moje karty to:")
                player.show_cards(player_cards)

            if round_no == 0:
                for x in range(2):
                    card = deck.take_one()
                    croupier_cards.append(card)
                    croupier_sum += card.value

                print("\n" * 2)
                print("Karty krupiera to:")
                print(f"{croupier_cards[0]}")
                print("Druga karta krupiera jest zakryta.")

            if round_no == 0:
                for card in player_cards:
                    if card.rank == "As":
                        card.value = deck.ace(card)
                        player_sum += card.value
            else:
                card = player_cards[round_no + 1]
                if card.rank == "As":
                    card.value = deck.ace(card)
                    player_sum += card.value
                count = 0
                for card in player_cards:
                    count += 1
                    # TODO, logika kart do dictionary albo podobnego typu - DONE


                    if card.rank == "As":
                        if count != len(player_cards):
                            ace_changer = "x"
                            # TODO, Powtarzalny kod powinien zostać wyniesiony do osobnej encji lub serwisu
                            while ace_changer not in ("t","n"):
                                ace_changer = input(f"Czy chcesz zmienić wartość swojego {card.__str__()}?({card.value}) (T/N)\n").lower()
                                if ace_changer == "t":
                                    card.value = deck.ace(card)
                                    if card.value == 1:
                                        player_sum -= 11
                                    else:
                                        player_sum -= 1
                                    player_sum += card.value
                                if ace_changer == "n":
                                    print(f"Okej, wartoś Asa nadal wynosi {card.value}.")

            if round_no == 0 and player_sum == 21:
                print("\n   BLACKJACK!")
                player.blackjack(bet_chips_list, player_bet)
                player.show_my_chips()
                print(f"Moje środki to: {player.money}zł\n")
                next_round = False
                turn += 1
                break

            if player_sum > 21:
                print("\n")
                print("PRZEGRANA! SUMA KART WIĘKSZA NIŻ 21! TRACISZ ŻETONY!")
                player.show_my_chips()
                print(f"Moje środki to: {player.money}zł\n")
                if player.money == 0:
                    continued = "X"
                    # TODO, Warunki można wynieść do metod i później się tylko do nich odwoływać (predicate, google it)
                    # TODO, na przykład plik ValidationService, który będzie zawierał metodę yes_no_answer
                    while continued not in ("n", "t"):
                        continued = input("KONIEC GRY! STRACIŁEŚ WSZYSTKIE PIENIĄDZE!\nCZY CHCESZ ZAGRAĆ PONOWNIE?   (T/N)").lower()
                        if continued == "n":
                            print("\nDZIĘKUJĘ ZA GRĘ! NARA!")
                            game_on = False
                            start = False
                            next_round = False
                            break
                        if continued == "t":
                            print("\n" * 20)
                            game_on = False
                            next_round = False
                            break

                else:
                    print("\n" * 2)
                    player_decision = "0"
                    next_round = False
                    turn += 1
                    break

            else:
                player_decision = 0
                print("\n" * 2)
                print("Wybierz co chcesz zrobić, przez wybranie 1 lub 2:")
                # TODO, dobra praktyka czyli duże listy, duże zbiory, staramy się procesować jako obiekt, albo drzewo ze względów na preformance
                # Big O notation (google it)
                while player_decision not in ['1', '2']:
                    player_decision = input("1 - Pas \n2 - Dobieram \n")
                    if player_decision not in ['1', '2']:
                        print("Wpisz 1 lub 2")

                if player_decision == "2":
                    print("\n" * 20)
                    print("Krupier dodaje kartę do Twojej ręki.\n")
                    card = deck.take_one()
                    player_cards.append(card)
                    player_sum += card.value
                    round_no += 1
                    print("Moje karty to:")
                    player.show_cards(player_cards)
                    print("\n" * 2)
                    print("Karty krupiera to:")
                    print(f"{croupier_cards[0]}")
                    print("Druga karta krupiera jest zakryta.")
                    if player_sum == 21:
                        print("\nSUMA TWOICH KART TO 21! WYGRANA!")
                        player.win_bet(bet_chips_list, player_bet)
                        player.show_my_chips()
                        print(f"Moje środki to: {player.money}zł\n")
                        next_round = False
                        player_decision = "0"
                        turn += 1
                        break

                while player_decision == "1":
                    croupier_round += 1
                    if croupier_round == 1:
                        ace_checker = 0
                        print("\nKrupier odsłania swoją drugą kartę.\n")
                        print("Moje karty to:")
                        player.show_cards(player_cards)
                        print("\n" * 2)
                        print("Karty krupiera to:")
                        croupier.show_cards(croupier_cards)

                        for card in croupier_cards:
                            if card.rank == "As" and ace_checker == 0:
                                card.value = 11
                                croupier_sum += 11
                                ace_checker += 1
                                continue
                            if card.rank == "As" and ace_checker == 1:
                                card.value = 1
                                croupier_sum += 1
                                ace_checker += 1
                        if croupier_sum == 21:
                            print("\nPRZEGRANA! SUMA KART KRUPIERA TO 21!")
                            player.show_my_chips()
                            print(f"Moje środki to: {player.money}zł\n")

                            if player.money == 0:
                                continued = "X"
                                while continued not in ("n", "t"):
                                    continued = input("KONIEC GRY! STRACIŁEŚ WSZYSTKIE PIENIĄDZE!\nCZY CHCESZ ZAGRAĆ PONOWNIE?   (T/N)").lower()
                                    if continued == "n":
                                        print("\nDZIĘKUJĘ ZA GRĘ! NARA!")
                                        game_on = False
                                        start = False
                                        player_decision = "0"
                                        next_round = False
                                        break
                                    if continued == "t":
                                        print("\n" * 20)
                                        game_on = False
                                        player_decision = "0"
                                        next_round = False
                                        break
                            else:
                                print("\n" * 2)
                                player_decision = "0"
                                next_round = False
                                turn += 1
                                break
                    else:
                        croupier_count = 2
                        while croupier_sum < 17:
                            croupier_compare = 0
                            card = deck.take_one()
                            croupier_cards.append(card)
                            if card.rank == "As":
                                card.value = 11
                            croupier_sum += card.value
                            for card in croupier_cards:
                                if croupier_sum > 21 and card.value == 11:
                                    card.value = 1
                                    croupier_sum -= 10
                                if croupier_count == croupier_compare:
                                    print(card)
                                else:
                                    croupier_compare += 1
                            croupier_count += 1
                        if croupier_sum > 21:
                            print("\nSUMA KART KRUPIERA WYŻSZA NIŻ 21! WYGRANA")
                            player.win_bet(bet_chips_list, player_bet)
                            player.show_my_chips()
                            print(f"Moje środki to: {player.money}zł\n")
                            next_round = False
                            player_decision = "0"
                            turn += 1
                            break
                        if croupier_sum == 21:
                            print("\nPRZEGRANA! SUMA KART KRUPIERA TO 21!")
                            player.show_my_chips()
                            print(f"Moje środki to: {player.money}zł\n")
                            if player.money == 0:
                                continued = "X"
                                while continued not in ("n", "t"):
                                    continued = input(
                                        "KONIEC GRY! STRACIŁEŚ WSZYSTKIE PIENIĄDZE!\nCZY CHCESZ ZAGRAĆ PONOWNIE?   (T/N)").lower()
                                    if continued == "n":
                                        print("\nDZIĘKUJĘ ZA GRĘ! NARA!")
                                        game_on = False
                                        start = False
                                        player_decision = "0"
                                        next_round = False
                                        break
                                    if continued == "t":
                                        print("\n" * 20)
                                        game_on = False
                                        player_decision = "0"
                                        next_round = False
                                        break
                            else:
                                print("\n" * 2)
                                player_decision = "0"
                                next_round = False
                                turn += 1
                                break

                        if croupier_sum < 21 and player_sum < croupier_sum:
                            print("\nPRZEGRANA! SUMA KART KRUPIERA WYŻSZA OD TWOJEJ!")
                            player.show_my_chips()
                            print(f"Moje środki to: {player.money}zł\n")
                            if player.money == 0:
                                continued = "X"
                                while continued not in ("n", "t"):
                                    continued = input(
                                        "KONIEC GRY! STRACIŁEŚ WSZYSTKIE PIENIĄDZE!\nCZY CHCESZ ZAGRAĆ PONOWNIE?   (T/N)").lower()
                                    if continued == "n":
                                        print("\nDZIĘKUJĘ ZA GRĘ! NARA!")
                                        game_on = False
                                        start = False
                                        player_decision = "0"
                                        next_round = False
                                        break
                                    if continued == "t":
                                        print("\n" * 20)
                                        game_on = False
                                        player_decision = "0"
                                        next_round = False
                                        break

                            else:
                                print("\n" * 2)
                                player_decision = "0"
                                next_round = False
                                turn += 1
                                break

                        if croupier_sum < 21 and player_sum > croupier_sum:
                            print("\nSUMA KART GRACZA WYŻSZA NIŻ KRUPIERA! WYGRANA")
                            player.win_bet(bet_chips_list, player_bet)
                            player.show_my_chips()
                            print(f"Moje środki to: {player.money}zł\n")
                            next_round = False
                            player_decision = "0"
                            turn += 1
                            break

                        if croupier_sum < 21 and player_sum == croupier_sum:
                            print("\nREMIS! OBSTAWIONA KWOTA WRACA DO CIEBIE!")
                            player.draw(bet_chips_list, player_bet)
                            player.show_my_chips()
                            print(f"Moje środki to: {player.money}zł\n")
                            next_round = False
                            player_decision = "0"
                            turn += 1
                            break
