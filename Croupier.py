from Hand import Hand


class Croupier(Hand):

    def __init__(self):
        self.all_cards = []

    def show_cards(self, all_cards):
        print("Karty krupiera to:")
        for card in all_cards:
            print(card)
