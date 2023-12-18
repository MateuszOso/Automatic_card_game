import Global
from Chip import Chip


class Hand:

    def __init__(self, name):
        self.all_chips = []
        self.all_cards = []
        self.all_chips_list = []
        self.name = name

    def amount_money(self):
        while True:
            try:
                self.money = int(input("Ile pieniędzy wpłacasz?(Max 10000)\n"))
                if self.money in range(1,10001):
                    return self.money
                else:
                    print("Wpisz kwotę od 1 - 10000")
            except ValueError:
                print("Wpisz kwotę cyfrą")


    def chip_hand(self):
        self.technic = self.money
        for token in Global.tokens:
            while self.technic - token >= 0:
                chip = Chip(token)
                self.all_chips.append(chip)
                self.all_chips_list.append(token)
                self.technic -= token

        return self.all_chips and self.all_chips_list

    def exchange_choice(self, decision_t_n):

        while decision_t_n == "t":
            token1 = input("Wpisz który żeton chcesz rozmienić.\n")
            while token1 not in [str(x) for x in self.all_chips_list]:
                token1 = input("Nie masz takiego żetonu! Wpisz jeszcze raz:\n")
            while token1 == "1":
                token1 = input("A na co chcesz rozmienieć 1? Nie da się! Wpisz jeszcze raz:\n")
            token2 = input("Wpisz jakie żetony chcesz dostać.\n")
            while not token2.isdigit():
                token2 = input("Wpisz jakie żetony chcesz dostać cyfrą.\n")
            while int(token2) > int(token1):
                token2 = input("Nie możesz rozmienić mniejszego żetonu na większe! Wpisz jeszcze raz debilu:\n")
            while token2 not in [str(x) for x in Global.tokens]:
                token2 = input("Nie masz takiego żetonu! Wpisz jeszcze raz:\n")
            while token2 == token1:
                token2 = input("Nie możesz rozmienić żetonu na ten sam żeton! Wpisz jeszcze raz debilu:\n")

            return [int(token1), int(token2)]

    def exchange(self, token1, token2):
        new_chips_list = []
        for object in self.all_chips_list:
            if token1 == object:
                self.all_chips_list.remove(object)
                while token1 > 0:
                    if token2 > token1:
                        for token in Global.tokens:
                            while token <= token1 and (token1 - token) >= 0:
                                token1 -= token
                                new_chips_list.append(token)
                    else:
                        new_chips_list.append(token2)
                        token1 -= token2
                self.all_chips_list.extend(new_chips_list)
                return self.all_chips_list.sort(reverse=True)


    def get_card(self, card):
        self.all_cards.append(card)

    def bet_money(self):

        self.bet_check = self.all_chips_list

        while True:

            try:
                player_bet = int(input("Jaką kwotę obstawiasz?\n"))
                if player_bet > self.money:
                    print("Brak wystarczających funduszy.")
                else:
                    return player_bet
            except ValueError:
                print("Podaj wartość cyfrą")


    def checker(self, player_bet):

        org_player_bet = player_bet
        count = 0
        for token in Global.tokens:
            total = 0
            next = "n"
            while token <= player_bet and next == "n":
                if player_bet == 0:
                    break
                if count == (len(self.bet_check) - 1):
                    if player_bet == self.bet_check[-1]:
                        if player_bet - token == 0:
                            player_bet -= token
                            if org_player_bet == self.money:
                                all_in = "y"
                                return all_in
                    if token == 1 and player_bet != 1 and player_bet != 0:
                        decision_t_n = input("Aby obstawić taką kwotę musisz rozmienić żetony. Rozmienić? (T/N)\n").lower()
                        return decision_t_n
                    break
                if token == self.bet_check[count]:
                    count += 1
                    player_bet -= token
                elif token > self.bet_check[count]:
                    while token > total:
                        if count == len(self.bet_check):
                            break
                        total += self.bet_check[count]
                        count += 1
                    if total > token and count != len(self.bet_check):
                        player_bet -= total
                        next = "y"
                    elif count != len(self.bet_check):
                        player_bet -= token
                        next = "y"
                else:
                    while token < self.bet_check[count]:
                        count += 1
                        if count == (len(self.bet_check) - 1):
                            break
                    if token >= self.bet_check[count] and count < (len(self.bet_check) - 1):
                        player_bet -= self.bet_check[count]
                        count += 1
                    elif token == 1:
                        decision_t_n = input("Aby obstawić taką kwotę musisz rozmienić żetony. Rozmienić? (T/N)\n").lower()
                        return decision_t_n
                    else:
                        break

    def bet(self, player_bet):

        count = 0
        bet_chips_list = []
        self.money -= player_bet

        for token in Global.tokens:
            while player_bet >= token:
                if count == len(self.all_chips_list):
                    count = 0
                    break
                if self.all_chips_list[count] == token:
                    bet_chips_list.append(self.all_chips_list.pop(count))
                    player_bet -= token
                    if self.all_chips_list == [] and self.checker(player_bet) != "y":
                        print("ALL IN!")
                elif self.all_chips_list[count] > token:
                    count += 1
                else:
                    count += 1

        return bet_chips_list

    def win_bet(self, amount, player_bet):

        self.money += 2 * player_bet
        self.all_chips_list.extend(2 * amount)

        return self.all_chips_list.sort(reverse=True)

    def draw(self, amount, player_bet):

        self.money += player_bet
        self.all_chips_list.extend(amount)

        return self.all_chips_list.sort(reverse=True)

    def blackjack(self, amount, player_bet):

        self.money += 3 * player_bet
        self.all_chips_list.extend(3 * amount)

        return self.all_chips_list.sort(reverse=True)

    def show_my_chips(self):

        print("To Twoje żetony:")
        print(f"500 ---> {len([x for x in self.all_chips_list if x == 500])}")
        print(f"100 ---> {len([x for x in self.all_chips_list if x == 100])}")
        print(f"50  ---> {len([x for x in self.all_chips_list if x == 50])}")
        print(f"20  ---> {len([x for x in self.all_chips_list if x == 20])}")
        print(f"10  ---> {len([x for x in self.all_chips_list if x == 10])}")
        print(f"5   ---> {len([x for x in self.all_chips_list if x == 5])}")
        print(f"1   ---> {len([x for x in self.all_chips_list if x == 1])}")

    def show_cards(self, all_cards):

        for card in all_cards:
            print(card)
